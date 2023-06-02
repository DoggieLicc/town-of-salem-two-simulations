from utils.classes import *
from typing import List

import utils.role_buckets as RoleBuckets
import utils.roles as Roles


def check_role_limit(generated_roles: List[Role], role: Role) -> bool:
    if not role.limit:
        return True

    num_roles = len([r for r in generated_roles if r == role])

    return num_roles + 1 <= role.limit


def check_rolebucket_limit(generated_roles: List[Role], role: Role) -> bool:
    coven_roles = RoleBuckets.RandomCoven.expand_possible_roles()
    apocalypse_roles = RoleBuckets.NeutralApocalypse.expand_possible_roles()

    if role in coven_roles:
        num_roles = len([r for r in generated_roles if generated_roles in coven_roles])

        return num_roles + 1 <= RoleBuckets.RandomCoven.limit
    elif role in apocalypse_roles:
        num_roles = len([r for r in generated_roles if generated_roles in apocalypse_roles])

        return num_roles + 1 <= RoleBuckets.NeutralApocalypse.limit

    else:
        return True


def get_valid_roles(generated_roles: List[Role], possible_roles: List[Role]) -> List[Role]:

    valid_roles: List[Role] = []

    for role in possible_roles:
        if check_role_limit(generated_roles, role) and check_rolebucket_limit(generated_roles, role):
            valid_roles.append(role)

    return valid_roles
