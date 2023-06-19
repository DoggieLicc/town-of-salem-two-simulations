from utils.presets_rolelists import AllAny, Classic, Ranked1
from utils.classes import check_list_for_opposing_factions
from collections import Counter


if __name__ == '__main__':
    role_lists = [AllAny, Classic, Ranked1]

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
        check_opposing_facs_check_str = input('Check generated lists for opposing factions? (y/N): ')

        if not check_opposing_facs_check_str:
            check_opposing_facs = False
            break

        if check_opposing_facs_check_str.lower() == 'y':
            check_opposing_facs = True
            break

        if check_opposing_facs_check_str.lower() == 'n':
            check_opposing_facs = False
            break

    if check_opposing_facs:
        print('Checking lists for opposing factions!')

    while True:
        num_gens_str = input('Type in the amount of lists to generate (default:10000): ')
        num_gens = None

        if not num_gens_str:
            num_gens = 10000

        else:
            if num_gens_str.isnumeric():
                num_gens = int(num_gens_str)

        if num_gens:
            break

    print(f'Amount of rolelists to generate: {num_gens}')

    role_counter = Counter()

    print('Generating...')

    successful_gens = 0

    while successful_gens < num_gens:
        roles = rolelist.generate_roles()

        if check_opposing_facs:
            opposing_facs = check_list_for_opposing_factions(roles)

            if not opposing_facs:
                print(f'Caught generated list with no opposing factions, retrying...: {roles}')
                continue

        successful_gens += 1

        if successful_gens % 1000 == 0:
            print(f'generated {successful_gens}/{num_gens}')

        unique_roles = set(roles)
        role_counter.update(unique_roles)

    print('Done!\n\n')

    for k, v in role_counter.most_common():
        print(f'{k.name}: ({v}/{num_gens}) {v*100/num_gens: .2f}%')
