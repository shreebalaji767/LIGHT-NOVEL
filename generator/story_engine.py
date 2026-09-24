import random
from world_engine import make_world
from character_engine import make_characters
from chapter_engine import Engine, ARCS

PREMISES=[
    "A failed office worker is reincarnated as a royal treasurer in a kingdom whose economy is governed by absurd laws.",
    "A supposedly legendary hero discovers that the kingdom's greatest threat is an administrative error with a sword.",
    "A village baker becomes responsible for an ancient prophecy because the prophecy was printed on the wrong receipt.",
    "A part-time villain accepts a mysterious job and discovers that the job is to manage the hero's retirement fund.",
    "A dungeon manager tries to reduce adventurer complaints while an ancient evil keeps filing maintenance requests.",
    "A royal archivist investigates a missing historical document and discovers that history itself has misplaced several chapters.",
    "A reincarnated clerk receives an overpowered skill whose only ability is finding contradictions in official paperwork.",
    "A retired assassin tries to run a quiet shop until every customer turns out to be connected to a world-ending prophecy.",
    "A minor noble inherits a useless title and discovers that the title is legally recognized as a weapon of mass inconvenience.",
    "A monster accountant is ordered to audit the Demon King's empire and accidentally becomes the most important person in the war.",
]
GENRES=[
    ["Comedy","Fantasy","Isekai","Adventure"], ["Parody","Fantasy","Mystery","Comedy"],
    ["Comedy","Fantasy","Dungeon","Adventure"], ["Parody","Fantasy","Politics","Mystery"],
    ["Comedy","Romance","Fantasy","Adventure"],
]
NOTES=[
    "The original outline had twelve chapters. Then somebody discovered a receipt.",
    "I intended to write a dignified fantasy epic. The characters disagreed.",
    "Every coincidence is intentional. Every typo is probably a prophecy.",
    "Please remember that the bureaucracy is fictional. The paperwork is not.",
    "The worldbuilding is extremely serious. The author is not.",
]

def make(seed, chapters=520):
    r=random.Random(seed)
    world=make_world(r)
    chars=make_characters(r,20)
    premise=r.choice(PREMISES)
    protagonist=chars[0]
    title=f"{r.choice(['I Was Reincarnated as','Apparently I Am Now','Nobody Told Me That','I Accidentally Became','My New Life Began With'])} {r.choice(['the kingdom’s least qualified problem solver','a government employee with a suspicious sword','the person responsible for an impossible prophecy','the world’s most unnecessary hero','the clerk assigned to the Demon King'])} {r.choice(['and Everything Went Wrong','and the Demon King Sent Me an Invoice','in a World Where Paperwork Is Magic','and Now Everyone Thinks I Am Important','but the World Has Other Plans'])}"
    synopsis=(f"{premise} The story unfolds in {world['name']}, where {world['rule'].lower()} "
              f"The central problem is {world['threat']}. {protagonist['name']} wants to {protagonist['goal']}, "
              "but every reasonable solution creates a new unreasonable obligation.")
    engine=Engine(r,chars,world)
    chapters_data=engine.generate(chapters)
    factions=[
        "Royal Administration","Adventurer Guild","Independent Merchants","Provincial Court",
        "The Unofficial Committee","Demon King's Office","Traveling Scholars","Dungeon Residents"
    ]
    locations=sorted({c["location"] for c in chapters_data})
    return {
        "id":f"novel-{seed:06d}","title":title,"synopsis":synopsis,"premise":premise,
        "genre":r.choice(GENRES),"authorNotes":r.choice(NOTES),"chapterCount":chapters,
        "world":world,"characters":chars,"factions":factions,"locations":locations,
        "storyArcs":[{"number":i+1,"title":a} for i,a in enumerate(ARCS)],
        "chapters":chapters_data
    }
