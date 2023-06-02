from utils.classes import *
from typing import List, Optional

import utils.role_buckets as RoleBuckets


def check_role_limit(generated_roles: List[Role], role: Role) -> bool:
    if not role.limit or len(generated_roles) < role.limit:
        return True

    num_roles = len([r for r in generated_roles if r == role])

    return num_roles + 1 <= role.limit


def check_rolebucket_limit(generated_roles: List[Role], role: Role) -> bool:
    if role in RoleBuckets.COVEN_ROLES:
        num_roles = len([r for r in generated_roles if generated_roles in RoleBuckets.COVEN_ROLES])

        return num_roles + 1 <= RoleBuckets.RandomCoven.limit

    if role in RoleBuckets.APOCALYPSE_ROLES:
        num_roles = len([r for r in generated_roles if generated_roles in RoleBuckets.APOCALYPSE_ROLES])

        return num_roles + 1 <= RoleBuckets.NeutralApocalypse.limit

    return True


def get_valid_roles(generated_roles: List[Role], possible_roles: List[Role], banned_roles: Optional[List[Role]]) -> List[Role]:

    valid_roles: List[Role] = []

    for role in possible_roles:
        if not role in banned_roles and check_role_limit(generated_roles, role) and check_rolebucket_limit(generated_roles, role):
            valid_roles.append(role)

    return valid_roles
