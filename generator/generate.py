import json
from pathlib import Path
from story_engine import make

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"novels"
SEEDS=[104729,209759,324161,433963,524287,655373,777221,888227]
CHAPTERS=520

OUT.mkdir(exist_ok=True)
for old in OUT.glob("novel-*.json"):
    old.unlink()

manifest=[]
for seed in SEEDS:
    novel=make(seed,CHAPTERS)
    path=OUT/f"{novel['id']}.json"
    path.write_text(json.dumps(novel,ensure_ascii=False,separators=(",",":")),encoding="utf-8")
    manifest.append({"file":path.name,"id":novel["id"],"title":novel["title"],"chapters":novel["chapterCount"]})

(OUT/"manifest.json").write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding="utf-8")
print(f"Generated {len(manifest)} complete novels with {CHAPTERS} chapters each.")
