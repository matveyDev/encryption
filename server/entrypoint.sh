#!/usr/bin/env bash

sleep 10

export SQLALCHEMY_DATABASE_URL=sqlite:///decryptor.db

alembic revision --autogenerate -m 'first'

alembic upgrade head

python3 main.py
