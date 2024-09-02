from utils.presets_rolelists import Ranked_15p, Ranked_12p, Classic_7p, Testing_3p, Taa_2p
from utils.classes import check_list_for_opposing_factions, Player

from utils import build_list, print_rolelist, RoleBucket, Role, RoleList
from utils import role_buckets
from utils import simple_input

import random

from utils.simple_input import get_boolean_input

MAX_TRIES = 100
SCROLLABLE_ROLES = list(role_buckets.Any.expand_possible_roles())
SCROLLABLE_SUBALIGNMENTS = [
    role_buckets.RandomTown,
    role_buckets.TownPower,
    role_buckets.TownKilling,
    role_buckets.TownInvestigative,
    role_buckets.TownProtective,
    role_buckets.RandomCoven,
    role_buckets.CovenKilling,
    role_buckets.CovenPower,
    role_buckets.CovenUtility,
    role_buckets.CovenDeception,
    role_buckets.RandomNeutral,
    role_buckets.NeutralApocalypse,
    role_buckets.NeutralPariah,
    role_buckets.NeutralKilling,
    role_buckets.NeutralEvil
]

SCROLLABLE_ITEMS = SCROLLABLE_ROLES + SCROLLABLE_SUBALIGNMENTS


def generate_lots(player, roles) -> list[int]:
    lots: list[int] = []
    blessed_scrolls = player.blessed_scrolls
    cursed_scrolls = player.cursed_scrolls

    for role in roles:
        lots_num = 10

        for blessed_scroll in blessed_scrolls:
            if isinstance(blessed_scroll, RoleBucket):
                if role in blessed_scroll.expand_possible_roles():
                    lots_num += 90
            else:
                if blessed_scroll == role:
                    lots_num += 190

        for cursed_scroll in cursed_scrolls:
            if cursed_scroll == role:
                lots_num = 1

        lots.append(lots_num)

    return lots

def assign_players_to_roles(players: list[Player], roles: list[Role]):
    random.shuffle(players)
    random.shuffle(roles)

    assigned_players = []

    for player in players:
        role_lots = generate_lots(player, roles)

        chosen_role = random.choices(roles, weights=role_lots)[0]
        player.assigned_role = chosen_role
        roles.remove(chosen_role)

        assigned_players.append(player)

#    assigned_players: dict[str, Role] = {}
#    all_player_lots = {p.name: generate_lots(p, roles) for p in players}

#    for role in roles:
#        player_names = [p.name for p in players]
#        weights = [lots[1][role] for lots in all_player_lots.items() if lots[0] in player_names]
#        chosen_player = random.choices(players, weights=weights)[0]
#
#        players.remove(chosen_player)
#        assigned_players[chosen_player.name] = role

    random.shuffle(assigned_players)

    return assigned_players

def select_rolelist() -> RoleList:
    role_lists = [Ranked_12p, Ranked_15p, Classic_7p, Testing_3p, Taa_2p]
    print('Available rolelists: ' + ', '.join([f"'{rl.name}'" for rl in role_lists]))

    while True:
        rolelist_str = simple_input.get_string_input('Type in a rolelist to simulate (or enter "Custom" to make your own): ')

        if rolelist_str.lower().strip() == 'custom':
            rolelist = build_list()
            break

        rolelist = [rl for rl in role_lists if rl.name.lower() == rolelist_str.lower().strip("' \"")]

        if rolelist:
            rolelist = rolelist[0]
            break

    print(f'You selected: {rolelist.name}')

    print('\n'.join([f'  {r.name}' for r in rolelist.roles]))
    return rolelist

def select_players(max_players: int, add_scrolls: bool) -> list[Player]:
    players = []

    while len(players) < max_players:
        player_name = simple_input.get_string_input(f'Input player\'s {len(players) + 1} name: ',
                                                    f'Player #{len(players) + 1}')
        player_blessed_scrolls: list[Role | RoleBucket] = []
        player_cursed_scrolls: list[Role] = []

        if add_scrolls:
            while len(player_blessed_scrolls) < 5:
                player_scroll_str = simple_input.get_string_input(
                    f'Input player\'s {len(players) + 1} blessed scroll #{len(player_blessed_scrolls) + 1}: ')

                if player_scroll_str.lower() == 'break':
                    break

                valid_role = [r for r in SCROLLABLE_ITEMS if r.name.lower() == player_scroll_str.lower()]

                if valid_role:
                    if valid_role in player_blessed_scrolls:
                        continue

                    player_blessed_scrolls.append(valid_role[0])

            while len(player_cursed_scrolls) < 5:
                player_scroll_str = simple_input.get_string_input(
                    f'Input player\'s {len(players) + 1} cursed scroll #{len(player_cursed_scrolls) + 1}: ')

                if player_scroll_str.lower() == 'break':
                    break

                valid_role = [r for r in SCROLLABLE_ROLES if r.name.lower() == player_scroll_str.lower()]

                if valid_role:
                    if valid_role in player_cursed_scrolls:
                        continue

                    player_cursed_scrolls.append(valid_role[0])

        new_player = Player(
            name=player_name,
            blessed_scrolls=player_blessed_scrolls,
            cursed_scrolls=player_cursed_scrolls
        )

        players.append(new_player)

    return players

def generate_list(rolelist: RoleList, check_opposing_facs : bool) -> list[Role]:
    if check_opposing_facs:
        print('Checking list for opposing factions!\n')

    for _ in range(MAX_TRIES):
        generated_roles = rolelist.generate_roles()

        if not check_opposing_facs:
            return generated_roles

        if check_list_for_opposing_factions(generated_roles):
            return generated_roles

    else:
        raise Exception('Unable to generate valid list!')

def main():
    players = []
    rolelist = select_rolelist()
    check_opposing_facs = get_boolean_input('Check generated lists for opposing factions? (y/N): ', False)

    add_players = get_boolean_input('Add players?: ')

    if add_players:
        add_scrolls = get_boolean_input('Add scrolls?: ')
        players = select_players(len(rolelist.roles), add_scrolls)

    generated_roles = generate_list(rolelist, check_opposing_facs)

    print('\nGenerated Roles:')
    print_rolelist(generated_roles)

    if add_players:
        assigned_players = assign_players_to_roles(players, generated_roles)

        print('\nAssigned roles:')
        for i, player in enumerate(assigned_players):
            print(f'[{i+1}] - {player.name} ({player.assigned_role.name})')


if __name__ == '__main__':
    main()
