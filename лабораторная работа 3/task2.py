def find_common_participants(str1, str2, delimiter=","):
    first_group = set(str1.split(delimiter))
    second_group = set(str2.split(delimiter))
    common = list(second_group.intersection(first_group))
    common.sort()
    return common

participants_first_group = "Иванов|Петров|Сидоров"

participants_second_group = "Петров|Сидоров|Смирнов"

participants = find_common_participants(participants_first_group, participants_second_group)
print("Общие участники:", participants)

