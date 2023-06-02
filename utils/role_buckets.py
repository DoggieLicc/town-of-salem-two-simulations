from utils.classes import *
import utils.roles as Roles

__all__ = ['Any', 'TownPower', 'TownKilling', 'TownProtective', 'TownSupport', 'TownInvestigative', 'RandomTown', 'CovenPower', 'CovenKilling', 'CovenUtility', 'CovenDeception', 'RandomCoven', 'NeutralApocalypse', 'NeutralEvil', 'NeutralKilling', 'RandomNeutral']


Any = RoleBucket(
    name='Any',
    possible_roles=Roles.__all__
)

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
    color=0x06e00c,
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
    color=0xb545ff,
    possible_roles=[CovenPower, CovenKilling, CovenUtility, CovenDeception],
    limit=4
)

NeutralApocalypse = RoleBucket(
    name='Neutral Apocalypse',
    color=0xff004e,
    possible_roles=[Roles.Baker, Roles.Berserker, Roles.Plaguebearer, Roles.SoulCollector],
    limit=1
)

NeutralEvil = RoleBucket(
    name='NeutralEvil',
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

# print([v for v, h in globals().items() if isinstance(h, RoleBucket)])
