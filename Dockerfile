FROM orchardup/python:2.7
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
WORKDIR /code/webapi
RUN ./manage.py syncdb --noinput
RUN ./manage.py migrate
WORKDIR /code
