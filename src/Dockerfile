FROM python:3.9
RUN apt-get update -y
RUN apt-get upgrade -y

WORKDIR /src

COPY ./requirements.txt ./
RUN pip install -r requirements.txt
COPY ./app ./app
COPY ./run.sh ./run.sh

CMD ["chmod", "777", "run.sh"]