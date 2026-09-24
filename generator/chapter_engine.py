import random

ARCS = [
    "The Problem With The Original Plan", "The Guild Has Lost Its Paperwork", "A Prophecy Nobody Asked For",
    "The Tournament That Should Have Been An Email", "The Villain's Administrative Crisis", "The City That Moved Overnight",
    "The Completely Avoidable War", "The Mystery of the Missing Object", "The Arc Where Everyone Needs A Receipt",
    "The Royal Family Has Questions", "The Dungeon Files A Complaint", "The Consequences Become Consequences",
    "The Great Misunderstanding", "The Secret That Was Not Very Secret", "The Final Exam That Is Somehow Political",
    "The Road That Refused To Be Mapped", "The Hero's Retirement Problem", "The Demon King's Customer Service Department",
    "The Festival With An Emergency Clause", "The Last Normal Tuesday",
]
EVENTS = [
    ("discovery", "a sealed document appears in the wrong person's hands"),
    ("conflict", "two factions interpret the same sentence in completely different ways"),
    ("errand", "a simple delivery becomes evidence in a much larger dispute"),
    ("investigation", "an ordinary object is connected to three unrelated incidents"),
    ("social", "a public misunderstanding becomes impossible to correct without admitting something worse"),
    ("magic", "a spell works exactly as written and therefore causes a ridiculous problem"),
    ("travel", "the road changes its destination while everyone is still walking on it"),
    ("battle", "a confrontation begins, but both sides discover they have the wrong target"),
    ("reversal", "a previous solution creates a new obligation"),
    ("revelation", "someone admits that they knew more than they claimed"),
    ("quiet", "nothing attacks anyone, which makes the characters more nervous than usual"),
    ("absurd", "a completely irrelevant item becomes the legal key to the crisis"),
]
LOCATIONS = [
    "the capital registry", "the adventurer guild", "the royal kitchen", "the eastern market", "the old dungeon",
    "the ministry basement", "Bellweather village", "the royal archives", "the suspicious bridge", "the provincial courthouse",
    "the moonlit station", "the abandoned academy", "the treaty garden", "the border checkpoint", "the prophecy museum",
    "the floating warehouse", "the underground bakery", "the mayoral tower", "the forbidden library", "the road that moved",
]
OBJECTS = ["receipt", "potato", "hat", "sword", "invoice", "permit", "teapot", "map", "bell", "key", "rubber stamp", "cake", "umbrella", "coin", "book"]

class Engine:
    def __init__(self, r, chars, world):
        self.r=r; self.chars=chars; self.world=world
        self.used_titles=set(); self.used_combos=set(); self.recent_phrases=[]
        self.threads=[
            "the missing royal relic", "the contradictory prophecy", "the unexplained border change",
            "the anonymous letter writer", "the dungeon's legal claim", "the suspicious invoice",
            "the identity of the person who altered history"
        ]
        self.state={c["id"]:{"trust":0,"location":"the capital registry","knowledge":[]} for c in chars}
        self.chapter_count=0

    def _pick_pov(self, n):
        if n == 1: return self.chars[0]
        candidates=self.chars[:]
        # Rotate perspective so the same character is never used twice in a row.
        prev=getattr(self,"last_pov",-1)
        candidates=[c for c in candidates if c["id"]!=prev] or candidates
        c=self.r.choice(candidates)
        self.last_pov=c["id"]
        return c

    def _title(self, n, pov, event):
        prefixes=["I Was Supposed To", "Nobody Prepared Me For", "Today We Accidentally", "The Day", "I Regret Discovering", "Apparently We Now Have To", "My Completely Reasonable Plan To", "The Extremely Bad Idea Called"]
        nouns=["the Missing Receipt", "a Second Demon King", "the Illegal Sandwich", "the Moving Road", "the Royal Mistake", "the Prophecy Problem", "the Dungeon Audit", "the World's Least Useful Sword", "the Emergency Meeting", "the Extremely Suspicious Cake"]
        for _ in range(200):
            t=f"{rchoice(self.r,prefixes)} {rchoice(self.r,nouns)} — {pov['name']} POV"
            if t not in self.used_titles:
                self.used_titles.add(t); return t
        return f"Chapter {n}: {event[0].title()}"

    def _voice(self,p):
        return {
            "dry": [f"{p['name']} regarded the situation with the professional disappointment of someone who had already predicted it.", "This was technically progress. Unfortunately, it was progress in the wrong direction."],
            "observational": [f"{p['name']} noticed three details before anyone else noticed the first one.", "The room looked ordinary until the small things started disagreeing with one another."],
            "anxious": [f"{p['name']} immediately identified seven ways this could become worse.", "The eighth way arrived before they finished counting."],
            "dramatic": [f"{p['name']} knew, with the terrible certainty reserved for prophecies and overdue bills, that this moment mattered.", "Somewhere, history was preparing to make a poor decision."],
            "deadpan": [f"{p['name']} had seen stranger things. None of them had been this inconvenient.", "There was no screaming yet, which was considered encouraging."],
            "earnest": [f"{p['name']} wanted to believe there was a simple answer.", "For approximately twelve seconds, that belief survived."],
            "sarcastic": [f"Naturally, {p['name']} thought, because ordinary solutions were apparently illegal now.", "The universe had once again mistaken inconvenience for character development."],
            "formal": [f"{p['name']} recorded the incident as objectively as circumstances permitted.", "The official version would later contain considerably fewer mistakes than the actual version."],
        }[p["voice"]]

    def chapter(self,n):
        arc=ARCS[((n-1)//26)%len(ARCS)]
        p=self._pick_pov(n)
        kind,event=self.r.choice(EVENTS)
        loc=self.r.choice(LOCATIONS)
        obj=self.r.choice(OBJECTS)
        thread=self.r.choice(self.threads)
        combo=(arc,kind,loc,obj,p["id"])
        tries=0
        while combo in self.used_combos and tries<30:
            kind,event=self.r.choice(EVENTS); loc=self.r.choice(LOCATIONS); obj=self.r.choice(OBJECTS); thread=self.r.choice(self.threads)
            combo=(arc,kind,loc,obj,p["id"]); tries+=1
        self.used_combos.add(combo)
        self.state[p["id"]]["location"]=loc
        if n>1:
            p["knowledge"].append(f"chapter {n}: {thread}")
        if n%17==0 and len(self.threads)>2:
            resolved=self.threads.pop(0)
            new=f"the consequence of resolving {resolved}"
            self.threads.append(new)
            resolution=f"The immediate problem involving {resolved} was settled, but the solution created {new}."
        else:
            resolution=f"The mystery remained open, although {p['name']} now had one useful fact: someone was treating {thread} as if it were a normal administrative matter."
        voice=self._voice(p)
        paragraphs=[
            f"CHAPTER {n} — {p['name']} POV",
            f"{arc} had already produced two meetings, one argument, and a document nobody could legally throw away.",
            f"{p['name']} arrived at {loc} intending to {p['goal']}. The plan lasted until the first unexpected detail appeared.",
            event.capitalize() + ".",
            voice[0],
            f"The important object was a {obj}. It was not magical in the usual sense, which made it considerably more suspicious.",
            f"{p['name']} checked the obvious explanation first. It was wrong. They checked the ridiculous explanation next. It was unfortunately closer.",
            f"The world of {self.world['name']} followed one inconvenient rule: {self.world['rule']}",
            voice[1],
            f"A second person arrived carrying information about {thread}. Their explanation contradicted the first explanation in exactly the way a useful clue should.",
            f"Nobody agreed on what to do with the {obj}. One person wanted to destroy it. Another wanted to file it. {p['name']} wanted to know why it had appeared here.",
            f"That question led to a small discovery: {p['secret']}",
            resolution,
            f"Before leaving, {p['name']} made a decision that would matter later: they would not trust the next official document until they had read the footnotes.",
            "For the first time that day, everyone agreed on something. This was probably going to get worse.",
        ]
        # Add an event-specific beat to avoid fixed chapter shapes.
        if kind=="battle": paragraphs.insert(8,f"The confrontation stopped when both sides realized their weapons had been issued under different legal definitions of 'weapon.'")
        elif kind=="quiet": paragraphs.insert(8,"Nothing happened for several minutes. The silence became so suspicious that somebody checked the ceiling.")
        elif kind=="travel": paragraphs.insert(8,"The road bent left, reconsidered, and politely delivered them somewhere else.")
        elif kind=="social": paragraphs.insert(8,"The audience applauded for reasons that nobody present could later explain.")
        elif kind=="magic": paragraphs.insert(8,f"The spell produced exactly the requested result, including the clause everyone had assumed was decorative.")
        elif kind=="absurd": paragraphs.insert(8,f"The irrelevant {obj} became relevant when an old law was quoted from memory and turned out to be correct.")
        else: paragraphs.insert(8,"The conversation became quieter when everyone realized that the newest clue had a date older than the kingdom itself.")
        self.chapter_count=n
        return {
            "number":n,"title":self._title(n,p,(kind,event)),"arcTitle":arc,"location":loc,
            "pov":{"id":p["id"],"name":p["name"],"role":p["role"],"voice":p["voice"]},
            "eventType":kind,"paragraphs":paragraphs,
            "state":{"openThreads":len(self.threads),"povKnowledge":len(p["knowledge"]),"chapter":n}
        }

    def generate(self,count=520):
        return [self.chapter(n) for n in range(1,count+1)]

def rchoice(r, values):
    return values[r.randrange(len(values))]
