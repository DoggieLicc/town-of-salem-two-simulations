import multiprocessing

import utils.role_buckets
from utils.presets_rolelists import AllAny
from utils.classes import parallel_generate_roles


def main():
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

    print('Generating...')

    results = parallel_generate_roles(AllAny, num_gens=num_gens)

    success_count = sum(1 for rl in results if len([r for r in rl if r in apoc_roles]) == 4)

    print(f'{success_count}/{num_gens} ({(success_count*100 / num_gens): .3f}%)')


if __name__ == '__main__':
    multiprocessing.set_start_method('spawn')
    main()
