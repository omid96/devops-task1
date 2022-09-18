FROM python:3.10.4-slim-buster

WORKDIR /

# ENVs

# Install dependencies
RUN pip install -U pip
COPY ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt

COPY . /

EXPOSE 8000

CMD ["gunicorn"  , "-b", "0.0.0.0:8000", "task1:create_app()"]
