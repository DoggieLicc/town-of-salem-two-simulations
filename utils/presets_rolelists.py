from utils import roles as Roles
from utils import role_buckets as RoleBuckets
from utils import RoleList

Ranked_12p = RoleList(
    name='Ranked_12p',
    roles=[
        RoleBuckets.TownPower,
        RoleBuckets.TownInvestigative,
        RoleBuckets.TownProtective,
        RoleBuckets.TownKilling,
        RoleBuckets.CommonTown,
        RoleBuckets.CommonTown,
        RoleBuckets.CommonTown,
        RoleBuckets.CommonTown,
        RoleBuckets.CovenPower,
        RoleBuckets.CovenKilling,
        RoleBuckets.CommonCoven,
        RoleBuckets.CommonCoven
    ]
)

Ranked_15p = RoleList(
    name='Ranked_15p',
    roles=[
        RoleBuckets.TownPower,
        RoleBuckets.TownInvestigative,
        RoleBuckets.TownInvestigative,
        RoleBuckets.TownProtective,
        RoleBuckets.TownKilling,
        RoleBuckets.CommonTown,
        RoleBuckets.CommonTown,
        RoleBuckets.CommonTown,
        RoleBuckets.CommonTown,
        RoleBuckets.CommonTown,
        RoleBuckets.CovenPower,
        RoleBuckets.CovenKilling,
        RoleBuckets.CommonCoven,
        RoleBuckets.CommonCoven,
        RoleBuckets.NeutralPariah
    ]
)

Classic_7p = RoleList(
    name='Classic_7p',
    roles=[
        RoleBuckets.TownInvestigative,
        RoleBuckets.TownProtective,
        RoleBuckets.CommonTown,
        RoleBuckets.CommonTown,
        RoleBuckets.CommonTown,
        RoleBuckets.RandomCoven,
        RoleBuckets.CommonCoven
    ],
    banned_roles={
        Roles.Bodyguard,
        Roles.Barber,
        Roles.Trapper,
        Roles.Deputy,
        Roles.Veteran
    }
)

Testing_3p = RoleList(
    name='testing',
    roles=[
        Roles.Oracle,
        Roles.CovenLeader,
        RoleBuckets.NeutralPariah,
    ],
    banned_roles={
        Roles.Bodyguard,
        Roles.Barber,
        Roles.Trapper,
        Roles.Deputy,
        Roles.Veteran
    }
)

Taa_2p = RoleList(
    name='taa_2p',
    roles=[
        RoleBuckets.TrueAny,
        RoleBuckets.TrueAny,
    ]
)

