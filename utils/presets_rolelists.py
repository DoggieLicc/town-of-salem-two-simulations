from utils import roles as Roles
from utils import role_buckets as RoleBuckets
from utils import RoleList

__all__ = ['AllAny', 'Classic']

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
