import utils


if __name__ == '__main__':
    role_lists = [utils.AllAny, utils.Classic]

    print('Available rolelists: ' + ', '.join([f"'{rl.__name__}'" for rl in role_lists]))

    while True:
        rolelist_str = input('Type in a rolelist to simulate.')

        rolelist = [rl for rl in role_lists if rl.__name__.lower() == rolelist_str.lower()]

        if rolelist:
            break

    print(rolelist)
