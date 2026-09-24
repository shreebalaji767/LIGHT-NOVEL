const qs=new URLSearchParams(location.search);
const novelId=qs.get('novel');
let chapter=Math.max(1,Number(qs.get('chapter')||1));
let novel=null;
const $=id=>document.getElementById(id);
const esc=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
async function init(){
  if(!novelId) return location.href='index.html';
  const manifest=await fetch('novels/manifest.json').then(r=>r.json());
  const item=manifest.find(x=>x.id===novelId);
  if(!item) return location.href='index.html';
  novel=await fetch('novels/'+item.file).then(r=>r.json());
  chapter=Math.min(chapter,novel.chapters.length); render();
}
function render(){
  const c=novel.chapters[chapter-1];
  document.title=`${c.title} — LIGHTNOVEL.EXE`;
  $('novelTitle').textContent=novel.title;
  $('world').textContent=novel.world.name;
  $('worldSummary').textContent=novel.world.rule;
  $('pov').textContent=`${c.pov.name} • ${c.pov.voice.toUpperCase()} POV`;
  $('role').textContent=c.pov.role;
  $('status').textContent=`${c.state.openThreads} open story threads • event: ${c.eventType}`;
  $('counter').textContent=`CHAPTER ${chapter} / ${novel.chapters.length}`;
  $('meta').textContent=`${c.arcTitle}  •  ${c.location}  •  ${c.eventType.toUpperCase()}`;
  $('chapterTitle').textContent=c.title;
  $('text').innerHTML=c.paragraphs.filter((p,i)=>i!==0).map(p=>p==='◆'?'<hr>':`<p>${esc(p)}</p>`).join('');
  $('prev').disabled=chapter<=1; $('next').disabled=chapter>=novel.chapters.length;
  $('prev').onclick=()=>go(-1); $('next').onclick=()=>go(1);
}
function go(delta){chapter=Math.max(1,Math.min(novel.chapters.length,chapter+delta));history.replaceState({},'',`reader.html?novel=${encodeURIComponent(novel.id)}&chapter=${chapter}`);window.scrollTo({top:0,behavior:'smooth'});render()}
document.addEventListener('keydown',e=>{if(e.key==='ArrowLeft')go(-1);if(e.key==='ArrowRight')go(1)});
init().catch(console.error);
