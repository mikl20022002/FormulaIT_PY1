# TODO Напишите функцию find_common_participants
def find_common_participants(group1, group2, devider=','):
    group1 = group1.split(devider)
    group2 = group2.split(devider)

    set1 = set(group1)
    set2 = set(group2)

    same_participants = set1.intersection(set2)
    same_participants = list(same_participants)
    same_participants.sort()

    return same_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, '|'))