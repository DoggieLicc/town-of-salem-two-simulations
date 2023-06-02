import utils.roles as Roles
import utils.role_buckets as RoleBuckets

from utils.classes import *

__all__ = ['AllAny', 'Classic']

AllAny = RoleList(
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
    banned_roles=[Roles.Amnesiac, Roles.Spy, Roles.Trickster]
)