


def filter_geo_logs(logs:list) -> dict:
    newLogs = []
    for log in logs:
        visit = tuple(log.keys())[0]
        if log[visit][1] == 'Россия':
            newLogs.append(log)
    return newLogs

def get_unique(ids:dict) -> list:
    uniqueList = []
    for user in ids:
        userIds = ids[user]
        for id in userIds:
            if id not in uniqueList:
                uniqueList.append(id)
    return uniqueList


def run_task_1():
    geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
    ]

    filteredLogs = filter_geo_logs(geo_logs)

    return filteredLogs

def run_task_2():
    ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}
    
    uniqueIds = get_unique(ids)

    return uniqueIds

def run_task_3():
    stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}

    topCompany = max(stats, key=stats.get)

    return topCompany