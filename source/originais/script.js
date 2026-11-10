const checkoutLinks = {
 Essencial: 'https://pay.cakto.com.br/tghh3wc_1304857',
 Premium: 'https://pay.cakto.com.br/iamnr2b'
};
const checkout = document.querySelector('#checkout');
const preview = document.querySelector('#preview');
document.querySelectorAll('[data-plan]').forEach(button => button.addEventListener('click', () => {
 const plan = button.dataset.plan;
 if (checkoutLinks[plan]) { window.location.assign(checkoutLinks[plan]); return; }
 document.querySelector('#chosen-plan').textContent = plan === 'Premium' ? 'o Kit Salão Premium.' : 'o Catálogo Essencial.';
 checkout.showModal();
}));
document.querySelectorAll('dialog').forEach(dialog => {
 dialog.querySelector('.close').addEventListener('click', () => dialog.close());
 dialog.addEventListener('click', e => { if(e.target!==dialog)return; const r=dialog.getBoundingClientRect(); if(e.clientX<r.left||e.clientX>r.right||e.clientY<r.top||e.clientY>r.bottom)dialog.close(); });
});
document.querySelector('.dismiss').addEventListener('click',()=>checkout.close());
const carousel=document.querySelector('.carousel');
const originals=[...carousel.querySelectorAll('[data-page]')];
originals.forEach(el=>{const c=el.cloneNode(true);c.setAttribute('aria-hidden','true');c.tabIndex=-1;c.removeAttribute('data-page');c.classList.add('carousel-copy');carousel.append(c);});
carousel.addEventListener('click',e=>{
 const card=e.target.closest('.actual-page');if(!card)return;
 const img=card.querySelector('img');const large=img.cloneNode();large.loading='eager';
 document.querySelector('#preview-content').replaceChildren(large);preview.showModal();
});
const reduced=window.matchMedia('(prefers-reduced-motion: reduce)');
let running=!reduced.matches,hover=false,focused=false,visible=false,pausedUntil=0,position=0,last=0,frame=0;
const control=document.querySelector('#autoplay');
function updateControl(){control.textContent=running?'Pausar':'Reproduzir';control.setAttribute('aria-label',running?'Pausar carrossel':'Reproduzir carrossel');control.setAttribute('aria-pressed',String(!running));}
updateControl();
control.addEventListener('click',()=>{running=!running;updateControl();});
reduced.addEventListener('change',()=>{running=!reduced.matches;updateControl();});
carousel.addEventListener('pointerenter',()=>hover=true);
carousel.addEventListener('pointerleave',()=>hover=false);
carousel.addEventListener('focusin',()=>focused=true);
carousel.addEventListener('focusout',e=>{focused=carousel.contains(e.relatedTarget);});
carousel.addEventListener('pointerdown',()=>pausedUntil=performance.now()+6500);
carousel.addEventListener('wheel',()=>pausedUntil=performance.now()+6500,{passive:true});
carousel.addEventListener('scroll',()=>{if(performance.now()<pausedUntil||hover||focused)position=carousel.scrollLeft;},{passive:true});
const observer=new IntersectionObserver(entries=>{visible=entries[0].isIntersecting;},{threshold:0.05});observer.observe(carousel);
function move(direction){pausedUntil=performance.now()+6000;const step=originals[0].offsetWidth+parseFloat(getComputedStyle(carousel).gap);carousel.scrollBy({left:direction*step,behavior:reduced.matches?'instant':'smooth'});}
document.querySelector('#prev').addEventListener('click',()=>move(-1));
document.querySelector('#next').addEventListener('click',()=>move(1));
function tick(now){const delta=last?Math.min(now-last,60):0;last=now;const loop=carousel.children[originals.length].offsetLeft-carousel.children[0].offsetLeft;
 if(running&&visible&&!hover&&!focused&&!preview.open&&!checkout.open&&!document.hidden&&now>pausedUntil&&loop>0){position+=delta*.035;if(position>=loop)position-=loop;carousel.scrollLeft=position;}else position=carousel.scrollLeft;
 frame=requestAnimationFrame(tick);
}
frame=requestAnimationFrame(tick);
window.addEventListener('pagehide',()=>{cancelAnimationFrame(frame);observer.disconnect();},{once:true});
