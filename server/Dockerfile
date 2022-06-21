FROM python:3.10.5

WORKDIR /app

COPY . /app

RUN pip3 install -r requirements.txt

RUN chmod u+x ./entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]
