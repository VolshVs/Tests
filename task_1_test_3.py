from task_1_test_1 import get_data


def get_unique_names():
    all_list = []
    for m in get_data('mentors'):
        all_list.extend(m)

    all_names_list = []
    for mentor in all_list:
        name = mentor.split(' ')
        all_names_list.extend(name[0::2])

    unique_names = set(all_names_list)

    all_names_sorted = sorted(unique_names)
    all_names_string = ', '.join(all_names_sorted)
    text = f'Тест 3. Уникальные имена преподавателей: {all_names_string}'

    return text
