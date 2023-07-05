import utils.role_buckets
from utils.presets_rolelists import AllAny
from utils.roles import Doomsayer

import random

# Simulate the odds of Doomsayer winning N1 by randomly guessing in AllAny

if __name__ == '__main__':

    role_lists = [AllAny, Classic, Ranked1_doom]

    print('Available rolelists: ' + ', '.join([f"'{rl.name}'" for rl in role_lists]))

    while True:
        rolelist_str = input('Type in a rolelist to simulate.: ')

        rolelist = [rl for rl in role_lists if rl.name.lower() == rolelist_str.lower().strip("' \"")]

        if rolelist:
            break

    rolelist = rolelist[0]

    print(f'You selected: {rolelist.name}\n')

    print('\n'.join([f'  {r.name}' for r in rolelist.roles]))

    while True:
        num_gens_str = input('Type in the amount of lists with doomsayer to generate (default:1000): ')
        num_gens = None

        if not num_gens_str:
            num_gens = 1000

        else:
            if num_gens_str.isnumeric():
                num_gens = int(num_gens_str)

        if num_gens:
            break

    list_count = 0
    success_count = 0

    num_coven = 0

    coven_roles = utils.role_buckets.COVEN_ROLES

    print('Generating...')

    while list_count < num_gens:

        roles = rolelist.generate_roles()

        doomsayers = [r for r in roles if r == Doomsayer]

        if not doomsayers:
            continue

        list_count += 1

        if list_count % 1000 == 0:
            print(f'generated {list_count}/{num_gens}')

        role_copy = roles.copy()
        role_copy.remove(Doomsayer)

        num_coven += len([r for r in roles if r in coven_roles])

        for doomsayer in doomsayers:
            random_roles = random.sample(role_copy, 3)

            if len([r for r in random_roles if r in coven_roles]) == 3:
                success_count += 1
                continue

                #print(random_roles)

    print(f'{success_count}/{list_count} ({(success_count*100 / list_count): .4f}%)')
    print(f'Average amount of coven roles per game: {num_coven/num_gens}')