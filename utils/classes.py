from __future__ import annotations

import multiprocessing
from dataclasses import dataclass, field
from typing import List, Union, Optional, Set, Callable
from functools import partial

import random

__all__ = ['Role', 'RoleBucket', 'RoleList', 'parallel_generate_roles', 'Player', 'check_list_for_opposing_factions']


@dataclass(frozen=True, eq=True, slots=True)
class Role:
    name: str
    limit: Optional[int] = None


@dataclass(slots=True)
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
                roles.update(role.expand_possible_roles())

        self.cached_roles = roles
        return self.cached_roles


@dataclass(slots=True)
class RoleList:
    name: str
    roles: List[Union[Role, RoleBucket]]
    banned_roles: Set[Role] = field(default_factory=set)
    sorted_roles: List[Union[Role, RoleBucket]] = field(init=False)

    def __post_init__(self):
        # Sort role/rolebuckets by amount of possible roles to have more flexibility
        self.sorted_roles = sorted(self.roles, key=lambda r: 1 if isinstance(r, Role) else len(r.expand_possible_roles()))

    def generate_roles(self, check: Optional[Callable] = None, *_):
        while True:
            generated_roles: List[Role] = []

            for role in self.sorted_roles:
                if isinstance(role, Role):
                    generated_roles.append(role)
                else:
                    expanded_roles = role.expand_possible_roles()
                    valid_roles = get_valid_roles(generated_roles, expanded_roles, self.banned_roles)

                    if not valid_roles:
                        raise Exception(f'There were no possible roles for {role.name}!')

                    generated_roles.append(random.choice(list(valid_roles)))

            if not check or check(generated_roles):
                return generated_roles


@dataclass(slots=True)
class Player:
    name: str
    assigned_role: Optional[Role] = None
    blessed_scrolls: Optional[List[Role|RoleBucket]] = field(default_factory=list)
    cursed_scrolls: Optional[List[Role]] = field(default_factory=list)


import utils.role_buckets as RoleBuckets


def check_role_limit(generated_roles: List[Role], role: Role) -> bool:
    if not role.limit or len(generated_roles) < role.limit:
        return True

    num_roles = sum(1 for r in generated_roles if r == role)

    return num_roles + 1 <= role.limit


def check_rolebucket_limit(generated_roles: List[Role], role: Role) -> bool:
    if role in RoleBuckets.COVEN_ROLES:
        num_roles = sum(1 for r in generated_roles if r in RoleBuckets.COVEN_ROLES)

        return num_roles + 1 <= RoleBuckets.RandomCoven.limit

    
    if role in RoleBuckets.APOCALYPSE_ROLES:
        num_roles = sum(1 for r in generated_roles if r in RoleBuckets.APOCALYPSE_ROLES)
        return num_roles + 1 <= RoleBuckets.NeutralApocalypse.limit


    return True


def get_valid_roles(generated_roles: List[Role], possible_roles: Set[Role], banned_roles: Optional[Set[Role]]) -> Set[Role]:
    valid_roles = {role for role in possible_roles if role not in banned_roles and check_role_limit(generated_roles, role) and check_rolebucket_limit(generated_roles, role)}
    return valid_roles


def check_list_for_opposing_factions(role_list: List[Role]) -> bool:
    role_set = set(role_list)
    townies = role_set.intersection(RoleBuckets.TOWN_ROLES)
    coven = role_set.intersection(RoleBuckets.COVEN_ROLES)

    if townies and coven:
        return True

    apocalypse = role_set.intersection(RoleBuckets.APOCALYPSE_ROLES)

    if (townies and apocalypse) or (coven and apocalypse):
        return True

    unique_neutral_killings = role_set.intersection(RoleBuckets.NeutralKilling.expand_possible_roles())

    if unique_neutral_killings:
        return bool(townies or coven or apocalypse or (len(unique_neutral_killings) > 1))

    # print(role_list)

    return False


def parallel_generate_roles(rolelist, num_gens, check: Optional[Callable] = None):
    with multiprocessing.Pool() as pool:
        generate_func = partial(rolelist.generate_roles, check)
        results = pool.map(generate_func, range(num_gens))

    return [r for r in results if r is not None]


def calculate_percentage(count, total):
    return count * 100 / total


def calculate_category_count(category_count, total_count):
    return f'{category_count}/{total_count} ({calculate_percentage(category_count, total_count):.4f}%)'


def b_print(text: str, *args, **kwargs):

    text = '\033[1m' + text + '\033[0m'

    print(text, *args, **kwargs)


def main():
    import time

    now = time.time()

    for _ in range(10_000):
        AllAny.generate_roles(check=check_list_for_opposing_factions)

    print(f'Took {time.time() - now} seconds')


if __name__ == '__main__':
    from utils.presets_rolelists import AllAny

    #multiprocessing.set_start_method('spawn')
    main()

