import requests
from dotenv import load_dotenv

load_dotenv()


class YandexAPIClient:
    BASE_YANDEX_DISK_URL = 'https://cloud-api.yandex.net/v1/disk'

    def __init__(self, token_ya, folder):
        self.token_ya = token_ya
        self.folder = folder
        self.headers = {'Content-Type': 'application/json',
                        'Accept': 'application/json',
                        'Authorization': 'OAuth ' + self.token_ya}
        self.params = {'path': self.folder}
        self.folder_url = '/resources'
        self.upload_url = '/resources/upload'

    def get_folder_yandex_disk(self):
        response = requests.get(self.BASE_YANDEX_DISK_URL + self.folder_url,
                                params=self.params, headers=self.headers)
        return response.status_code
