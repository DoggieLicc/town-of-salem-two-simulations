from __future__ import annotations

from dataclasses import dataclass
from typing import List, Union, Optional

import utils.helper_funcs as helpers

import random

__all__ = ['Role', 'RoleBucket', 'RoleList']


@dataclass(frozen=True, eq=True)
class Role:
    name: str
    color: Optional[int] = 0
    limit: Optional[int] = None


@dataclass
class RoleBucket:
    name: str
    possible_roles: List[Union[Role, RoleBucket]]
    color: Optional[int] = None
    limit: Optional[int] = None

    def expand_possible_roles(self):
        roles = set()

        for role in self.possible_roles:
            if isinstance(role, Role):
                roles.add(role)

            else:
                for r in role.expand_possible_roles():
                    roles.add(r)

        return list(roles)



@dataclass
class RoleList:
    roles: List[Union[Role, RoleBucket]]
    banned_roles: List[Role] = field(default_factory=list)

    def generate_roles(self):

        # Sort role/rolebuckets by amount of possible roles to have more flexibility
        sorted_roles = sorted(self.roles, key=lambda r: (1 if isinstance(r, Role) else len(r.expand_possible_roles()), r.name))

        generated_roles: List[Role] = []

        for role in sorted_roles:
            if isinstance(role, Role):
                generated_roles.append(role)

            else:
                expanded_roles = role.expand_possible_roles()
                valid_roles = helpers.get_valid_roles(generated_roles, expanded_roles, self.banned_roles)

                generated_roles.append(random.choice(valid_roles))

        return sorted(generated_roles, key=lambda r: r.name)


if __name__ == '__main__':
    from utils.presets_rolelists import *

    for _ in range(250):
        print([r.name for r in Classic.generate_roles()])
