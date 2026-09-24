const esc=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const grid=document.getElementById('grid');
const shuffle=document.getElementById('shuffle');
async function load(){
  const manifest=await fetch('novels/manifest.json').then(r=>r.json());
  const novels=await Promise.all(manifest.map(x=>fetch('novels/'+x.file).then(r=>r.json())));
  novels.forEach((n,i)=>{
    const card=document.createElement('article'); card.className='card';
    card.innerHTML=`<small>NOVEL ${String(i+1).padStart(3,'0')}</small><h2>${esc(n.title)}</h2><p>${esc(n.synopsis)}</p><div class="tags">${n.genre.map(g=>`<span>${esc(g)}</span>`).join('')}</div><footer><span>${n.chapters.length} CHAPTERS</span><button>READ</button></footer>`;
    card.querySelector('button').onclick=()=>location.href=`reader.html?novel=${encodeURIComponent(n.id)}&chapter=1`;
    grid.appendChild(card);
  });
  shuffle.onclick=()=>{const n=novels[Math.floor(Math.random()*novels.length)];location.href=`reader.html?novel=${encodeURIComponent(n.id)}&chapter=1`};
}
load().catch(e=>{grid.innerHTML='<p class="error">Library data could not be loaded. Deploy this folder on a static web host or use a local static server; browsers block fetch() from file:// pages.</p>';console.error(e)});
