import random

FIRST = ["Ari", "Mira", "Ren", "Sora", "Nell", "Kian", "Lio", "Vera", "Toma", "Yuna", "Bram", "Iris", "Noa", "Cato", "Eli", "Rhea", "Milo", "Aya", "Finn", "Nika", "Juno", "Pax", "Rin", "Theo"]
LAST = ["Bell", "Voss", "Quill", "Morrow", "Vale", "Pike", "Dane", "Wren", "Ash", "Locke", "Merrin", "Crow", "North", "Fable", "Stone", "Kestrel"]
ROLES = [
    ("Reincarnated Clerk", "collect evidence before anyone notices the plot", "being blamed for a system they did not design"),
    ("Disgraced Hero", "prove that heroism is not a job title", "being remembered for the wrong victory"),
    ("Royal Archivist", "find the missing page that keeps history coherent", "knowing one fact that should not exist"),
    ("Part-Time Villain", "complete one honest villainous task and go home", "having a heroic reputation in another country"),
    ("Guild Receptionist", "make the adventurer queue obey basic mathematics", "the guild founder left them a secret emergency authority"),
    ("Wandering Baker", "deliver a cake before it becomes a diplomatic incident", "their recipes accidentally contain spell formulas"),
    ("Dungeon Manager", "keep monsters employed and adventurers alive", "the dungeon considers them its legal owner"),
    ("Royal Knight", "protect the person they were ordered to arrest", "their oath has a hidden second sentence"),
    ("Village Mayor", "stop the village from becoming an empire", "the village sits on something ancient"),
    ("Cursed Scholar", "translate a book that argues back", "their curse is actually a warning"),
    ("Traveling Merchant", "sell one harmless item for a reasonable price", "they can identify counterfeit prophecies"),
    ("Monster Accountant", "make the dungeon's finances balance", "numbers reveal monsters' emotions"),
    ("Prophecy Translator", "discover what the prophecy meant before the king acts", "the prophecy was written by someone they know"),
    ("Retired Assassin", "live quietly and never accept another contract", "their old clients keep becoming heroes"),
    ("Apprentice Mage", "learn one useful spell without causing an international incident", "their magic reacts to lies"),
    ("Minor Noble", "avoid inheriting a useless title", "their family owns a key to something impossible"),
    ("Demon Clerk", "process mortal paperwork without invading anything", "the Demon King trusts them too much"),
    ("Traveling Doctor", "keep everyone alive long enough to argue", "they recognize a disease nobody has named"),
    ("Street Performer", "earn enough money for dinner", "their audience sometimes includes ghosts"),
    ("Cartographer", "map a road that changes every night", "the map redraws itself around secrets"),
]
TRAITS = [
    "overly literal", "quietly competitive", "optimistic at the worst times", "professionally suspicious", "dramatic about paperwork", "calm until somebody lies", "unable to resist a mystery", "terrible at pretending not to care", "practical to an unreasonable degree", "convinced every problem has a receipt"
]

def make_characters(r, n=20):
    chars=[]
    used_names=set()
    for i in range(n):
        role, goal, fear = ROLES[i % len(ROLES)]
        while True:
            name=f"{r.choice(FIRST)} {r.choice(LAST)}"
            if name not in used_names:
                used_names.add(name); break
        chars.append({
            "id": i,
            "name": name,
            "role": role,
            "goal": goal,
            "fear": fear,
            "trait": r.choice(TRAITS),
            "voice": r.choice(["dry", "observational", "anxious", "dramatic", "deadpan", "earnest", "sarcastic", "formal"]),
            "secret": f"{name} has a private connection to {r.choice(['the royal archives','the oldest dungeon','the missing relic','the prophecy','the border dispute'])}.",
            "knowledge": [],
        })
    return chars
