import os

import task_1_test_1
import task_1_test_2
import task_1_test_3
import task_2_API

if __name__ == '__main__':
    task_1_test_1.get_count_names()
    task_1_test_2.get_sorted_courses()
    task_1_test_3.get_unique_names()
    yandex_client = task_2_API.YandexAPIClient(os.getenv('TOKEN_YANDEX_DISK'),
                                               os.getenv('NEW_FOLDER'))
    yandex_client.get_folder_yandex_disk()
