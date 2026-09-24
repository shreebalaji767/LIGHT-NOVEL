import random

WORLDS = [
    ("The Republic of Unnecessary Kingdoms", "Every spell requires a registered purpose.", "The borders move whenever someone files the correct form."),
    ("The Continent of Borrowed Tomorrows", "Time can be borrowed, but the interest is paid in memories.", "Yesterday is legally considered an import."),
    ("The Seven Provinces of Specific Laws", "Magic obeys written clauses more strongly than spoken commands.", "Every province has a different definition of what counts as a dragon."),
    ("The Moonlit Federation of Mostly Normal People", "Moonlight reveals hidden contracts and temporary enchantments.", "The capital holds elections for positions nobody remembers creating."),
    ("The Kingdom Beneath the Extremely Large Hat", "Authority increases according to the size of one's ceremonial hat.", "The national treasure is a perfectly ordinary spoon."),
    ("The Inland Sea of Forty-Nine Mayors", "A promise spoken beside water becomes magically enforceable.", "Forty-nine towns insist they are the capital."),
    ("The Empire of Mildly Forbidden Things", "Anything described as forbidden becomes harder to destroy.", "The royal vault contains a door labeled 'probably nothing'."),
    ("The Archipelago of Suspiciously Convenient Prophecies", "Prophecies become stronger when people misunderstand them.", "Every prophecy has at least one typo."),
]

def make_world(r):
    name, rule, oddity = r.choice(WORLDS)
    magic = r.choice([
        "Contract magic turns promises, receipts, and signatures into real spells.",
        "Ranked magic is measured by how loudly reality notices you.",
        "People cast spells by declaring extremely specific exceptions to ordinary physics.",
        "Magic is powered by unresolved problems; solving one can actually make you weaker.",
        "The oldest spells are bureaucratic procedures nobody remembers inventing.",
    ])
    threat = r.choice([
        "an ancient prophecy that keeps changing its punctuation",
        "a Demon King whose greatest weapon is administrative patience",
        "a dungeon that has learned to negotiate its own rent",
        "a missing royal relic that insists it was never missing",
        "a celestial committee preparing an audit of mortal civilization",
    ])
    return {"name": name, "rule": rule, "oddity": oddity, "magic": magic, "threat": threat}
