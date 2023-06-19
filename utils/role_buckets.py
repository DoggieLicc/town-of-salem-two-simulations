from utils import roles as Roles
from utils.classes import RoleBucket

__all__ = ['Any', 'TownPower', 'TownKilling', 'TownProtective', 'TownSupport', 'TownInvestigative', 'RandomTown', 'CovenPower', 'CovenKilling', 'CovenUtility', 'CovenDeception', 'RandomCoven', 'NeutralApocalypse', 'NeutralEvil', 'NeutralKilling', 'RandomNeutral', 'COVEN_ROLES', 'APOCALYPSE_ROLES', 'TOWN_ROLES']


TownPower = RoleBucket(
    name='Town Power',
    possible_roles=[Roles.Jailor, Roles.Mayor, Roles.Monarch, Roles.Prosecutor]
)

TownKilling = RoleBucket(
    name='Town Killing',
    possible_roles=[Roles.Deputy, Roles.Trickster, Roles.Veteran, Roles.Vigilante]
)

TownProtective = RoleBucket(
    name='Town Protective',
    possible_roles=[Roles.Bodyguard, Roles.Cleric, Roles.Crusader, Roles.Trapper]
)

TownSupport = RoleBucket(
    name='Town Support',
    possible_roles=[Roles.Admirer, Roles.Amnesiac, Roles.Retributionist, Roles.TavernKeeper]
)

TownInvestigative = RoleBucket(
    name='Town Investigative',
    possible_roles=[Roles.Coroner, Roles.Investigator, Roles.Lookout, Roles.Psychic, Roles.Seer, Roles.Sheriff, Roles.Spy, Roles.Tracker]
)

RandomTown = RoleBucket(
    name='Random Town',
    possible_roles=[TownPower, TownKilling, TownProtective, TownSupport, TownInvestigative]
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
    possible_roles=[Roles.Necromancer, Roles.Poisoner, Roles.PotionMaster, Roles.VoodooMaster, Roles.Wilding]
)


CovenDeception = RoleBucket(
    name='Coven Deception',
    possible_roles=[Roles.Dreamweaver, Roles.Enchanter, Roles.Illusionist, Roles.Medusa]
)


RandomCoven = RoleBucket(
    name='Random Coven',
    possible_roles=[CovenPower, CovenKilling, CovenUtility, CovenDeception],
    limit=4
)

NeutralApocalypse = RoleBucket(
    name='Neutral Apocalypse',
    possible_roles=[Roles.Baker, Roles.Berserker, Roles.Plaguebearer, Roles.SoulCollector],
)

NeutralEvil = RoleBucket(
    name='Neutral Evil',
    possible_roles=[Roles.Doomsayer, Roles.Executioner, Roles.Jester, Roles.Pirate],
)

NeutralKilling = RoleBucket(
    name='Neutral Killing',
    possible_roles=[Roles.Arsonist, Roles.SerialKiller, Roles.Shroud, Roles.Werewolf],
)


RandomNeutral = RoleBucket(
    name='Random Neutral',
    possible_roles=[NeutralApocalypse, NeutralEvil, NeutralKilling],
)


Any = RoleBucket(
    name='Any',
    possible_roles=[RandomTown, RandomCoven, RandomNeutral]
)

COVEN_ROLES = RandomCoven.expand_possible_roles()

APOCALYPSE_ROLES = NeutralApocalypse.expand_possible_roles()

TOWN_ROLES = RandomTown.expand_possible_roles()

# print([v for v, h in globals().items() if isinstance(h, RoleBucket)])
