users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

dict = {'Общее количество':0,
        'Уникальные посещения':0}

dict['Общее количество'] = len(users)
dict['Уникальные посещения'] = len(set(users))
print(dict)