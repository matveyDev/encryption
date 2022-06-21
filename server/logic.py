import json

from base64 import b64encode
import requests

from sqlalchemy import create_engine, update, select
from sqlalchemy.orm import Session

from core.database.db import SQLALCHEMY_DATABASE_URL
from core.models import Encryption
from settings import API_URL


class EncryptorAPI:

    def __init__(self) -> None:
        self.url_encrypted_data = API_URL + 'top-secret-data'
        self.url_decrypt_data = API_URL + 'decrypt'

    async def _get_encrypted_data(self) -> list[str]:
        response = requests.get(url=self.url_encrypted_data)
        encrypted_data = json.loads(response.text)
        return encrypted_data

    async def _get_decrypted_data(self, encrypted_data: list[str]) -> list[str]:
        json_data = json.dumps(encrypted_data)
        auth = b64encode(b'qummy:GiVEmYsecReT!').decode('ascii')
        headers = {
            'Authorization': f'Basic {auth}'
        }
        response = requests.post(
            url=self.url_decrypt_data,
            data=json_data,
            headers=headers
        )
        encrypted_data = json.loads(response.text)
        return encrypted_data


class EncryptorUploader:

    def __init__(self) -> None:
        engine = create_engine(SQLALCHEMY_DATABASE_URL)
        self.session = Session(engine)

    def upload_encrypted_data(self, data: list[str]) -> None:
        objects_to_create = []
        for text in data:
            objects_to_create.append(
                Encryption(encrypted_text=text)
            )

        self.session.bulk_save_objects(objects_to_create)
        self.session.commit()

    def upload_decrypted_data(
            self,
            encrypted_data: list[str],
            decrypted_data: list[str]
        ) -> None:
        objects_to_update = []
        for en_string, de_string in zip(encrypted_data, decrypted_data):
            objects_to_update.append({
                'encrypted_text': en_string,
                'decrypted_text': de_string,
            })
            query = (
                update(Encryption).
                values(decrypted_text = de_string).
                where(Encryption.encrypted_text == en_string)
            )
            self.session.execute(query)
            self.session.commit()
