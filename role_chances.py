import multiprocessing

from utils.presets_rolelists import AllAny, Classic, Ranked1
from utils.classes import check_list_for_opposing_factions, parallel_generate_roles, calculate_percentage, b_print
from utils import build_list

import utils.role_buckets as RoleBuckets

from collections import Counter


def main():
    role_lists = [AllAny, Classic, Ranked1]

    print('Available rolelists: ' + ', '.join([f"'{rl.name}'" for rl in role_lists]))

    while True:
        rolelist_str = input('Type in a rolelist to simulate or "custom": ')

        if rolelist_str.lower().strip() == 'custom':
            rolelist = build_list()
            break

        rolelist = [rl for rl in role_lists if rl.name.lower() == rolelist_str.lower().strip("' \"")]

        if rolelist:
            rolelist = rolelist[0]
            break

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

    print('Generating...')

    generated_roles = parallel_generate_roles(rolelist, num_gens, check_list_for_opposing_factions if check_opposing_facs else None)

    print('Done!\n\n')

    role_counter = Counter()

    for roles in generated_roles:
        role_counter.update(roles)

    town_count = sum(role_counter.get(role, 0) for role in RoleBuckets.TOWN_ROLES)
    coven_count = sum(role_counter.get(role, 0) for role in RoleBuckets.COVEN_ROLES)
    na_count = sum(role_counter.get(role, 0) for role in RoleBuckets.APOCALYPSE_ROLES)
    nk_count = sum(role_counter.get(role, 0) for role in RoleBuckets.NeutralKilling.expand_possible_roles())
    ne_count = sum(role_counter.get(role, 0) for role in RoleBuckets.NeutralEvil.expand_possible_roles())

    total_count = town_count+coven_count+na_count+nk_count+ne_count

    role_len = len(rolelist.roles)

    b_print(f"Town: ({town_count/num_gens:.2f}/{role_len}) {calculate_percentage(town_count, total_count):.2f}%")
    for role in sorted(RoleBuckets.TOWN_ROLES, key=lambda r: role_counter.get(r, 0), reverse=True):
        count = role_counter.get(role, 0)
        print(f"{role.name}: ({count}/{num_gens}) {calculate_percentage(count, num_gens):.2f}%")

    b_print(f"\nCoven: ({coven_count/num_gens:.2f}/{role_len}) {calculate_percentage(coven_count, total_count):.2f}%")
    for role in sorted(RoleBuckets.COVEN_ROLES, key=lambda r: role_counter.get(r, 0), reverse=True):
        count = role_counter.get(role, 0)
        print(f"{role.name}: ({count}/{num_gens}) {calculate_percentage(count, num_gens):.2f}%")

    b_print(f"\nNeutralApoc: ({na_count/num_gens:.2f}/{role_len}) {calculate_percentage(na_count, total_count):.2f}%")
    for role in sorted(RoleBuckets.APOCALYPSE_ROLES, key=lambda r: role_counter.get(r, 0), reverse=True):
        count = role_counter.get(role, 0)
        print(f"{role.name}: ({count}/{num_gens}) {calculate_percentage(count, num_gens):.2f}%")

    b_print(f"\nNeutralKill: ({nk_count/num_gens:.2f}/{role_len}) {calculate_percentage(nk_count, total_count):.2f}%")
    neutral_killing_roles = RoleBuckets.NeutralKilling.expand_possible_roles()
    for role in sorted(neutral_killing_roles, key=lambda r: role_counter.get(r, 0), reverse=True):
        count = role_counter.get(role, 0)
        print(f"{role.name}: ({count}/{num_gens}) {calculate_percentage(count, num_gens):.2f}%")

    b_print(f"\nNeutralEvil: ({ne_count/num_gens:.2f}/{role_len}) {calculate_percentage(ne_count, total_count):.2f}%")
    neutral_evil_roles = RoleBuckets.NeutralEvil.expand_possible_roles()
    for role in sorted(neutral_evil_roles, key=lambda r: role_counter.get(r, 0), reverse=True):
        count = role_counter.get(role, 0)
        print(f"{role.name}: ({count}/{num_gens}) {calculate_percentage(count, num_gens):.2f}%")


if __name__ == '__main__':
    multiprocessing.set_start_method('spawn')
    main()
