from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Union, Optional, Set

import random

__all__ = ['Role', 'RoleBucket', 'RoleList']


@dataclass(frozen=True, eq=True)
class Role:
    name: str
    limit: Optional[int] = None


@dataclass
class RoleBucket:
    name: str
    possible_roles: List[Union[Role, RoleBucket]]
    limit: Optional[int] = None
    cached_roles: Optional[Set[Role]] = None

    def expand_possible_roles(self) -> Set[Role]:
        if self.cached_roles:
            return self.cached_roles

        roles = set()

        for role in self.possible_roles:
            if isinstance(role, Role):
                roles.add(role)

            else:
                for r in role.expand_possible_roles():
                    roles.add(r)

        self.cached_roles = roles
        return self.cached_roles


@dataclass
class RoleList:
    name: str
    roles: List[Union[Role, RoleBucket]]
    banned_roles: Set[Role] = field(default_factory=set)
    sorted_roles: List[Union[Role, RoleBucket]] = field(init=False)

    def __post_init__(self):
        # Sort role/rolebuckets by amount of possible roles to have more flexibility
        self.sorted_roles = sorted(self.roles, key=lambda r: 1 if isinstance(r, Role) else len(r.expand_possible_roles()))

    def generate_roles(self):

        generated_roles: List[Role] = []

        for role in self.sorted_roles:
            if isinstance(role, Role):
                generated_roles.append(role)

            else:
                expanded_roles = role.expand_possible_roles()
                valid_roles = get_valid_roles(generated_roles, expanded_roles, self.banned_roles)

                generated_roles.append(random.choice(list(valid_roles)))

        return generated_roles

import utils.role_buckets as RoleBuckets


def check_role_limit(generated_roles: List[Role], role: Role) -> bool:
    if not role.limit or len(generated_roles) < role.limit:
        return True

    num_roles = len([r for r in generated_roles if r == role])

    return num_roles + 1 <= role.limit


def check_rolebucket_limit(generated_roles: List[Role], role: Role) -> bool:
    if role in RoleBuckets.COVEN_ROLES:
        num_roles = len([r for r in generated_roles if r in RoleBuckets.COVEN_ROLES])

        return num_roles + 1 <= RoleBuckets.RandomCoven.limit

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


if __name__ == '__main__':
    from utils.presets_rolelists import *

    import time

    now = time.time()

    for _ in range(1000):
        c = AllAny.generate_roles()
        check_list_for_opposing_factions(c)

    print(f'Took {time.time() - now} seconds')

