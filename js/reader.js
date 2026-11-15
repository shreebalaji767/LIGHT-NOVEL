const qs=new URLSearchParams(location.search);
const novelId=qs.get('novel');
let chapter=Math.max(1,Number(qs.get('chapter')||1));
let novel=null;
const $=id=>document.getElementById(id);
const esc=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const readStore=(key,fallback)=>{try{return JSON.parse(localStorage.getItem('ln:'+key))??fallback}catch{return fallback}};
const writeStore=(key,value)=>{try{localStorage.setItem('ln:'+key,JSON.stringify(value))}catch(e){console.warn('Local reading data could not be saved',e)}};
function saveProgress(){const progress=readStore('progress',{});progress[novel.id]={chapter,updated:Date.now()};writeStore('progress',progress)}
function isBookmarked(){return readStore('bookmarks',[]).some(x=>x.novel===novel.id&&x.chapter===chapter)}
function syncBookmark(){const b=$('bookmark');if(!b)return;b.setAttribute('aria-pressed',String(isBookmarked()));b.textContent=isBookmarked()?'♥ Saved':'♡ Save chapter'}
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
  document.title=`${c.title} — ${novel.title}`;
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
  $('readingProgress').style.width=(chapter/novel.chapters.length*100)+'%';
  $('readingProgress').setAttribute('aria-valuenow',String(Math.round(chapter/novel.chapters.length*100)));
  saveProgress();syncBookmark();
}
function go(delta){chapter=Math.max(1,Math.min(novel.chapters.length,chapter+delta));history.replaceState({},'',`reader.html?novel=${encodeURIComponent(novel.id)}&chapter=${chapter}`);window.scrollTo({top:0,behavior:'smooth'});render()}
document.addEventListener('keydown',e=>{if(e.key==='ArrowLeft')go(-1);if(e.key==='ArrowRight')go(1)});
$('bookmark').addEventListener('click',()=>{const b=readStore('bookmarks',[]),i=b.findIndex(x=>x.novel===novel.id&&x.chapter===chapter);if(i>=0)b.splice(i,1);else b.push({novel:novel.id,chapter,title:novel.chapters[chapter-1].title,updated:Date.now()});writeStore('bookmarks',b);syncBookmark()});
$('fontDown').addEventListener('click',()=>{const n=Math.max(15,Number(getComputedStyle(document.documentElement).getPropertyValue('--reader-font').replace('px',''))-1||18);document.documentElement.style.setProperty('--reader-font',n+'px');localStorage.setItem('ln:font',n)});
$('fontUp').addEventListener('click',()=>{const n=Math.min(28,(Number(localStorage.getItem('ln:font'))||18)+1);document.documentElement.style.setProperty('--reader-font',n+'px');localStorage.setItem('ln:font',n)});
$('themeToggle').addEventListener('click',()=>{const next=document.body.dataset.theme==='paper'?'dark':'paper';document.body.dataset.theme=next;localStorage.setItem('ln:readerTheme',next)});
const savedFont=Number(localStorage.getItem('ln:font'));if(savedFont)document.documentElement.style.setProperty('--reader-font',Math.min(28,Math.max(15,savedFont))+'px');
document.body.dataset.theme=localStorage.getItem('ln:readerTheme')||'dark';
init().catch(e=>{console.error(e);$('chapterTitle').textContent='Unable to load this chapter';$('text').textContent='Please check your connection and reload the page.'});
