FROM python:3.9
RUN apt-get update -y
RUN apt-get upgrade -y

WORKDIR /src

RUN python -m pip install --upgrade pip
COPY ./requirements.txt ./
RUN pip install -r requirements.txt
COPY ./app ./app

CMD ["python3", "./app/manage.py", "runserver", "0.0.0.0:8000"]