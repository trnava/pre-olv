FROM python:3.6.6

ENV PYTHONUNBUFFERED 1
ENV PY_ENV 'local'

RUN mkdir /code

WORKDIR /code

COPY requirements.txt /code/

RUN apt-get update && apt-get install -y graphviz
RUN pip install -r requirements.txt

COPY . /code/

# ENTRYPOINT ["pyhon"]
# CMD ["manage.py runserver -p 8008"]


