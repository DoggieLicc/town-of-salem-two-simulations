from utils.classes import *
from typing import List, Optional, Set

import utils.role_buckets as RoleBuckets

__all__ = ['check_role_limit', 'check_rolebucket_limit', 'check_list_for_opposing_factions']

def check_role_limit(generated_roles: List[Role], role: Role) -> bool:
    if not role.limit or len(generated_roles) < role.limit:
        return True

    num_roles = len([r for r in generated_roles if r == role])

    return num_roles + 1 <= role.limit


def check_rolebucket_limit(generated_roles: List[Role], role: Role) -> bool:
    if role in RoleBuckets.COVEN_ROLES:
        num_roles = len([r for r in generated_roles if r in RoleBuckets.COVEN_ROLES])

        return num_roles + 1 <= RoleBuckets.RandomCoven.limit

    if role in RoleBuckets.APOCALYPSE_ROLES:
        num_roles = len([r for r in generated_roles if r in RoleBuckets.APOCALYPSE_ROLES])

        return num_roles + 1 <= RoleBuckets.NeutralApocalypse.limit

    return True


def get_valid_roles(generated_roles: List[Role], possible_roles: Set[Role], banned_roles: Optional[Set[Role]]) -> Set[Role]:

    valid_roles: Set[Role] = set()

    for role in possible_roles:
        if not role in banned_roles and check_role_limit(generated_roles, role) and check_rolebucket_limit(generated_roles, role):
            valid_roles.add(role)

    return valid_roles


def check_list_for_opposing_factions(role_list: List[Role]) -> bool:
    townies = [r for r in role_list if r in RoleBuckets.TOWN_ROLES]
    coven = [r for r in role_list if r in RoleBuckets.COVEN_ROLES]

    if townies and coven:
        return True

    apocalypse = [r for r in role_list if r in RoleBuckets.APOCALYPSE_ROLES]

    if (townies and apocalypse) or (coven and apocalypse):
        return True

    unique_neutral_killings = set([r for r in role_list if r in RoleBuckets.NeutralKilling.expand_possible_roles()])

    if unique_neutral_killings:
        return bool(townies or coven or apocalypse or len(unique_neutral_killings))

    return False
