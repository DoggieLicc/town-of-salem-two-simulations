from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Union, Optional, Set

import utils.helper_funcs as helpers

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
                valid_roles = helpers.get_valid_roles(generated_roles, expanded_roles, self.banned_roles)

                generated_roles.append(random.choice(list(valid_roles)))

        return generated_roles


if __name__ == '__main__':
    from utils.presets_rolelists import *

    import time

    now = time.time()

    for _ in range(1000):
        c = AllAny.generate_roles()
        helpers.check_list_for_opposing_factions(c)

    print(f'Took {time.time() - now} seconds')

