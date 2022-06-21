import requests
import json

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from core.models import Encryption
from core.database.db import SQLALCHEMY_DATABASE_URL
from settings import API_URL


# ToDo: think about right separate classes
class EncryptorAPI:

    def __init__(self) -> None:
        self.url_encrypted_data = API_URL + 'top-secret-data'

    def _get_encrypted_data(self) -> list[str]:
        response = requests.get(self.url_encrypted_data)
        encrypted_data = json.loads(response.text)
        return encrypted_data


class EncryptorUploader(EncryptorAPI):

    def __init__(self) -> None:
        super().__init__()
        engine = create_engine(SQLALCHEMY_DATABASE_URL)
        self.session = Session(engine)

    def upload_database(self, data: list[str]) -> None:
        objects_create = []
        for text in range(len(data)):
            objects_create.append(
                Encryption(encrypted_text=text)
            )

        self.session.bulk_save_objects(objects_create)
        self.session.commit()
