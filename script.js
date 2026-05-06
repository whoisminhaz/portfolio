document.addEventListener('DOMContentLoaded',()=>{
// NAV
const nav=document.getElementById('navbar');
window.addEventListener('scroll',()=>nav.classList.toggle('scrolled',scrollY>60));
const tog=document.getElementById('nav-toggle'),links=document.getElementById('nav-links');
tog.addEventListener('click',()=>links.classList.toggle('active'));
links.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>links.classList.remove('active')));
document.querySelectorAll('a[href^="#"]').forEach(a=>{a.addEventListener('click',e=>{e.preventDefault();const t=document.querySelector(a.getAttribute('href'));if(t)t.scrollIntoView({behavior:'smooth'})})});

// PARTICLES
const c=document.getElementById('particles'),ctx=c.getContext('2d');
let W,H;function resize(){W=c.width=innerWidth;H=c.height=innerHeight}resize();
window.addEventListener('resize',resize);
const dots=Array.from({length:60},()=>({x:Math.random()*innerWidth,y:Math.random()*innerHeight,vx:(Math.random()-0.5)*0.4,vy:(Math.random()-0.5)*0.4,r:Math.random()*2+0.5}));
function drawParticles(){ctx.clearRect(0,0,W,H);dots.forEach(d=>{d.x+=d.vx;d.y+=d.vy;if(d.x<0||d.x>W)d.vx*=-1;if(d.y<0||d.y>H)d.vy*=-1;ctx.beginPath();ctx.arc(d.x,d.y,d.r,0,Math.PI*2);ctx.fillStyle='rgba(108,92,231,0.25)';ctx.fill()});
for(let i=0;i<dots.length;i++)for(let j=i+1;j<dots.length;j++){const dx=dots[i].x-dots[j].x,dy=dots[i].y-dots[j].y,dist=Math.sqrt(dx*dx+dy*dy);if(dist<120){ctx.beginPath();ctx.moveTo(dots[i].x,dots[i].y);ctx.lineTo(dots[j].x,dots[j].y);ctx.strokeStyle=`rgba(0,206,201,${0.08*(1-dist/120)})`;ctx.stroke()}}
requestAnimationFrame(drawParticles)}drawParticles();

// TYPING
const words=['measurable growth.','real impact.','winning results.','scalable ventures.','strategic value.'];
const el=document.getElementById('typed');let wi=0,ci=0,del=false;
function type(){if(!del){if(ci<words[wi].length){el.textContent+=words[wi][ci];ci++;setTimeout(type,80)}else{setTimeout(()=>{del=true;type()},2000)}}
else{if(ci>0){el.textContent=words[wi].substring(0,ci-1);ci--;setTimeout(type,40)}else{del=false;wi=(wi+1)%words.length;setTimeout(type,400)}}}type();

// COUNTERS
const counters=document.querySelectorAll('.stat-num');
const cObs=new IntersectionObserver(entries=>{entries.forEach(e=>{if(e.isIntersecting){const el=e.target,target=parseFloat(el.dataset.count),dec=el.dataset.decimal==='true';let cur=0;const step=target/40;const iv=setInterval(()=>{cur+=step;if(cur>=target){cur=target;clearInterval(iv)}el.textContent=dec?cur.toFixed(1):Math.round(cur)},30);cObs.unobserve(el)}})},{threshold:0.5});
counters.forEach(c=>cObs.observe(c));

// REVEAL
const reveals=document.querySelectorAll('.reveal');
const rObs=new IntersectionObserver(entries=>{entries.forEach(e=>{if(e.isIntersecting){e.target.classList.add('active');rObs.unobserve(e.target)}})},{threshold:0.1,rootMargin:'0px 0px -40px 0px'});
reveals.forEach(el=>rObs.observe(el));

// TILT
document.querySelectorAll('[data-tilt]').forEach(card=>{card.addEventListener('mousemove',e=>{const r=card.getBoundingClientRect(),x=(e.clientX-r.left)/r.width-0.5,y=(e.clientY-r.top)/r.height-0.5;card.style.transform=`perspective(600px) rotateY(${x*8}deg) rotateX(${-y*8}deg) translateY(-4px)`});
card.addEventListener('mouseleave',()=>{card.style.transform='perspective(600px) rotateY(0) rotateX(0) translateY(0)'})});
});

// CURSOR & GLOW
const cursorGlow = document.createElement('div');
cursorGlow.id = 'cursor-glow';
document.body.appendChild(cursorGlow);
window.addEventListener('mousemove', e => {
    cursorGlow.style.left = e.clientX + 'px';
    cursorGlow.style.top = e.clientY + 'px';
});
document.querySelectorAll('.glow-container').forEach(container => {
    container.addEventListener('mousemove', e => {
        container.querySelectorAll('.glow-card').forEach(card => {
            const rect = card.getBoundingClientRect();
            card.style.setProperty('--mouse-x', `${e.clientX - rect.left}px`);
            card.style.setProperty('--mouse-y', `${e.clientY - rect.top}px`);
        });
    });
});


