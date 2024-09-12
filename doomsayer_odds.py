import multiprocessing

import utils.role_buckets
from utils.presets_rolelists import AllAny, Classic, Ranked
from utils.roles import Doomsayer
from utils.classes import parallel_generate_roles
from utils import build_list, simple_input

import random

# Simulate the odds of Doomsayer winning N1 by randomly guessing in a specified role list


def check(rolelist):
    return [r for r in rolelist if r == Doomsayer]


def main():
    role_lists = [AllAny, Classic, Ranked]

    print('Available rolelists: ' + ', '.join([f"'{rl.name}'" for rl in role_lists]))

    while True:
        rolelist_str = input('Type in a rolelist to simulate (or "custom" for custom): ')

        if rolelist_str.lower().strip() == 'custom':
            rolelist = build_list()
            break

        rolelist = [rl for rl in role_lists if rl.name.lower() == rolelist_str.lower().strip("' \"")]

        if rolelist:
            rolelist = rolelist[0]
            break

    print(f'You selected: {rolelist.name}\n')

    print('\n'.join([f'  {r.name}' for r in rolelist.roles]))

    num_gens = simple_input.get_integer_input('Type in the amount of lists to generate (default:10000): ', 10000)

    success_count = 0

    num_coven = 0

    coven_roles = utils.role_buckets.COVEN_ROLES

    print('Generating...')

    results = parallel_generate_roles(rolelist, num_gens, check=check)

    for result in results:
        role_copy = result.copy()
        role_copy.remove(Doomsayer)

        num_coven += len([r for r in result if r in coven_roles])

        doomsayers = [r for r in result if r == Doomsayer]

        for _ in doomsayers:
            random_roles = random.sample(role_copy, 3)

            if len([r for r in random_roles if r in coven_roles]) == 3:
                success_count += 1
                continue

    print(f'{success_count}/{num_gens} ({(success_count*100 / num_gens): .4f}%)')
    print(f'Average amount of coven roles per game: {num_coven/num_gens}')


if __name__ == '__main__':
    multiprocessing.set_start_method('spawn')
    main()
