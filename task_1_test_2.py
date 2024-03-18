from task_1_test_1 import get_data


def get_sorted_courses():
    mentors_names = []
    for m in get_data('mentors'):
        course_names = []
        for name in m:
            course_names.append(name.split(' ')[0])
        mentors_names.append(course_names)
    pairs = []
    for id1 in range(len(mentors_names)):
        for id2 in range(len(mentors_names)):
            if id1 != id2:
                intersection_set = set(
                    mentors_names[id1]
                ).intersection(
                    set(mentors_names[id2]
                        )
                )
                if len(intersection_set) > 0:
                    pair = [get_data('courses')[id1], get_data('courses')[id2]]
                if [pair[0], pair[1]] not in pairs and [pair[1], pair[0]] not in pairs:
                    pairs.append(pair)
                    all_names_sorted = sorted(intersection_set)
                    c_1 = get_data('courses')[id1]
                    c_2 = get_data('courses')[id2]
                    n = ', '.join(all_names_sorted)
                    text = f"Задание 2. На курсах {c_1} и {c_2} преподают: {n}"
                    return text
