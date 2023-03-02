FROM tiangolo/uwsgi-nginx:python3.10

COPY requirements.txt /app/requirements.txt

RUN pip install --upgrade pip

RUN pip install --no-cache-dir --upgrade -r /step/requirements.txt

COPY ./step /step
