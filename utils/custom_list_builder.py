from utils import role_buckets
from utils.classes import RoleList

__all__ = ['build_list', 'print_rolelist']


def print_rolelist(roles: list):
    if not roles:
        return

    for i, role in enumerate(roles):
        print(f'[{i+1}] - {role.name}')


def build_list() -> RoleList:
    roles = []
    banned_roles = []

    available_roles = list(role_buckets.Any.expand_possible_roles())

    available_role_buckets = role_buckets.ROLE_BUCKETS

    while True:
        print_rolelist(roles)

        inp = input('\nEnter the name of a Role or RoleBucket to add, or "list" to list available roles, "next" to move on to the next step, or "delete" to delete an item: ')

        inp = inp.strip().lower()

        if inp == 'list':
            print('Available Roles')
            for role in available_roles:
                print(role.name)

            print('\nAvailable RoleBuckets')
            for rb in available_role_buckets:
                print(rb.name)

            continue

        if inp == 'delete':
            if not roles:
                continue

            del_inp = input('Enter the role number to delete: ')

            if not del_inp.isnumeric() or len(roles) < int(del_inp):
                print('Invalid number!')
                continue

            del roles[int(del_inp)-1]
            continue

        if inp == 'next':
            if len(roles) < 5:
                print("Mininum of 5 roles required")
                continue

            while True:
                print_rolelist(banned_roles)

                inp2 = input('Input a role to ban, or "list", "delete", "back", "finish": ')

                inp2 = inp2.lower().strip()

                if inp2 == 'back':
                    break

                if inp2 == 'list':
                    print('Available Roles')
                    for role in available_roles:
                        print(role.name)
                        continue

                if inp2 == 'delete':
                    if not banned_roles:
                        continue

                    del_inp = input('Enter the role number to delete: ')

                    if not del_inp.isnumeric() or len(banned_roles) < int(del_inp):
                        print('Invalid number!')
                        continue

                    del banned_roles[int(del_inp) - 1]
                    continue

                if inp2 == 'finish':
                    return RoleList(
                        name='Custom',
                        roles=roles,
                        banned_roles=set(banned_roles)
                    )

                banned_role = [r for r in available_roles if inp2 == r.name.lower()]

                if banned_role:
                    banned_role = banned_role[0]

                    if banned_role in roles or banned_role in banned_roles:
                        print('Can\'t ban role already in list!')
                        continue

                    if len(banned_roles) == 3:
                        print('Already at max of 3 roles!')
                        continue

                    banned_roles.append(banned_role)

        added_role = [r for r in (available_roles + available_role_buckets) if inp == r.name.lower()]

        if added_role:
            if len(roles) == 15:
                print('Already at max of 15 roles!')
                continue

            roles.append(added_role[0])


if __name__ == '__main__':
    print(build_list())