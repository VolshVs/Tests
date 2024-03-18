import os
from unittest import TestCase, skipIf

from task_2_API import YandexAPIClient


class TestAPIYandex(TestCase):

    @skipIf(YandexAPIClient(
        os.getenv('TOKEN_YANDEX_DISK'),
        os.getenv('NEW_FOLDER')
    ).get_folder_yandex_disk() == 404, "Исключение. "
                                       "Запрошенная папка отсутствует.")
    def test_get_200(self):
        self.self_ = YandexAPIClient(
            os.getenv('TOKEN_YANDEX_DISK'),
            os.getenv('NEW_FOLDER')
        )
        status = 200
        response = self.self_.get_folder_yandex_disk()
        self.assertEqual(response, status)
