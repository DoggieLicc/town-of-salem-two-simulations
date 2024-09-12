import multiprocessing

import utils.role_buckets
from utils import simple_input
from utils.presets_rolelists import AllAny
from utils.classes import parallel_generate_roles


def main():
    num_gens = simple_input.get_integer_input('Type in the amount of lists to generate (default:10000): ', 10000)

    apoc_roles = utils.role_buckets.APOCALYPSE_ROLES

    print('Generating...')

    results = parallel_generate_roles(AllAny, num_gens=num_gens)

    success_count = sum(1 for rl in results if len([r for r in rl if r in apoc_roles]) == 4)

    print(f'{success_count}/{num_gens} ({(success_count*100 / num_gens): .3f}%)')


if __name__ == '__main__':
    multiprocessing.set_start_method('spawn')
    main()
