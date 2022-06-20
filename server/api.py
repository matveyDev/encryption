import requests
import json

from fastapi import APIRouter

from settings import API_URL

router = APIRouter()


@router.get('/get-encrypted-data')
async def get_encrypted_data() -> None:
    response = requests.get(API_URL + 'top-secret-data')
    list_response = json.loads(response.text)
