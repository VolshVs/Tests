def get_data(word):
    if word == 'courses':
        courses = ["Python-разработчик с нуля", "Java-разработчик с нуля", "Fullstack-разработчик на Python",
                   "Frontend-разработчик с нуля"]
        return courses
    elif word == 'mentors':
        mentors = [
            ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев",
             "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина",
             "Азамат Искаков", "Роман Гордиенко"],
            ["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев",
             "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев",
             "Никита Шумский", "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков",
             "Максим Воронцов", "Евгений Грязнов", "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
            ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский",
             "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая",
             "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
            ["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин",
             "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин",
             "Михаил Ларченко"]
        ]
        return mentors


def get_count_names():
    all_list = []
    for m in get_data('mentors'):
        all_list.extend(m)

    all_names_list = []
    for mentor in all_list:
        name = mentor.split(' ')
        all_names_list.extend(name[0::2])

    unique_names = sorted(set(all_names_list))

    popular = []
    for name in unique_names:
        popular.append([name, all_names_list.count(name)])
    popular.sort(key=lambda x: x[1], reverse=True)
    top_3 = popular[0:3]
    text = f'Задание 1. {top_3[0][0]}: {top_3[0][1]} раз(а), ' \
           f'{top_3[1][0]}: {top_3[1][1]} раз(а), ' \
           f'{top_3[2][0]}: {top_3[2][1]} раз(а)'

    return text
