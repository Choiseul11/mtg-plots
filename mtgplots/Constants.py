'''
Card Data Constants
'''
COLORS = ['White', 'Blue', 'Black', 'Red', 'Green']
COLOR_MAP = {'White': 'W', 'Blue':'U', 'Black':'B', 'Red':'R', 'Green':'G'}
RARITIES = ['Common', 'Uncommon', 'Rare', 'Mythic Rare', 'Basic', 'Special']
COLORIDS = ['C', 'W', 'U', 'B', 'R', 'G', 
			'WU', 'WB', 'WR', 'WG', 'UB', 'UR', 'UG', 'BR', 'BG', 'RG', 
			'WUB', 'WUR', 'WUG', 'WBR', 'WBG', 'WRG', 'UBR', 'UBG', 'URG', 'BRG', 
			'WUBR', 'WUBG', 'WURG', 'WBRG', 'UBRG', 
			'WUBRG']

'''
Set Code Constants
'''
ALL_SETS = ['LEA', 'LEB', 'CED', 'CEI', '2ED', 'ARN', 'pDRC', 'ATQ', '3ED', 
			'LEG', 'DRK', 'FEM', 'pLGM', 'pMEI', '4ED', 'ICE', 'CHR', 'HML', 
			'ALL', 'RQS', 'pARL', 'pCEL', 'MIR', 'MGB', 'ITP', 'VIS', '5ED', 
			'VAN', 'POR', 'pPOD', 'WTH', 'pPRE', 'TMP', 'STH', 'PO2', 'pJGP', 
			'EXO', 'UGL', 'pALP', 'USG', 'ATH', 'ULG', '6ED', 'PTK', 'UDS', 
			'S99', 'pGRU', 'pWOR', 'pWOS', 'MMQ', 'BRB', 'pSUS', 'pFNM', 'pELP', 
			'NMS', 'S00', 'PCY', 'BTD', 'INV', 'PLS', '7ED', 'pMPR', 'APC', 
			'ODY', 'DKM', 'TOR', 'JUD', 'ONS', 'LGN', 'SCG', 'pREL', '8ED', 
			'MRD', 'DST', '5DN', 'CHK', 'UNH', 'BOK', 'SOK', '9ED', 'RAV', 
			'p2HG', 'pGTW', 'GPT', 'pCMP', 'DIS', 'CSP', 'CST', 'TSB', 'TSP', 
			'pHHO', 'PLC', 'pPRO', 'pGPX', 'FUT', '10E', 'pMGD', 'pSUM', 'MED', 
			'LRW', 'EVG', 'MOR', 'pLPA', 'p15A', 'SHM', 'EVE', 'DRB', 'ME2', 
			'pWPN', 'ALA', 'DD2', 'CON', 'DDC', 'ARB', 'M10', 'V09', 'HOP', 
			'ME3', 'ZEN', 'DDD', 'H09', 'WWK', 'DDE', 'ROE', 'DPA', 'ARC', 'M11', 
			'V10', 'DDF', 'SOM', 'PD2', 'ME4', 'MBS', 'DDG', 'NPH', 'CMD', 'M12', 
			'V11', 'DDH', 'ISD', 'PD3', 'DKA', 'DDI', 'AVR', 'PC2', 'M13', 'V12', 
			'DDJ', 'RTR', 'CM1', 'GTC', 'DDK', 'DDS', 'pWCQ', 'DGM', 'MMA', 'M14', 
			'V13', 'DDL', 'THS', 'C13', 'BNG', 'DDM', 'JOU', 'MD1', 'CNS', 'VMA', 
			'CPK', 'M15', 'V14', 'DDN', 'KTK', 'C14', 'DD3_GVL', 'DD3_DVD', 'DD3_EVG', 
			'DD3_JVC', 'FRF_UGIN', 'FRF', 'DDO', 'DTK', 'TPR', 'MM2', 'ORI', 'V15', 
			'DDP', 'EXP', 'BFZ', 'C15', 'OGW', 'DDQ', 'W16', 'SOI', 'EMA', 'EMN', 
			'V16', 'CN2', 'DDR', 'MPS', 'KLD', 'C16', 'PCA', 'AER', 'MM3', 'W17', 
			'MPS_AKH', 'AKH', 'CMA', 'E01', 'HOU', 'C17', 'XLN', 'DDT', 'IMA', 'E02',
			'UST', 'RIX']

CORE_SETS = [u'LEA', u'LEB', u'2ED', u'3ED', u'4ED', u'5ED', u'6ED', u'7ED', u'8ED',
			 u'9ED', u'10E', u'M10', u'M11', u'M12', u'M13', u'M14', u'M15', u'ORI']

EXPANSION_SETS = [u'ARN', u'ATQ', u'LEG', u'DRK', u'FEM', u'ICE', u'HML', u'ALL', u'MIR',
				  u'VIS', u'WTH', u'TMP', u'STH', u'EXO', u'USG', u'ULG', u'UDS', u'MMQ',
				  u'NMS', u'PCY', u'INV', u'PLS', u'APC', u'ODY', u'TOR', u'JUD', u'ONS',
				  u'LGN', u'SCG', u'MRD', u'DST', u'5DN', u'CHK', u'BOK', u'SOK', u'RAV',
				  u'GPT', u'DIS', u'CSP', u'TSB', u'TSP', u'PLC', u'FUT', u'LRW', u'MOR',
				  u'SHM', u'EVE', u'ALA', u'CON', u'ARB', u'ZEN', u'WWK', u'ROE', u'SOM',
				  u'MBS', u'NPH', u'ISD', u'DKA', u'AVR', u'RTR', u'GTC', u'DGM', u'THS',
				  u'BNG', u'JOU', u'KTK', u'FRF', u'DTK', u'BFZ', u'OGW', u'SOI', u'EMN',
				  u'KLD', u'AER', u'AKH', u'HOU', u'XLN', u'RIX']

PROMO_SETS = [u'pDRC', u'pLGM', u'pMEI', u'pARL', u'pCEL', u'pPOD', u'pPRE', u'pJGP',
			  u'pALP', u'pGRU', u'pWOR', u'pWOS', u'pSUS', u'pFNM', u'pELP', u'pMPR',
			  u'pREL', u'p2HG', u'pGTW', u'pCMP', u'pHHO', u'pPRO', u'pGPX', u'pMGD',
			  u'pSUM', u'pLPA', u'p15A', u'pWPN', u'pWCQ', u'FRF_UGIN']

DUEL_DECKS = [u'EVG', u'DD2', u'DDC', u'DDD', u'DDE', u'DDF', u'DDG', u'DDH', u'DDI',
			  u'DDJ', u'DDK', u'DDL', u'DDM', u'DDN', u'DD3_GVL', u'DD3_EVG', u'DD3_DVD',
			  u'DD3_JVC', u'DDO', u'DDP', u'DDQ', u'DDR', u'DDS', u'DDT']

BOX_SETS = [u'RQS', u'MGB', u'ATH', u'BRB', u'BTD', u'DKM', u'CST', u'DPA', u'MD1']

MASTERS_SETS = [u'MED', u'ME2', u'ME3', u'ME4', u'VMA']

PREMIUM_DECKS = [u'H09', u'PD2', u'PD3']

BOARD_GAME_DECKS = [u'E02']

UN_SETS = [u'UGL', u'UNH', u'UST']

FROM_THE_VAULT = [u'DRB', u'V09', u'V10', u'V11', u'V12', u'V13', u'V14', u'V15', u'V16']

VANGUARD = [u'VAN']

MASTERPIECE_SETS = [u'EXP', u'MPS', u'MPS_AKH']

COMMANDER_SETS = [u'CMD', u'CM1', u'C13', u'C14', u'C15', u'C16', u'CMA', u'C17']

ARCHENEMY = [u'ARC', u'E01']

PLANECHASE = [u'HOP', u'PC2', u'PCA']

REPRINT_SETS = [u'CED', u'CEI', u'CHR', u'MMA', u'TPR', u'MM2', u'EMA', u'MM3', u'IMA']

CONSPIRACY = [u'CNS', u'CN2']

STARTER_SETS = [u'ITP', u'POR', u'PO2', u'PTK', u'S99', u'S00', u'CP1', u'CP2', u'CP3', u'W16', u'W17']

'''
Creature Data Constants
'''

RACES = ["Aetherborn", "Angel", "Antelope", "Ape", "Archon", "Assembly-Worker", "Atog",
		 "Aurochs", "Avatar", "Badger", "Basilisk", "Bat", "Bear", "Beast", "Beeble",
		 "Bird", "Blinkmoth", "Boar", "Bringer", "Brushwagg", "Camarid", "Camel",
		 "Caribou", "Carrier", "Cat", "Centaur", "Cephalid", "Chimera", "Cockatrice",
		 "Construct", "Crab", "Crocodile", "Cyclops", "Dauthi", "Demon", "Devil",
		 "Dinosaur", "Djinn", "Dragon", "Drake", "Dreadnought", "Dryad", "Dwarf",
		 "Efreet", "Eldrazi", "Elemental", "Elephant", "Elf", "Elk", "Eye", "Faerie",
		 "Ferret", "Fish", "Fox", "Frog", "Fungus", "Gargoyle", "Germ", "Giant", "Gnome",
		 "Goat", "Goblin", "God", "Golem", "Gorgon", "Graveborn", "Gremlin", "Griffin",
		 "Hag", "Harpy", "Hellion", "Hippo", "Hippogriff", "Homarid", "Homunculus", "Horror",
		 "Horse", "Hound", "Human", "Hydra", "Hyena", "Illusion", "Imp", "Incarnation",
		 "Insect", "Jackal", "Jellyfish", "Juggernaut", "Kavu", "Kirin", "Kithkin", "Kobold",
		 "Kor", "Kraken", "Lamia", "Lammasu", "Leech", "Leviathan", "Lhurgoyf", "Licid", "Lizard",
		 "Manticore", "Masticore", "Merfolk", "Metathran", "Minotaur", "Mole", "Monger", "Mongoose",
		 "Monkey", "Moonfolk", "Mutant", "Myr", "Naga", "Nautilus", "Nephilim", "Nightmare",
		 "Nightstalker", "Noggle", "Nymph", "Octopus", "Ogre", "Ooze", "Orb", "Orc", "Orgg", "Ouphe",
		 "Ox", "Oyster", "Pegasus", "Pentavite", "Pest", "Phelddagrif", "Phoenix", "Pincher", "Plant",
		 "Praetor", "Prism", "Rabbit", "Rat", "Reflection", "Rhino", "Sable", "Salamander", "Sand",
		 "Saproling", "Satyr", "Scarecrow", "Scorpion", "Serpent", "Servo", "Shade", "Shapeshifter",
		 "Sheep", "Siren", "Skeleton", "Slith", "Sliver", "Slug", "Snake", "Soltari", "Spawn", "Specter",
		 "Sphinx", "Spider", "Spike", "Spirit", "Splinter", "Sponge", "Squid", "Squirrel", "Starfish",
		 "Surrakar", "Tetravite", "Thalakos", "Thopter", "Thrull", "Treefolk", "Trilobite", "Triskelavite",
		 "Troll", "Turtle", "Unicorn", "Vampire", "Vedalken", "Viashino", "Volver", "Wall", "Weird", "Werewolf",
		 "Whale", "Wolf", "Wolverine", "Wombat", "Worm", "Wraith", "Wurm", "Yeti", "Zombie", "Zubera"]

CLASSES = ["Advisor", "Ally", "Archer", "Artificer", "Assassin1", "Barbarian1", "Berserker",
		   "Citizen", "Cleric", "Coward", "Deserter", "Drone", "Druid", "Elder", "Flagbearer",
		   "Knight", "Mercenary", "Minion", "Monk", "Mystic", "Ninja", "Nomad", "Pilot", "Pirate",
		   "Processor", "Rebel", "Rigger", "Rogue", "Samurai", "Scion", "Scout", "Serf", "Shaman",
		   "Soldier", "Spellshaper", "Survivor", "Warrior", "Wizard"]

'''
KEYWORD CONSTANTS
'''
KEYWORDS = ["Deathtouch", "Defender", "Double Strike", "Enchant", "Equip", "First Strike", "Flash",
			"Flying", "Haste", "Hexproof", "Indestructible", "Intimidate", "Landwalk", "Lifelink",
			"Protection", "Reach", "Shroud", "Trample", "Vigilance", "Banding", "Rampage", "Cumulative Upkeep",
			"Flanking", "Phasing", "Buyback", "Shadow", "Cycling", "Echo", "Horsemanship", "Fading", "Kicker",
			"Flashback", "Madness", "Fear", "Morph", "Amplify", "Provoke", "Storm", "Affinity", "Entwine",
			"Modular", "Sunburst", "Bushido", "Soulshift", "Splice", "Offering", "Ninjutsu", "Epic", "Convoke",
			"Dredge", "Transmute", "Bloodthirst", "Haunt", "Replicate", "Forecast", "Graft", "Recover",
			"Ripple", "Split Second", "Suspend", "Vanishing", "Absorb", "Aura Swap", "Delve", "Fortify",
			"Frenzy", "Gravestorm", "Poisonous", "Transfigure", "Champion", "Changeling", "Evoke", "Hideaway",
			"Prowl", "Reinforce", "Conspire", "Persist", "Wither", "Retrace", "Devour", "Exalted", "Unearth",
			"Cascade", "Annihilator", "Level Up", "Rebound", "Totem Armor", "Infect", "Battle Cry",
			"Living Weapon", "Undying", "Miracle", "Soulbond", "Overload", "Scavenge", "Unleash", "Cipher",
			"Evolve", "Extort", "Fuse", "Bestow", "Tribute", "Dethrone", "Hidden Agenda", "Outlast", "Prowess",
			"Dash", "Exploit", "Menace", "Renown", "Awaken", "Devoid", "Ingest", "Myriad", "Surge", "Skulk",
			"Emerge", "Escalate", "Melee", "Crew", "Fabricate", "Partner", "Undaunted", "Improvise", "Aftermath",
			"Embalm", "Eternalize", "Afflict"]