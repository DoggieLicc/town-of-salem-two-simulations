from utils.presets_rolelists import AllAny, Classic, Ranked_Practice
from utils.classes import check_list_for_opposing_factions

from utils import build_list, print_rolelist

MAX_TRIES = 100


def main():
    role_lists = [AllAny, Classic, Ranked_Practice]

    print('Available rolelists: ' + ', '.join([f"'{rl.name}'" for rl in role_lists]))

    while True:
        rolelist_str = input('Type in a rolelist to simulate (or enter "Custom" to make your own): ')

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
        print('Checking list for opposing factions!\n')

    for _ in range(MAX_TRIES):
        generated_roles = rolelist.generate_roles()

        if not check_opposing_facs:
            break

        if check_list_for_opposing_factions(generated_roles):
            break
    else:
        raise Exception('Unable to generate valid list!')

    print('\nGenerated Roles:')
    print_rolelist(sorted(generated_roles, key=lambda r: r.name))


if __name__ == '__main__':
    main()
