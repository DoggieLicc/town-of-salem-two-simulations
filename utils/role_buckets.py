from utils import roles as Roles
from utils.classes import RoleBucket

# __all__ = ['Any', 'TownPower', 'TownKilling', 'TownProtective', 'TownSupport', 'TownInvestigative', 'RandomTown', 'CovenPower', 'CovenKilling', 'CovenUtility', 'CovenDeception', 'RandomCoven', 'NeutralApocalypse', 'NeutralEvil', 'NeutralKilling', 'RandomNeutral', 'COVEN_ROLES', 'APOCALYPSE_ROLES', 'TOWN_ROLES', 'ROLE_BUCKETS']

TownPower = RoleBucket(
    name='Town Power',
    possible_roles=[Roles.Jailor, Roles.Mayor, Roles.Monarch, Roles.Prosecutor, Roles.Marshal]
)

TownKilling = RoleBucket(
    name='Town Killing',
    possible_roles=[Roles.Deputy, Roles.Trickster, Roles.Veteran, Roles.Vigilante, Roles.Barber]
)

TownProtective = RoleBucket(
    name='Town Protective',
    possible_roles=[Roles.Bodyguard, Roles.Cleric, Roles.Crusader, Roles.Trapper, Roles.Oracle]
)

TownSupport = RoleBucket(
    name='Town Support',
    possible_roles=[Roles.Admirer, Roles.Coachmaster, Roles.Retributionist, Roles.TavernKeeper]
)

TownInvestigative = RoleBucket(
    name='Town Investigative',
    possible_roles=[Roles.Coroner, Roles.Investigator, Roles.Lookout, Roles.Psychic, Roles.Seer, Roles.Sheriff, Roles.Spy, Roles.Tracker]
)

TownSpecial = RoleBucket(
    name='Town Special',
    possible_roles=[Roles.Spiritualist]
)

CommonTown = RoleBucket(
    name='Common Town',
    possible_roles=[TownKilling, TownProtective, TownSupport, TownInvestigative]
)

RandomTown = RoleBucket(
    name='Random Town',
    possible_roles=[TownPower, CommonTown]
)

CovenPower = RoleBucket(
    name='Coven Power',
    possible_roles=[Roles.CovenLeader, Roles.HexMaster, Roles.Witch]
)

CovenKilling = RoleBucket(
    name='Coven Killing',
    possible_roles=[Roles.Conjurer, Roles.Jinx, Roles.Ritualist]
)

CovenUtility = RoleBucket(
    name='Coven Utility',
    possible_roles=[Roles.Necromancer, Roles.Poisoner, Roles.PotionMaster, Roles.VoodooMaster, Roles.Wilding, Roles.Banshee]
)

CovenDeception = RoleBucket(
    name='Coven Deception',
    possible_roles=[Roles.Dreamweaver, Roles.Enchanter, Roles.Illusionist, Roles.Medusa]
)

SalientCoven = RoleBucket(
    name='Salient Coven',
    possible_roles=[CovenPower, CovenKilling]
)

CommonCoven = RoleBucket(
    name='Common Coven',
    possible_roles=[CovenDeception, CovenUtility]
)

RandomCoven = RoleBucket(
    name='Random Coven',
    possible_roles=[SalientCoven, CommonCoven],
    limit=4
)

CovenSpecial = RoleBucket(
    name='Coven Special',
    possible_roles=[Roles.SuperCoven]
)

SoulCollectorOrWarlock = RoleBucket(
    name='Soul Collector/Warlock',
    possible_roles=[Roles.SoulCollector, Roles.Warlock]
)

NeutralApocalypse = RoleBucket(
    name='Neutral Apocalypse',
    possible_roles=[Roles.Baker, Roles.Berserker, Roles.Plaguebearer, SoulCollectorOrWarlock],
)

NeutralEvil = RoleBucket(
    name='Neutral Evil',
    possible_roles=[Roles.Doomsayer, Roles.Executioner, Roles.Jester, Roles.Inquisitor],
)

NeutralKilling = RoleBucket(
    name='Neutral Killing',
    possible_roles=[Roles.Arsonist, Roles.SerialKiller, Roles.Shroud, Roles.Werewolf],
)

NeutralPariah = RoleBucket(
    name='Neutral Pariah',
    possible_roles=[Roles.Judge, Roles.Auditor, Roles.Starspawn, Roles.Politician]
)

NeutralSpecial = RoleBucket(
    name='Neutral Special',
    possible_roles=[Roles.Vampire, Roles.CursedSoul, Roles.Jackal]
)

CommonNeutral = RoleBucket(
    name='Common Neutral',
    possible_roles=[NeutralEvil, NeutralPariah]
)

NeutralDangerous = RoleBucket(
    name='Neutral Dangerous',
    possible_roles=[NeutralKilling, NeutralApocalypse]
)

RandomNeutral = RoleBucket(
    name='Random Neutral',
    possible_roles=[CommonNeutral, NeutralDangerous],
)

Any = RoleBucket(
    name='Any',
    possible_roles=[RandomTown, RandomCoven, RandomNeutral]
)

TrueAny = RoleBucket(
    name='True Any',
    possible_roles=[Any, TownSpecial, NeutralSpecial]
)

COVEN_ROLES = RandomCoven.expand_possible_roles()

APOCALYPSE_ROLES = NeutralApocalypse.expand_possible_roles()

TOWN_ROLES = RandomTown.expand_possible_roles()

ROLE_BUCKETS = [h for v, h in globals().items() if isinstance(h, RoleBucket)]
