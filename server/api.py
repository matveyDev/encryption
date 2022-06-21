from fastapi import APIRouter, Response

from logic import EncryptorUploader

router = APIRouter()
encryptor = EncryptorUploader()


@router.get('/upload-encrypted-data', status_code=201)
async def upload_encrypted_data() -> list[str]:
    data = encryptor._get_encrypted_data()
    encryptor.upload_database(data)

    return data
