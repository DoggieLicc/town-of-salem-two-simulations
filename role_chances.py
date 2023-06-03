from utils.presets_rolelists import AllAny, Classic
from collections import Counter


if __name__ == '__main__':
    role_lists = [AllAny, Classic]

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
    for _ in range(num_gens):
        roles = rolelist.generate_roles()
        unique_roles = set(roles)
        role_counter.update(unique_roles)

    print(role_counter)
