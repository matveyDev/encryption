from pydantic import BaseModel


class EncryptedList(BaseModel):
    class Config:
        schema_extra = {
            'example': [
                'm32f3290jf93',
                'f23kf23lfl-54',
                'mio32jm43=g54',
            ]
        }


class DecryptedList(BaseModel):
    class Config:
        schema_extra = {
            'example': [
                'Расшифрованная строка 1',
                'Расшифрованная строка 2',
                'Расшифрованная строка 3',
            ]
        }
