from utils.classes import Role

__all__ = ['Prosecutor', 'Monarch', 'Mayor', 'Jailor', 'Admirer', 'Amnesiac', 'Bodyguard', 'Cleric', 'Coroner', 'Crusader', 'Investigator', 'Lookout', 'Psychic', 'Retributionist', 'Seer', 'Sheriff', 'Spy', 'TavernKeeper', 'Tracker', 'Trapper', 'Trickster', 'Veteran', 'Vigilante', 'Conjurer', 'CovenLeader', 'Dreamweaver', 'Enchanter', 'HexMaster', 'Illusionist', 'Jinx', 'Medusa', 'Necromancer', 'Poisoner', 'PotionMaster', 'Ritualist', 'VoodooMaster', 'Wilding', 'Witch', 'Baker', 'Berserker', 'Plaguebearer', 'SoulCollector', 'Arsonist', 'SerialKiller', 'Shroud', 'Werewolf', 'Doomsayer', 'Executioner', 'Jester', 'Pirate', 'Deputy']


# TOWN POWER
Prosecutor = Role(name='Prosecutor', limit=1)
Monarch = Role(name='Monarch', limit=1)
Mayor = Role(name='Mayor', limit=1)
Jailor = Role(name='Jailor', limit=1)

# RANDOM TOWN
Admirer = Role(name='Admirer')
Amnesiac = Role(name='Amnesiac')
Bodyguard = Role(name='Bodyguard')
Cleric = Role(name='Cleric')
Coroner = Role(name='Coroner')
Crusader = Role(name='Crusader')
Deputy = Role(name='Deputy')
Investigator = Role(name='Investigator')
Lookout = Role(name='Lookout')
Psychic = Role(name='Psychic')
Retributionist = Role(name='Retributionist')
Seer = Role(name='Seer')
Sheriff = Role(name='Sheriff')
Spy = Role(name='Spy')
TavernKeeper = Role(name='Tavern Keeper')
Tracker = Role(name='Tracker')
Trapper = Role(name='Trapper')
Trickster = Role(name='Trickster')
Veteran = Role(name='Veteran')
Vigilante = Role(name='Vigilante')

# RANDOM COVEN
Conjurer = Role(name='Conjurer', limit=1)
CovenLeader = Role(name='Coven Leader', limit=1)
Dreamweaver = Role(name='Dreamweaver', limit=1)
Enchanter = Role(name='Enchanter', limit=1)
HexMaster = Role(name='Hex Master', limit=1)
Illusionist = Role(name='Illusionist', limit=1)
Jinx = Role(name='Jinx', limit=1)
Medusa = Role(name='Medusa', limit=1)
Necromancer = Role(name='Necromancer', limit=1)
Poisoner = Role(name='Poisoner', limit=1)
PotionMaster = Role(name='Potion Master', limit=1)
Ritualist = Role(name='Ritualist', limit=1)
VoodooMaster = Role(name='Voodoo Master', limit=1)
Wilding = Role(name='Wilding', limit=1)
Witch = Role(name='Witch', limit=1)

# NEUTRAL APOCALYPSE
Baker = Role(name='Baker', limit=1)
Berserker = Role(name='Berserker', limit=1)
Plaguebearer = Role(name='Plaguebearer', limit=1)
SoulCollector = Role(name='Soul Collector', limit=1)

# NEUTRAL KILLING (unique colors)
Arsonist = Role(name='Arsonist', limit=6)
SerialKiller = Role(name='Serial Killer', limit=6)
Shroud = Role(name='Shroud', limit=6)
Werewolf = Role(name='Werewolf', limit=6)

# NEUTRAL EVIL (unique colors)
Doomsayer = Role(name='Doomsayer', limit=6)
Executioner = Role(name='Executioner', limit=6)
Jester = Role(name='Jester', limit=6)
Pirate = Role(name='Pirate', limit=1)
