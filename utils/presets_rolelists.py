from utils import roles as Roles
from utils import role_buckets as RoleBuckets
from utils import RoleList

__all__ = ['AllAny', 'Classic', 'Ranked_Practice', 'Ranked_Practice_Doom']

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


Ranked_Practice = RoleList(
    name='Ranked Practice',
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
        RoleBuckets.CovenPower,
        RoleBuckets.CovenUtility,
        RoleBuckets.RandomCoven,
        RoleBuckets.RandomCoven,
        RoleBuckets.NeutralEvil,
        RoleBuckets.RandomNeutral
    ],
    banned_roles={Roles.Pirate}
)

Ranked_Practice_Doom = RoleList(
    name='Ranked Practice Doom',
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
        RoleBuckets.CovenPower,
        RoleBuckets.CovenUtility,
        RoleBuckets.RandomCoven,
        RoleBuckets.RandomCoven,
        Roles.Doomsayer,
        RoleBuckets.RandomNeutral
    ],
    banned_roles={Roles.Pirate}
)
