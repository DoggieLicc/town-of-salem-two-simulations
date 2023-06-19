import utils.role_buckets
from utils.presets_rolelists import AllAny


if __name__ == '__main__':

    while True:
        num_gens_str = input('Type in the amount of lists to generate: (default:1000): ')
        num_gens = None

        if not num_gens_str:
            num_gens = 1000

        else:
            if num_gens_str.isnumeric():
                num_gens = int(num_gens_str)

        if num_gens:
            break

    apoc_roles = utils.role_buckets.APOCALYPSE_ROLES

    success_count = 0

    print('Generating...')

    for i in range(num_gens):

        roles = AllAny.generate_roles()

        apocs = [r for r in roles if r in apoc_roles]

        if len(apocs) == 4:
            success_count += 1

        if i % 1000 == 0:
            print(f'generated {i}/{num_gens}')

    print(f'{success_count}/{num_gens} ({(success_count / num_gens): .3f}%)')
