from models.models import users, base_user_info

def get_statistics_text(user_id: int, text: str) -> str | bool:
    if User.in_data(user_id):
        return text.replace('wins', str(users[user_id]['wins'])).replace('total_games',
                                                                         str(users[user_id]['total_games']))
    else:
        return 'Ошибка! Пользователя не существует'


class User:
    def add(user_id: int, first_name) -> None:
        if user_id not in users:
            users[user_id] = dict.copy(base_user_info)
            users[user_id]['nickname'] = first_name

    def in_data(user_id: int) -> bool:
        return user_id in users

    def change_nick_status(user_id: int) -> None:
        users[user_id]['change_nick'] = not users[user_id]['change_nick']
