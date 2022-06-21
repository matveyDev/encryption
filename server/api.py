from fastapi import APIRouter

from logic import EncryptorUploader, EncryptorAPI

router = APIRouter()
uploader = EncryptorUploader()
API = EncryptorAPI()


@router.get('/upload-encrypted-data', status_code=201)
async def upload_encrypted_data() -> list[str]:
    data = await API._get_encrypted_data()
    uploader.upload_encrypted_data(data)

    return data


@router.post('/upload-decrypted-data', status_code=201)
async def upload_decrypted_data() -> list[str]:
    encrypted_data = await API._get_encrypted_data()
    decrypted_data = await API._get_decrypted_data(encrypted_data)
    uploader.upload_decrypted_data(encrypted_data, decrypted_data)

    return decrypted_data
