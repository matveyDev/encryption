from fastapi import APIRouter, Response

from logic import EncryptorBase

router = APIRouter()
encryptor = EncryptorBase()


@router.post('/upload-encrypted-data', status_code=201)
async def upload_encrypted_data() -> list[str]:
    data = await encryptor._get_encrypted_data()
    encryptor.upload_encrypted_data(data)

    return data


@router.post('/upload-decrypted-data', status_code=201)
async def upload_decrypted_data() -> list[str]:
    encrypted_data = await encryptor._get_encrypted_data()
    decrypted_data = await encryptor._get_decrypted_data(encrypted_data)
    encryptor.upload_decrypted_data(encrypted_data, decrypted_data)

    return decrypted_data


@router.post('/send-result', status_code=202)
async def send_result() -> None:
    encryptor.send_result()

    return Response(status_code=202)
