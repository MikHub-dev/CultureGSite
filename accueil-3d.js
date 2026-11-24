/* CultureGSite : 9 scènes 3D ludiques pour les cartes de l'accueil (SVG + petit moteur de projection, sans bibliothèque).
   Usage : <svg viewBox="0 0 400 300" data-3d="philosophie|economie|sante|geopolitique|physique|informatique|maths|etudes|langue">
   Même moteur que IASite / QuantumSite / RoutineSite. */
(function(){
const F=600, D=600, NS='http://www.w3.org/2000/svg';
const RM = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
const f1=v=>Math.round(v*10)/10;
const L=(()=>{const v=[-.45,.75,.55],n=Math.hypot(...v);return v.map(a=>a/n)})();
const PI=Math.PI;

function rot(p,c){const x1=p[0]*c.cy+p[2]*c.sy, z1=-p[0]*c.sy+p[2]*c.cy;return [x1,p[1]*c.cp-z1*c.sp,p[1]*c.sp+z1*c.cp];}
function proj(v,c){const s=c.k*F/(D-v[2]);return [c.x+v[0]*s,c.y-v[1]*s,s];}
const pts=P=>P.map(p=>f1(p[0])+','+f1(p[1])).join(' ');
const hex=h=>[1,3,5].map(i=>parseInt(h.slice(i,i+2),16));
function mix(a,b,k){return 'rgb('+a.map((v,i)=>Math.round(v+(b[i]-v)*k)).join(',')+')';}
const lt=(c,k)=>mix(hex(c),[255,255,255],k), dk=(c,k)=>mix(hex(c),[0,0,0],k);
const add=(a,b)=>[a[0]+b[0],a[1]+b[1],a[2]+b[2]];
const rotYv=(p,a)=>[p[0]*Math.cos(a)+p[2]*Math.sin(a),p[1],-p[0]*Math.sin(a)+p[2]*Math.cos(a)];
const rotZ=(p,a)=>[p[0]*Math.cos(a)-p[1]*Math.sin(a),p[0]*Math.sin(a)+p[1]*Math.cos(a),p[2]];
const rotX=(p,a)=>[p[0],p[1]*Math.cos(a)-p[2]*Math.sin(a),p[1]*Math.sin(a)+p[2]*Math.cos(a)];
const FY=-70;

/* dégradés sphériques partagés (créés à la demande) */
const GR={};
function G(col){const id='c3g'+col.slice(1);GR[id]=col;return `url(#${id})`;}
function gradDefs(){let s='';for(const id in GR){const c=GR[id];
  s+=`<radialGradient id="${id}" cx=".36" cy=".3" r=".72"><stop offset="0" stop-color="${lt(c,.65)}"/><stop offset=".55" stop-color="${c}"/><stop offset="1" stop-color="${dk(c,.55)}"/></radialGradient>`;}
  return s;}

/* primitives */
function ring(r,y,n,a0,a1,fn){const o=[];for(let i=0;i<=n;i++){const a=a0+(a1-a0)*i/n;o.push(fn?fn(r,a):[r*Math.cos(a),y,r*Math.sin(a)]);}return o;}
function segs(P,st,k){const o=[];k=k||1;for(let i=0;i<P.length-1;i+=k)o.push(Object.assign({t:'l',p:P.slice(i,Math.min(i+k,P.length-1)+1)},st));return o;}
function obox(c,h,R,col,alpha,extra){
  R=R||(p=>p);const o=[],[a,b,d]=h;
  const Fc=[[[1,0,0],[[a,-b,-d],[a,-b,d],[a,b,d],[a,b,-d]]],[[-1,0,0],[[-a,-b,-d],[-a,b,-d],[-a,b,d],[-a,-b,d]]],
    [[0,1,0],[[-a,b,-d],[a,b,-d],[a,b,d],[-a,b,d]]],[[0,-1,0],[[-a,-b,-d],[-a,-b,d],[a,-b,d],[a,-b,-d]]],
    [[0,0,1],[[-a,-b,d],[-a,b,d],[a,b,d],[a,-b,d]]],[[0,0,-1],[[-a,-b,-d],[a,-b,-d],[a,b,-d],[-a,b,-d]]]];
  for(const [n,P] of Fc)o.push(Object.assign({t:'f',p:P.map(p=>add(c,R(p))),n:R(n),col:hex(col),alpha:alpha==null?1:alpha,flat:true},extra||{}));
  return o;
}
function cyl(c,r,h,col,n,R){n=n||16;R=R||(p=>p);const o=[],top=[],cc=hex(col);
  for(let i=0;i<n;i++){const a=i/n*2*PI,b=(i+1)/n*2*PI,m=(a+b)/2;
    o.push({t:'f',p:[[r*Math.cos(a),0,r*Math.sin(a)],[r*Math.cos(b),0,r*Math.sin(b)],[r*Math.cos(b),h,r*Math.sin(b)],[r*Math.cos(a),h,r*Math.sin(a)]].map(q=>add(c,R(q))),n:R([Math.cos(m),0,Math.sin(m)]),col:cc,alpha:1,flat:true});
    top.push(add(c,R([r*Math.cos(-a),h,r*Math.sin(-a)])));}
  o.push({t:'f',p:top,n:R([0,1,0]),col:cc.map(v=>Math.round(v+(255-v)*.25)),alpha:1,flat:true});
  return o;}
const sph=(c,r,col,ex)=>Object.assign({t:'b',p:[c],r,fill:col.startsWith('#')?G(col):col},ex||{});
const cap=(a,b,r,c1,c2,ex)=>Object.assign({t:'cap',p:[a,b],r,c1,c2:c2||lt(c1,.35),o2:.6},ex||{});
const tx=(p,s,fs,fill,ex)=>Object.assign({t:'tx',p:[p],s,fs,fill,b:3000},ex||{});
const bub=(p,tip,s,col,ex)=>Object.assign({t:'bub',p:[p,tip],s,col,fs:12,b:4000},ex||{});
function disc(c,r,col,op,b){return {t:'poly',p:ring(r,0,40,0,2*PI).map(q=>add(c,q)),fill:col,op,b:b==null?-2000:b};}
function floor(r,col){
  const o=[{t:'poly',p:ring(r,FY,64,0,2*PI),fill:`url(#c3f${col.slice(1)})`,b:-3000}];
  o.push(...segs(ring(r+4,FY,96,0,2*PI),{s:col,o:.45,w:1,b:-2900,da:'2 6'},96));
  o.push(...segs(ring(r*.6,FY,64,0,2*PI),{s:col,o:.14,w:.8,b:-2950},64));
  return o;
}
/* yeux : deux billes blanches + pupilles, sur un visage tourné vers +z local */
function yeux(W,y,z,ec,r,look){r=r||3.6;look=look||[0,0];const o=[];
  for(const s of [-1,1]){o.push(sph(W([s*ec,y,z]),r,'#ffffff',{b:20}));o.push({t:'b',p:[W([s*ec+look[0]*r*.4,y+look[1]*r*.4,z+r*.8])],r:r*.5,fill:'#14161e',b:21});}
  return o;}
/* petit personnage (pieds à l'origine locale, regarde +z) ; W : local -> monde */
function perso(W,o){
  const out=[],sk=o.skin||'#e9b48c',bd=o.body,lg=o.legs||'#2b3242';
  const hipY=o.assis?o.assis:44, top=hipY+34, hy=top+16;
  for(const s of [-1,1]){
    if(o.assis){out.push(cap(W([s*6,hipY,2]),W([s*7,hipY,22]),5.5,lg,lt(lg,.2)),cap(W([s*7,hipY,22]),W([s*7,(o.pied||0)+3,24]),5,lg,lt(lg,.2)));}
    else out.push(cap(W([s*6,hipY,0]),W(o.pieds?o.pieds[s<0?0:1]:[s*7,3,0]),5.5,lg,lt(lg,.2)));
  }
  out.push(cap(W([0,hipY+6,0]),W([0,top,0]),12.5,bd));
  const mains=o.mains||[[-15,hipY,4],[15,hipY,4]];
  mains.forEach((m,i)=>{const s=i?1:-1;
    if(o.coudes){out.push(cap(W([s*13,top,0]),W(o.coudes[i]),4.3,bd),cap(W(o.coudes[i]),W(m),4.3,bd));}
    else out.push(cap(W([s*13,top,0]),W(m),4.3,bd));
    out.push(sph(W(m),4,sk));});
  if(o.cheveux)out.push(sph(W([0,hy+3,-3.5]),12.6,o.cheveux));
  out.push(sph(W([0,hy,0]),12,sk));
  if(o.yeux!==false)out.push(...yeux(W,hy+2,9.5,4.2,2.6,o.look));
  return out;
}

/* ---------- 1. Philosophie : Socrate et un robot en méditation ---------- */
const MENTHE='#7ee0c3';
function philoDyn(t){
  const o=floor(118,MENTHE);
  /* Socrate, assis sur un bloc de marbre */
  const aS=1.05,WS=p=>add(rotYv(p,aS),[-58,FY,-4]);
  o.push(...obox(WS([0,12,-2]),[15,12,13],p=>rotYv(p,aS),'#9aa7a4'));
  o.push(...obox(WS([0,25,-2]),[17,1.5,15],p=>rotYv(p,aS),'#c3ccca'));
  const g=Math.sin(t*2.4);
  o.push(...perso(WS,{assis:27,body:'#e9efe9',skin:'#e2ab83',yeux:false,
    mains:[[-11,29,20],[19,72+6*g,15]],coudes:[[-15,44,8],[20,55,10]]}));
  o.push(cap(WS([18,76+6*g,15]),WS([19,84+6*g,16]),1.6,'#e2ab83'));
  o.push(cap(WS([-12,58,6]),WS([11,33,9]),3.2,MENTHE,lt(MENTHE,.4)));
  const hy=27+34+16;
  for(const s of [-1,1])o.push(sph(WS([s*8.5,hy-2,-6]),5,'#dfe4e3'));
  o.push(sph(WS([0,hy-8,9]),8.5,'#e8ecea',{b:3}),sph(WS([0,hy-14,8]),7,'#d5dbd9',{b:2}),sph(WS([0,hy-3,11]),5,'#e8ecea',{b:3}));
  for(const s of [-1,1])o.push({t:'b',p:[WS([s*4.2,hy+2,11.2])],r:1.6,fill:'#20242c',b:4});
  o.push(sph(WS([0,hy-1,12.5]),2.6,'#e2ab83',{b:5}));
  /* robot zen en lévitation, jambes croisées */
  const bob=RM?0:4*Math.sin(t*1.6),aR=-1.0,WR=p=>add(rotYv(p,aR),[56,FY+16+bob,4]),R=p=>rotYv(p,aR);
  o.push(disc([56,FY+.5,4],20-bob*.8,'#000',.35));
  o.push(cap(WR([-19,8,4]),WR([13,5,17]),6,'#8fa3b0','#c4d3dc'),cap(WR([19,8,4]),WR([-13,5,17]),6,'#8fa3b0','#c4d3dc'));
  o.push(...obox(WR([0,30,0]),[13,16,9],R,'#c7d3dc'));
  o.push(sph(WR([0,34,9.6]),4,MENTHE,{b:2}));
  o.push(...obox(WR([0,60,0]),[13,11,11],R,'#dbe5ec'));
  o.push(...obox(WR([0,60,11.3]),[10,6,.6],R,'#0e1e26'));
  for(const s of [-1,1]){const P=[];for(let i=0;i<=6;i++){const a=PI*i/6;P.push(WR([s*4.6+3*Math.cos(a),60.5-1.6*Math.sin(a),12.3]));}
    o.push({t:'l',p:P,s:MENTHE,w:1.6,b:20});}
  o.push({t:'l',p:[WR([0,71,0]),WR([0,80,0])],s:'#c7d3dc',w:1.6});
  o.push(sph(WR([0,82,0]),3.4,MENTHE,{fl:'c3glow'}));
  for(const s of [-1,1]){const sh=[s*15,42,0],el=[s*20,26,7],h=[s*15,12,15];
    o.push(cap(WR(sh),WR(el),3.6,'#9fb0bd','#d7e2e9'),cap(WR(el),WR(h),3.6,'#9fb0bd','#d7e2e9'),sph(WR(h),3.6,'#c7d3dc'));}
  /* aura */
  for(let k=0;k<2;k++){const r=30+((t*14+k*20)%40),op=RM?.25:Math.max(0,.5*(1-(r-30)/40));
    o.push(...segs(ring(r,0,48,0,2*PI).map(q=>add(q,[56,FY+30+bob,4])),{s:MENTHE,o:op,w:1.2,b:-50},4));}
  /* dialogue */
  const ph=RM?0:Math.floor(t/2.6)%3;
  if(ph===0)o.push(bub([-40,52,0],WS([6,90,6]),'Connais-toi toi-même !',MENTHE));
  if(ph===1)o.push(bub([40,64,0],WR([0,84,0]),'Je relis mon code…',MENTHE));
  if(ph===2)o.push(bub([46,64,0],WR([0,84,0]),'Ommm… 0101…',MENTHE));
  return o;
}

/* ---------- 2. Économie : personnage en blocs qui fait pleuvoir les billets ---------- */
const OR='#f2c879';
function ecoDyn(t){
  const o=floor(118,OR);
  const a=-.25,P0=[-14,FY,6],W=p=>add(rotYv(p,a),P0),R=p=>rotYv(p,a);
  o.push(disc([-14,FY+.5,6],24,'#000',.35));
  const hop=RM?0:Math.abs(Math.sin(t*4))*3;
  const Wh=p=>W([p[0],p[1]+hop,p[2]]);
  for(const s of [-1,1])o.push(...obox(W([s*5.5,13+hop*.5,0]),[5,13+hop*.5,5.5],R,'#363a52'));
  o.push(...obox(Wh([0,41,0]),[13,13,7],R,OR));
  o.push(...obox(Wh([0,41,7.3]),[3.4,12,.4],R,'#f4f6fb'),...obox(Wh([0,38,7.9]),[1.5,9,.4],R,'#d64560'));
  o.push(...obox(Wh([0,65,0]),[10.5,10.5,10.5],R,'#f5c49c'));
  o.push(...obox(Wh([0,67,10.9]),[9.5,2.6,.5],R,'#111318'));
  o.push(...obox(Wh([4.5,67.6,11.5]),[2,.6,.2],R,'#5fd4ff',.9));
  o.push({t:'l',p:[Wh([-5.5,59.5,11]),Wh([-2,57.2,11]),Wh([2,57.2,11]),Wh([5.5,59.5,11])],s:'#1d2330',w:1.8,b:20});
  o.push(...obox(Wh([0,76.5,0]),[14,1,14],R,'#1d2028'),...obox(Wh([0,84,0]),[8.5,7,8.5],R,'#1d2028'),...obox(Wh([0,79,0]),[8.8,1.6,8.8],R,OR));
  /* bras gauche : tient la liasse ; bras droit : lance en éventail */
  const fl=RM?0:.35*Math.sin(t*9);
  const armL=p=>R(rotX(p,-1.25)),armR=p=>R(rotZ(rotX(p,-.15),2.45+fl));
  const shL=Wh([-17,50,0]),shR=Wh([17,50,0]);
  o.push(...obox(add(shL,armL([0,-10,0])),[3.6,11,3.6],armL,OR));
  o.push(...obox(add(shL,armL([0,-22,0])),[5,1.5,8],armL,'#7fbf6a'));
  o.push(...obox(add(shR,armR([0,-10,0])),[3.6,11,3.6],armR,OR));
  const H=add(shR,armR([0,-23,0]));
  for(let k=-2;k<=2;k++){const rr=p=>armR(rotZ(p,k*.25));o.push(...obox(add(H,rr([0,-6,0])),[3.6,8,.3],rr,'#8fd17a'));}
  /* pluie de billets : fontaine autour du personnage */
  const N=16;
  for(let i=0;i<N;i++){
    const u=RM?(i/N):((t*.4+i/N)%1),dir=-1.3+2.4*((i*5)%N)/N,sp=46+(i*13%24);
    const x=H[0]+4+sp*Math.cos(dir)*u*1.5+6*Math.sin(u*14+i),z=H[2]+sp*Math.sin(dir)*u*1.1+5*Math.cos(u*11+i);
    let y=H[1]+6+70*u-170*u*u;const land=y<FY+1;if(land)y=FY+1;
    const ax=land?0:u*9+i,ay=u*5+i*1.3,Rb=p=>rotYv(rotX(rotZ(p,land?0:Math.sin(u*10+i)*.8),ax),ay);
    const op=u>.85?Math.max(0,(1-u)/.15):Math.min(1,u*8);
    o.push(...obox([x,y,z],[7.5,.3,3.8],Rb,'#8fd17a',op));
    o.push(...obox(add([x,y,z],Rb([0,.4,0])),[2,.05,2],Rb,'#4c8a3e',op));
  }
  /* piles de pièces */
  [[-66,-10,6],[-48,-30,4],[-74,16,3],[56,-30,2]].forEach(([x,z,n])=>{for(let k=0;k<n;k++)o.push(...cyl([x+(k%2)*.8,FY+k*3.4,z],8,3,k%2?'#e0b25e':OR,14));});
  const wob=RM?0:Math.sin(t*3)*3;
  o.push(tx([-50,40+wob,0],'money money !',17,OR,{fw:800,op:.95}));
  return o;
}

/* ---------- 3. Santé : le brocoli fait de la muscu ---------- */
const VERT='#7fe3b2';
function santeDyn(t){
  const o=floor(118,VERT);
  const c=RM?.5:.5-.5*Math.cos(t*2.6),B=48+20*c,sq=1-c;
  const W=p=>[p[0],p[1]-sq*4,p[2]];
  o.push(disc([0,FY+.5,0],26,'#000',.35));
  for(const s of [-1,1]){o.push(cap([s*7,FY+20,0],[s*11,FY+3,5],3.8,'#8fc56f'),sph([s*11,FY+3,8],5,'#5fae58'));}
  o.push(cap(W([0,FY+20,0]),W([0,-2,0]),12,'#9ccf7f','#c9f0b0'));
  const fl=[[0,26,0,21],[-19,15,2,15],[19,15,2,15],[-11,33,-7,14],[11,35,-6,14],[0,12,10,14],[-8,38,6,11],[9,36,8,11],[0,45,-2,12]];
  for(const [x,y,z,r] of fl)o.push(sph(W([x,y,z]),r,'#3f9e5a'));
  o.push(...yeux(W,-16,11.5,5,3.8,[0,1]));
  o.push(...obox(W([0,-29,11.6]),[5,1.6,.4],null,'#ffffff'));
  o.push({t:'l',p:[W([-6,-27,11.7]),W([-6,-31,11.7])],s:'#2a5a34',w:1});
  /* bras + haltère */
  for(const s of [-1,1]){const hd=[s*24,B,9];o.push(cap(W([s*11,-22,2]),W([s*20,(B-22)/2-4,10]),3.6,'#8fc56f'),cap(W([s*20,(B-22)/2-4,10]),W(hd),3.6,'#8fc56f'),sph(W(hd),4.2,'#5fae58'));}
  o.push(cap(W([-52,B,9]),W([52,B,9]),1.8,'#8a93a6','#d9dee8',{b:30}));
  for(const s of [-1,1])for(const [x,r,h] of [[38,14,5],[44,10,4]]){
    o.push(...cyl(W([s>0?x:-x-h,B,9]),r,h,s>0?'#3a4560':'#3a4560',18,p=>rotZ(p,-PI/2)).map(f=>Object.assign(f,{b:30})));}
  /* gouttes de sueur, compteur */
  for(let k=0;k<2;k++){const u=RM?.3:((t*.8+k*.5)%1);o.push(sph(W([(k?1:-1)*(22+12*u),50-40*u,6]),2.4,'#9fe8ff',{op:1-u}));}
  const rep=RM?3:1+Math.floor((t*2.6+PI)/(2*PI))%10;
  o.push(tx([-98,30,0],'Rép. '+rep,16,VERT,{fw:800}));
  const hb=RM?1:1+.18*Math.max(0,Math.sin(t*6));
  o.push(tx([-98,4,0],'♥',22*hb,'#ff6b8b',{fw:800}));
  return o;
}

/* ---------- 4. Géopolitique : tir à la corde sur le globe ---------- */
const ROUGE='#ff5a6e';
function geoDyn(t){
  const o=floor(118,ROUGE);
  const C=[0,-18,0],Rg=46,spin=RM?0:t*.5;
  o.push(...obox([0,FY+3,0],[22,3,22],null,'#3a2a33'),cap([0,FY+6,0],[0,C[1]-Rg+4,0],3,'#6b4a55'));
  o.push(sph(C,Rg,'#24345e',{b:0}));
  for(let k=0;k<6;k++){const a0=spin+k*PI/6;
    o.push(...segs(ring(Rg+.6,0,40,0,2*PI,(r,a)=>add(C,rotYv([r*Math.sin(a),r*Math.cos(a),0],a0))),{s:ROUGE,o:.55,w:1},2));}
  for(const la of [-.5,0,.5]){const rr=Rg*Math.cos(la);o.push(...segs(ring(rr+.6,Rg*Math.sin(la),40,0,2*PI).map(q=>add(C,q)),{s:ROUGE,o:.4,w:.9},2));}
  /* drapeaux plantés */
  [[.4,.3,'#ffd166'],[2.3,-.2,'#5fd4ff'],[4.1,.5,'#7fe3b2']].forEach(([lo,la,c])=>{
    const n=rotYv([Math.cos(la)*Math.sin(lo),Math.sin(la),Math.cos(la)*Math.cos(lo)],spin);
    const base=add(C,n.map(v=>v*Rg)),tip=add(C,n.map(v=>v*(Rg+16)));
    o.push({t:'l',p:[base,tip],s:'#d9dee8',w:1.3},{t:'poly',p:[tip,add(tip,[8,-3,0]),add(tip,[0,-6,0])],fill:c});});
  /* deux dirigeants tirent la corde */
  const pull=RM?0:.12*Math.sin(t*2.2),ld=[];
  [[-1,'#4a6fd1'],[1,'#d64560']].forEach(([s,col])=>{
    const th=s*(.34+pull*s),lean=-s*.08;
    const foot=add(C,[Rg*Math.sin(th),Rg*Math.cos(th),0]);
    const W=p=>add(rotZ(rotZ(rotYv(p.map(v=>v*.36),-s*PI/2),lean),-th),foot);
    const hand=[0,48,16];
    o.push(...perso(W,{body:col,cheveux:'#2b2118',mains:[[-4,46,16],[4,48,17]],look:[0,0]}));
    ld.push(W(hand));});
  const mid=[(ld[0][0]+ld[1][0])/2,Math.max(ld[0][1],ld[1][1])+2,(ld[0][2]+ld[1][2])/2];
  const rope=[];for(let i=0;i<=12;i++){const u=i/12,q=1-4*(u-.5)**2;rope.push([ld[0][0]+(ld[1][0]-ld[0][0])*u,ld[0][1]+(ld[1][1]-ld[0][1])*u+q*1.5,ld[0][2]+(ld[1][2]-ld[0][2])*u]);}
  o.push(...segs(rope,{s:'#e8c27a',w:2.2,b:40},2));
  o.push(sph(add(mid,[0,0,0]),2.6,ROUGE,{b:50}));
  const ph=RM?0:Math.floor(t/1.8)%2;
  o.push(ph?bub([60,62,0],ld[1],'Non, à moi !',ROUGE):bub([-58,62,0],ld[0],'À moi !',ROUGE));
  return o;
}

/* ---------- 5. Physique : la pomme de Newton ---------- */
const CYAN='#5fd4ff';
function physDyn(t){
  const o=floor(118,CYAN);
  const TX=-30,TZ=-20;
  o.push(cap([TX,FY,TZ],[TX,30,TZ],8,'#6b4a32','#8a6446'),cap([TX,18,TZ],[TX+18,40,TZ],4,'#6b4a32','#8a6446'));
  for(const [x,y,z,r] of [[0,48,0,28],[-24,38,4,20],[22,40,8,20],[-8,64,-6,20],[14,62,4,18],[2,40,18,16]])o.push(sph([TX+x,y,TZ+z],r,'#2f9e7e'));
  for(const [x,y,z] of [[-12,40,24],[18,52,20],[-22,56,10]])o.push(sph([TX+x,y,TZ+z],3.5,'#ff5a6e',{b:1}));
  /* Newton assis contre l'arbre */
  const NX=-14,NZ=6,W=p=>add(rotYv(p,.25),[NX,FY,NZ]);
  o.push(...perso(W,{assis:9,pied:0,body:'#3d5a8a',mains:[[-12,12,24],[13,12,24]],yeux:false}));
  const hy=9+34+16;
  for(const [x,y,z] of [[-11,hy+2,-2],[11,hy+2,-2],[-12,hy-8,-2],[12,hy-8,-2],[0,hy+8,-4]])o.push(sph(W([x,y,z]),7,'#eceef4'));
  /* la pomme tombe : bonk ! */
  const u=RM?.6:(t*.33)%1,head=W([0,hy+12,2]);
  let A,bonk=u>.32&&u<.85;
  if(u<.32){const k=u/.32;A=[head[0]+2,46-(46-head[1])*k*k,head[2]+2];}
  else{const k=Math.min(1,(u-.32)/.45);A=[head[0]+2+52*k,head[1]+38*k-70*k*k,head[2]+16*k];if(A[1]<FY+6)A[1]=FY+6;}
  o.push(sph(A,6.5,'#ff5a6e',{b:60}),{t:'l',p:[add(A,[0,6,0]),add(A,[1.5,10,0])],s:'#6b4a32',w:1.4,b:61});
  const eyesY=hy+2;
  if(bonk){for(const s of [-1,1]){o.push({t:'l',p:[W([s*4.2-1.6,eyesY+1.6,11.4]),W([s*4.2+1.6,eyesY-1.6,11.4])],s:'#20242c',w:1.3,b:5},{t:'l',p:[W([s*4.2-1.6,eyesY-1.6,11.4]),W([s*4.2+1.6,eyesY+1.6,11.4])],s:'#20242c',w:1.3,b:5});}
    for(let k=0;k<5;k++){const a=t*4+k*2*PI/5;o.push(tx(add(head,[18*Math.cos(a),6+3*Math.sin(a*2),18*Math.sin(a)]),'★',11,'#ffd166'));}
    o.push(tx([58,40,0],'BONK !',18,CYAN,{fw:800}));}
  else for(const s of [-1,1])o.push({t:'b',p:[W([s*4.2,eyesY,11.2])],r:1.7,fill:'#20242c',b:4});
  if(u>.5)o.push(bub([60,8,0],W([8,hy+4,10]),'Eurêka : F = m·g !',CYAN,{op:Math.min(1,(u-.5)/.1)}));
  return o;
}

/* ---------- 6. Informatique : la chasse au bug ---------- */
const BLEU='#7aa2ff';
function infoDyn(t){
  const o=floor(118,BLEU);
  const LX=-4,LZ=-4;
  o.push(...obox([LX,FY+3,LZ],[40,3,26],null,'#9aa3b2'));
  o.push(...obox([LX,FY+6.2,LZ+4],[33,.3,14],null,'#2a2f3a'));
  for(let r=0;r<3;r++)o.push({t:'l',p:[[LX-30,FY+6.8,LZ-4+r*7],[LX+30,FY+6.8,LZ-4+r*7]],s:'#56607a',w:3,da:'4 2'});
  const tl=-.28,Rs=p=>rotX(p,tl),hinge=[LX,FY+6,LZ-26];
  o.push(...obox(add(hinge,Rs([0,26,-1.5])),[40,26,1.5],Rs,'#8a93a6'));
  const S=(x,y)=>add(hinge,Rs([x,y,.3]));
  o.push({t:'poly',p:[S(-36,3),S(36,3),S(36,49),S(-36,49)],fill:'#0b1226',b:5});
  const err=RM?1:Math.floor(t*1.2)%2;
  [[0,BLEU,.8],[1,'#e6eefc',.5],[2,'#7ee0c3',.7],[1,'#e6eefc',.45],[0,'#ffb86b',.6]].forEach(([ind,c,w],i)=>{
    o.push({t:'l',p:[S(-30+ind*6,44-i*6),S(-30+ind*6+50*w,44-i*6)],s:c,w:2.2,o:.85,b:6});});
  o.push(tx(S(0,8),err?'ERREUR 404':'chargement…',10,err?'#ff5a6e':BLEU,{fw:700,b:7}));
  /* le bug court en huit sur le clavier */
  const s=RM?0:t*1.3,bx=LX+30*Math.sin(s),bz=LZ+6+11*Math.sin(2*s),hd=Math.atan2(30*Math.cos(s),22*Math.cos(2*s));
  const Wb=p=>add(rotYv(p.map(v=>v*1.25),hd),[bx,FY+7,bz]);
  for(let k=0;k<3;k++)for(const sd of [-1,1]){const w=RM?0:Math.sin(t*20+k*2+sd)*1.6;o.push({t:'l',p:[Wb([sd*4,2,-3+k*3]),Wb([sd*9,0,-3+k*3+w])],s:'#14161e',w:1.2});}
  o.push(sph(Wb([0,4,-1]),7,'#ff5a6e'),sph(Wb([0,4,6.5]),3.8,'#20242c'));
  for(const [x,z] of [[-3,-3],[3,-3],[0,-6],[-3,2],[3,2]])o.push({t:'b',p:[Wb([x,9.5,z])],r:1.3,fill:'#14161e',b:8});
  for(const sd of [-1,1]){o.push({t:'l',p:[Wb([sd*1.5,6,9]),Wb([sd*5,12,14])],s:'#14161e',w:1},sph(Wb([sd*1.6,5.6,9.6]),1.3,'#ffffff',{b:9}));}
  /* tasse de café */
  const MX=48,MZ=22;
  o.push(cap([MX,FY+2,MZ],[MX,FY+15,MZ],8,'#d9dee8','#ffffff',{o2:.9}));
  o.push(...segs(ring(5,0,16,-PI/2,PI/2,(r,a)=>[MX+8+r*Math.cos(a),FY+9+r*Math.sin(a),MZ]),{s:'#d9dee8',w:2.2}));
  for(let k=0;k<2;k++){const P=[];for(let i=0;i<=8;i++){const v=i/8;P.push([MX-2+k*4+2.5*Math.sin(v*6+t*3+k),FY+24+v*22,MZ]);}o.push(...segs(P,{s:'#cfd8ea',o:.5,w:1.4},2));}
  o.push(bub([-30,30,0],S(-20,49),'Il est où ce bug ?!',BLEU));
  return o;
}

/* ---------- 7. Maths : π jongle avec ses décimales ---------- */
const VIOLET='#b8a6ff',DEC='31415926535897932384';
function mathsDyn(t){
  const o=floor(118,VIOLET);
  /* socle : la somme infinie qui vaut un nombre fini */
  o.push(...cyl([22,FY,0],32,6,'#3a3266',24),...cyl([22,FY+6,0],24,10,'#4b4183',24));
  const C=[22,FY+16+50,0],R=50,sp=RM?0:t*.35;
  /* la boule de verre : fond (derrière) puis reflets (devant) */
  o.push({t:'b',p:[C],r:R,fill:'rgba(184,166,255,.10)',s:VIOLET,sw:1.6,b:-400});
  /* l'infini emprisonné : des sphères emboîtées, chacune deux fois plus petite, qui plongent sans fin */
  const u=RM?.5:(t*.28)%1;
  for(let n=0;n<9;n++){
    const r=R*.88*Math.pow(.5,n+u);if(r<.25)break;
    const op=(n===0?u:1)*(.85-n*.05),a0=sp*(n%2?-1.4:1)+n*.7,col=n%2?'#d8cfff':VIOLET,w=Math.max(.35,1.4-n*.12);
    const ringA=ring(r,0,36,0,2*PI).map(q=>add(C,rotYv(rotX(q,.35),a0)));
    const ringB=ring(r,0,36,0,2*PI,(rr,a)=>[rr*Math.cos(a),rr*Math.sin(a),0]).map(q=>add(C,rotYv(q,a0)));
    const ringC=ring(r,0,36,0,2*PI,(rr,a)=>[0,rr*Math.sin(a),rr*Math.cos(a)]).map(q=>add(C,rotYv(q,a0)));
    for(const P of [ringA,ringB,ringC])o.push(...segs(P,{s:col,o:op,w},3));
  }
  o.push({t:'b',p:[C],r:2.2,fill:'#ffffff',fl:'c3glow',b:300});
  o.push({t:'b',p:[add(C,[-14,16,R*.7])],r:6,fill:'rgba(255,255,255,.35)',b:400},{t:'b',p:[add(C,[-20,8,R*.6])],r:2.5,fill:'rgba(255,255,255,.5)',b:401});
  o.push(tx([22,FY+3,36],'1 + ½ + ¼ + ⅛ + … = 2',9.5,'#efeaff',{fw:600}));
  /* π observe à la loupe */
  const W=p=>add(rotYv(p.map(v=>v*.62),.5),[-66,FY,18]),R9=p=>rotYv(p,.5),bob=RM?0:1.2*Math.sin(t*4);
  o.push(disc([-66,FY+.5,18],18,'#000',.35));
  const K=.62,hs=h=>h.map(v=>v*K);
  o.push(...obox(W([-15,47,0]),hs([5.5,47,6]),R9,VIOLET),...obox(W([15,45,0]),hs([5.5,45,6]),R9,VIOLET),...obox(W([21,3,0]),hs([7,3,6]),R9,VIOLET));
  o.push(...obox(W([0,100+bob,0]),hs([36,6.5,7]),R9,'#c9bcff'),...obox(W([-36,95+bob,0]),hs([4,6,7]),R9,'#c9bcff'));
  o.push(...yeux(p=>W([p[0],p[1]+bob,p[2]]),102,7.5,9,4.6,[1,0]));
  const lp=W([32,100+bob,30]);
  o.push(cap(W([30,96+bob,4]),lp,1.8,VIOLET),cap(lp,W([24,88+bob,40]),1.6,'#6b4a32'));
  o.push({t:'b',p:[W([34,104+bob,34])],r:5.5,fill:'rgba(200,230,255,.25)',s:'#e8e2ff',sw:1.4,b:20});
  o.push(bub([-30,52,0],W([0,112,0]),"L'infini… dans une boule !",VIOLET));
  return o;
}

/* ---------- 8. Études : le lancer de toque ---------- */
const ORANGE='#ffb86b';
function etudesDyn(t){
  const o=floor(118,ORANGE);
  const ph=RM?.3:(t*.55)%1,j=RM?0:Math.max(0,Math.sin(ph*2*PI))*12;
  /* pile de livres */
  [['#4a6fd1',0],['#d64560',.2],['#7ee0c3',-.15],['#ffd166',.1]].forEach(([c,a],k)=>{
    const Rb=p=>rotYv(p,a);o.push(...obox([-62,FY+4+k*8,-6],[18,4,12],Rb,c),...obox(add([-62,FY+4+k*8,-6],Rb([1.5,0,0])),[17,3.2,12.3],Rb,'#f1ece0'));});
  /* élève qui saute, bras en l'air */
  o.push(disc([6,FY+.5,6],22-j*.4,'#000',.35));
  const W=p=>[p[0]*.95+6,p[1]*.95+FY+j,p[2]*.95+6];
  o.push(...perso(W,{body:'#2a2f45',cheveux:'#3a2a1d',mains:[[-22,104,6],[22,104,6]],coudes:[[-20,90,2],[20,90,2]],pieds:[[-9,3,-6],[9,3,6]]}));
  o.push(cap(W([-12,76,7]),W([10,48,9]),2.6,ORANGE,lt(ORANGE,.4)));
  o.push({t:'l',p:[W([-4,94,11.5]),W([0,92,11.8]),W([4,94,11.5])],s:'#5a2a1d',w:1.6,b:10});
  /* la toque s'envole */
  const k=RM?.4:ph,hy=FY+108+52*Math.sin(PI*k),spin=k*2*PI*2,tlt=Math.sin(k*2*PI)*.5;
  const C=[6,hy,6],Rc=p=>rotYv(rotX(p,tlt),spin);
  o.push(...obox(C,[16,1.1,16],Rc,'#1e2233'),...obox(add(C,Rc([0,-4.5,0])),[8,3.6,8],Rc,'#262b40'));
  const corner=add(C,Rc([15,0,15]));
  o.push({t:'l',p:[add(C,Rc([0,1.2,0])),add(C,Rc([10,1.2,10])),corner,add(corner,[0,-11,0])],s:'#ffd166',w:1.4,b:20},sph(add(corner,[0,-12,0]),2.4,'#ffd166',{b:21}));
  /* confettis */
  for(let i=0;i<16;i++){const u=RM?(i/16):((t*.35+i/16)%1),x=-70+((i*53)%140),z=-30+((i*37)%70);
    const Rf=p=>rotYv(rotX(p,u*12+i),u*7+i);o.push(...obox([x+6*Math.sin(u*8+i),95-170*u,z],[2.6,.2,1.6],Rf,['#ffd166','#ff6b8b','#7ee0c3','#7aa2ff',ORANGE][i%5],u>.9?(1-u)*10:1));}
  o.push(tx([-80,30,0],'ADMIS !',20,ORANGE,{fw:800,op:ph>.15&&ph<.85?1:.35}));
  return o;
}

/* ---------- 9. Langue : les accents s'envolent du dictionnaire ---------- */
const ROSE='#ff6b8b',LETTRES=['é','à','ç','ê','ù','œ','ï','«»','è','ô','Aa','â'];
function langueDyn(t){
  const o=floor(118,ROSE);
  const BZ=0;
  o.push(disc([0,FY+.5,BZ],46,'#000',.3));
  for(const s of [-1,1]){const Rp=p=>rotZ(p,-s*.16),c=[s*25,FY+8,BZ];
    o.push(...obox(add(c,[0,-2.5,0]),[26,1.5,32],Rp,'#8a2e48'));
    o.push(...obox(c,[24,2.5,30],Rp,'#f3eee4'));
    for(let i=0;i<6;i++){const z=-22+i*8;o.push({t:'l',p:[add(c,Rp([-18,2.8,z])),add(c,Rp([(i===5?2:18),2.8,z]))],s:'#b9b1c4',w:1,o:.8});}}
  /* le rouge-gorge qui sautille sur le dictionnaire */
  const ph=RM?0:(t*1.4)%1,hop=RM?0:Math.max(0,Math.sin(ph*2*PI))*7,tl=RM?0:.25*Math.sin(t*5);
  const rb=p=>add(rotYv(p.map(v=>v*1.5),-.35),[34,FY+11+hop,4]);
  for(const s of [-1,1]){o.push({t:'l',p:[rb([s*3,5,0]),rb([s*3.4,0,1])],s:'#c98a4a',w:1.4},{t:'l',p:[rb([s*3.4,0,1]),rb([s*3.4,0,4])],s:'#c98a4a',w:1.2});}
  o.push({t:'poly',p:[rb([-3,12,-9]),rb([3,12,-9]),rb([5,7+tl*8,-22]),rb([-5,7+tl*8,-22])],fill:'#6b5134',b:-5});
  o.push(sph(rb([0,13,-1]),12,'#8a6a45'));
  o.push(sph(rb([0,13,6]),8,'#f2642e',{b:2}));
  for(const s of [-1,1])o.push({t:'poly',p:[rb([s*9,18,2]),rb([s*11,13,-4]),rb([s*9,9,-12]),rb([s*7.5,15,-6])],fill:'#6b5134',b:3});
  const hb=RM?0:Math.sin(t*3)*.25,H=rb([0,23,3]);
  o.push(sph(H,8,'#8a6a45',{b:4}));
  o.push(sph(rb([0,20.5,7]),6,'#f2642e',{b:5}));
  const bk=rb([Math.sin(hb)*2,22.5,10]);
  o.push({t:'poly',p:[add(bk,[-2.6,1.4,0]),add(bk,[2.6,1.4,0]),add(bk,rotYv([0,-.8,8],-.35+hb))],fill:'#3a2a1d',b:7});
  for(const s of [-1,1]){o.push({t:'b',p:[rb([s*4,25,8])],r:2.1,fill:'#ffffff',b:6},{t:'b',p:[rb([s*4.1,25.2,9.4])],r:1.2,fill:'#14161e',b:7});}
  const hd=rb([0,31,2]);
  /* plume qui écrit */
  const qx=RM?0:Math.sin(t*2.2)*8,tip=[-24+qx,FY+11.5,10];
  o.push({t:'l',p:[tip,add(tip,[16,40,-6])],s:'#cfd8ea',w:1.6,b:30});
  const fe=[];for(let i=0;i<=10;i++){const v=i/10,w=9*Math.sin(PI*v);fe.push(add(tip,[10+16*v*.8+w*.6,18+40*v*.55-w*.4,-4*v]));}
  for(let i=10;i>=0;i--){const v=i/10,w=9*Math.sin(PI*v);fe.push(add(tip,[10+16*v*.8-w*.6,18+40*v*.55+w*.4,-4*v]));}
  o.push({t:'poly',p:fe,fill:'#ffe3ea',op:.92,s:ROSE,so:.6,b:31});
  /* tourbillon de lettres */
  const N=LETTRES.length;
  LETTRES.forEach((s,i)=>{const u=RM?(i/N):((t*.16+i/N)%1),a=u*5+i*2*PI/N,r=12+48*u;
    o.push(tx([r*Math.cos(a),FY+14+u*95,BZ+r*Math.sin(a)],s,15+8*u,lt(ROSE,.35),{fw:700,op:Math.sin(PI*u)*.95,ff:'Georgia,serif'}));});
  o.push(bub([50,34,0],hd,'Cui ! Zéro faute !',ROSE));
  return o;
}

const CFG={
  philosophie:{dyn:philoDyn,col:MENTHE,auto:t=>.35*Math.sin(t*.25),yaw0:0},
  economie:{dyn:ecoDyn,col:OR,auto:t=>.4*Math.sin(t*.3),yaw0:.1},
  sante:{dyn:santeDyn,col:VERT,auto:t=>.45*Math.sin(t*.28),yaw0:-.2},
  geopolitique:{dyn:geoDyn,col:ROUGE,auto:t=>.4*Math.sin(t*.25),yaw0:0},
  physique:{dyn:physDyn,col:CYAN,auto:t=>.4*Math.sin(t*.27),yaw0:.25},
  informatique:{dyn:infoDyn,col:BLEU,k:1.6,cy:140,auto:t=>.4*Math.sin(t*.3),yaw0:-.25},
  maths:{dyn:mathsDyn,col:VIOLET,auto:t=>.45*Math.sin(t*.26),yaw0:.2},
  etudes:{dyn:etudesDyn,col:ORANGE,auto:t=>.4*Math.sin(t*.3),yaw0:0},
  langue:{dyn:langueDyn,col:ROSE,k:1.5,cy:170,auto:t=>.45*Math.sin(t*.24),yaw0:.2}
};

function Scene(svg,cfg){
  this.svg=svg;this.cfg=cfg;this.uy=0;this.up=0;this.hy=0;this.hp=0;this.thy=0;this.thp=0;this.nd=-1;
  this.cx=+(svg.dataset.cx||cfg.cx||200);this.cy=+(svg.dataset.cy||cfg.cy||182);this.pitch=+(svg.dataset.pitch||.3);this.k=+(svg.dataset.scale||cfg.k||1.3);
  this.defs=document.createElementNS(NS,'defs');svg.insertBefore(this.defs,svg.firstChild);
  this.g=document.createElementNS(NS,'g');svg.appendChild(this.g);
  /* la zone interactive : la carte entière si la scène est dans une carte, sinon le SVG */
  const zone=svg.closest('[data-3d-zone]')||svg;
  let drag=null;this.moved=false;
  zone.style.touchAction='pan-y';
  zone.addEventListener('pointerdown',e=>{drag={x:e.clientX,y:e.clientY,uy:this.uy,up:this.up};this.moved=false;});
  window.addEventListener('pointerup',()=>{drag=null;});
  zone.addEventListener('pointermove',e=>{
    const r=zone.getBoundingClientRect();
    if(drag&&e.pointerType!=='touch'||drag&&e.buttons){const dx=e.clientX-drag.x,dy=e.clientY-drag.y;if(Math.abs(dx)+Math.abs(dy)>6)this.moved=true;
      if(this.moved){this.uy=drag.uy+dx*.012;this.up=Math.max(-.3,Math.min(.45,drag.up+dy*.006));}}
    else{this.thy=((e.clientX-r.left)/r.width-.5)*.8;this.thp=((e.clientY-r.top)/r.height-.5)*.3;}
  });
  zone.addEventListener('pointerleave',()=>{this.thy=0;this.thp=0;drag=null;});
  zone.addEventListener('click',e=>{if(this.moved){e.stopPropagation();e.preventDefault();this.moved=false;}},true);
}
Scene.prototype.frame=function(t){
  const c=this.cfg;
  this.hy+=(this.thy-this.hy)*.08;this.hp+=(this.thp-this.hp)*.08;
  const yaw=(RM?0:c.auto(t))+this.uy+this.hy+(c.yaw0||0), pit=this.pitch+this.up+this.hp;
  const C={cy:Math.cos(yaw),sy:Math.sin(yaw),cp:Math.cos(pit),sp:Math.sin(pit),x:this.cx,y:this.cy,k:this.k};
  const prims=c.dyn(RM?0:t);
  const items=[];
  for(const pr of prims){
    const V=pr.t==='bub'?[[pr.p[0][0],pr.p[0][1],pr.p[0][2]],rot(pr.p[1],C)]:pr.p.map(p=>rot(p,C));
    let d=0;for(const v of V)d+=v[2];d/=V.length;d+=(pr.b||0);
    let k=1;
    if(pr.n){const n=rot(pr.n,C),cx=V.reduce((s,v)=>s+v[0],0)/V.length,cy=V.reduce((s,v)=>s+v[1],0)/V.length,cz=V.reduce((s,v)=>s+v[2],0)/V.length;
      if(n[0]*(0-cx)+n[1]*(0-cy)+n[2]*(D-cz)<=0)continue;
      k=Math.max(0,n[0]*L[0]+n[1]*L[1]+n[2]*L[2]);}
    items.push({pr,V,d,k});
  }
  items.sort((a,b)=>a.d-b.d);
  let o='';
  for(const it of items){
    const pr=it.pr,P=it.V.map(v=>proj(v,C));
    if(pr.t==='f'){
      const fill=mix([8,10,18],pr.col,.42+.58*it.k);
      o+=`<polygon points="${pts(P)}" fill="${fill}"${pr.alpha<1?` fill-opacity="${f1(pr.alpha)}"`:''} stroke="${fill}" stroke-width=".4" stroke-linejoin="round"/>`;
    }else if(pr.t==='poly'){
      o+=`<polygon points="${pts(P)}" fill="${pr.fill}"${pr.op!=null?` opacity="${pr.op}"`:''}${pr.s?` stroke="${pr.s}" stroke-opacity="${pr.so||1}"`:''}/>`;
    }else if(pr.t==='l'){
      const s=P[0][2];
      o+=`<polyline points="${pts(P)}" fill="none" stroke="${pr.s}" stroke-opacity="${pr.o==null?1:f1(pr.o*100)/100}" stroke-width="${f1((pr.w||1)*s*100)/100}" stroke-linecap="round" stroke-linejoin="round"${pr.da?` stroke-dasharray="${pr.da}"`:''}/>`;
    }else if(pr.t==='b'){
      const p=P[0],r=f1(pr.r*p[2]);
      o+=`<circle cx="${f1(p[0])}" cy="${f1(p[1])}" r="${r}" fill="${pr.fill}"${pr.s?` stroke="${pr.s}" stroke-width="${pr.sw||1.5}"`:''}${pr.op!=null?` opacity="${f1(pr.op*100)/100}"`:''}${pr.fl?` filter="url(#${pr.fl})"`:''}/>`;
    }else if(pr.t==='cap'){
      const s=(P[0][2]+P[1][2])/2,ln=pts(P);
      o+=`<polyline points="${ln}" stroke="${pr.c1}" stroke-width="${f1(pr.r*2*s)}" stroke-linecap="round" fill="none"/><polyline points="${ln}" stroke="${pr.c2}" stroke-width="${f1(pr.r*1.2*s)}" stroke-linecap="round" fill="none" opacity="${pr.o2||.6}" transform="translate(${f1(-pr.r*.25*s)} ${f1(-pr.r*.3*s)})"/>`;
    }else if(pr.t==='tx'){
      const p=P[0];
      o+=`<text x="${f1(p[0])}" y="${f1(p[1])}" font-size="${f1(pr.fs*p[2])}" fill="${pr.fill}" text-anchor="middle" font-family="${pr.ff||'Inter,Arial,sans-serif'}"${pr.fw?` font-weight="${pr.fw}"`:''}${pr.op!=null?` opacity="${f1(pr.op*100)/100}"`:''} style="paint-order:stroke" stroke="#050d22" stroke-width="3" stroke-opacity=".6">${pr.s}</text>`;
    }else if(pr.t==='bub'){
      /* bulle de BD : centre fixe à l'écran (x,y relatifs au centre), pointe vers un point 3D */
      const cx=this.cx+pr.p[0][0]*this.k,cy=this.cy-pr.p[0][1]*this.k,tp=P[1],fs=pr.fs,w=pr.s.length*fs*.6+20,h=fs+12;
      const bx=Math.max(4,Math.min(396-w,cx-w/2)),by=cy-h/2,mx=Math.max(bx+12,Math.min(bx+w-12,tp[0]));
      const tipY=tp[1]-6,base=tipY>cy?by+h:by;
      o+=`<g${pr.op!=null?` opacity="${f1(pr.op*100)/100}"`:''}><path d="M${f1(mx-6)},${f1(base)} L${f1(tp[0])},${f1(tipY)} L${f1(mx+6)},${f1(base)}" fill="#0b1630" stroke="${pr.col}" stroke-width="1.3" stroke-linejoin="round"/>`+
        `<rect x="${f1(bx)}" y="${f1(by)}" width="${f1(w)}" height="${h}" rx="${h/2}" fill="#0b1630" fill-opacity=".92" stroke="${pr.col}" stroke-width="1.3"/>`+
        `<rect x="${f1(mx-5)}" y="${f1(base-1.5)}" width="10" height="3" fill="#0b1630"/>`+
        `<text x="${f1(bx+w/2)}" y="${f1(by+h/2+fs*.36)}" font-size="${fs}" font-weight="600" fill="#fff4dc" text-anchor="middle" font-family="Inter,Arial,sans-serif">${pr.s}</text></g>`;
    }
  }
  const nk=Object.keys(GR).length;
  if(nk!==this.nd){this.nd=nk;const col=c.col;
    this.defs.innerHTML=gradDefs()+`<radialGradient id="c3f${col.slice(1)}"><stop offset="0" stop-color="${col}" stop-opacity=".32"/><stop offset="1" stop-color="${col}" stop-opacity=".02"/></radialGradient>`+
      `<filter id="c3glow" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="2.5" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>`;}
  this.g.innerHTML=o;
};

const scenes=[];
document.querySelectorAll('svg[data-3d]').forEach(svg=>{const k=svg.getAttribute('data-3d');if(CFG[k])scenes.push(new Scene(svg,CFG[k]));});
const t0=performance.now();let vis=true;
document.addEventListener('visibilitychange',()=>{vis=!document.hidden;});
function loop(now){if(vis){const t=Math.max(0,(now-t0)/1000);for(const s of scenes){const r=s.svg.getBoundingClientRect();if(r.bottom>0&&r.top<innerHeight)s.frame(t);}}if(!RM)requestAnimationFrame(loop);}
scenes.forEach(s=>s.frame(0));requestAnimationFrame(loop);
})();
