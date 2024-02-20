from utils import roles as Roles
from utils import role_buckets as RoleBuckets
from utils import RoleList

__all__ = ['AllAny', 'Classic', 'Ranked']

AllAny = RoleList(
    name='All Any',
    roles=[
        RoleBuckets.Any,
        RoleBuckets.Any,
        RoleBuckets.Any,
        RoleBuckets.Any,
        RoleBuckets.Any,
        RoleBuckets.Any,
        RoleBuckets.Any,
        RoleBuckets.Any,
        RoleBuckets.Any,
        RoleBuckets.Any,
        RoleBuckets.Any,
        RoleBuckets.Any,
        RoleBuckets.Any,
        RoleBuckets.Any,
        RoleBuckets.Any
    ]
)

Classic = RoleList(
    name='Classic',
    roles=[
        Roles.Mayor,
        Roles.Seer,
        Roles.Cleric,
        Roles.Sheriff,
        Roles.TavernKeeper,
        Roles.Investigator,
        Roles.CovenLeader,
        Roles.Poisoner,
        Roles.Enchanter,
        Roles.SerialKiller,
        Roles.Executioner,
        Roles.Jester,
        RoleBuckets.TownKilling,
        RoleBuckets.RandomTown,
        RoleBuckets.RandomTown
    ],
    banned_roles={Roles.Amnesiac, Roles.Spy, Roles.Trickster}
)


Ranked = RoleList(
    name='Ranked',
    roles=[
        RoleBuckets.TownPower,
        RoleBuckets.TownKilling,
        RoleBuckets.TownProtective,
        RoleBuckets.TownInvestigative,
        RoleBuckets.TownInvestigative,
        RoleBuckets.RandomTown,
        RoleBuckets.RandomTown,
        RoleBuckets.RandomTown,
        RoleBuckets.RandomTown,
        RoleBuckets.CovenKilling,
        RoleBuckets.RandomCoven,
        RoleBuckets.RandomCoven,
        RoleBuckets.RandomCoven,
        RoleBuckets.NeutralEvil,
        RoleBuckets.NeutralKilling
    ],
    banned_roles={Roles.Pirate}
)


Town_Traitor = RoleList(
    name='Town Traitor',
    roles=[
        Roles.Crusader,
        RoleBuckets.TownPower,
        RoleBuckets.TownPower,
        RoleBuckets.TownKilling,
        RoleBuckets.TownProtective,
        RoleBuckets.TownInvestigative,
        RoleBuckets.TownInvestigative,
        RoleBuckets.TownSupport,
        RoleBuckets.RandomTown,
        RoleBuckets.RandomTown,
        RoleBuckets.RandomTown,
        RoleBuckets.CovenPower,
        RoleBuckets.CovenKilling,
        RoleBuckets.RandomCoven,
        RoleBuckets.RandomCoven
    ],
    banned_roles={Roles.Admirer, Roles.Trickster, Roles.Dreamweaver}
)