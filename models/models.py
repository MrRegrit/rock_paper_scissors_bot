users: dict[int, dict] = {}

base_user_info: dict = {
    'change_nick': False,
    'game_status': False,
    'nickname': None,
    'total_games': 0,
    'wins': 0,
    'search_status': False,
    'enemy_id': None,
    'move': 0,
    'score': 0,
}

queue: list[int] = []



