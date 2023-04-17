FROM python:3.9.15-slim as builder
RUN apt-get update && \
    apt-get install -y gcc
ADD requirements.txt  ./
RUN mkdir -p /install
RUN pip3 install --prefix=/install -r requirements.txt

FROM python:3.9.15-slim
COPY --from=builder /install /usr/local
RUN mkdir -p /app
WORKDIR /app
ADD . /app

RUN mkdir tmpfs

RUN python3 -m venv /env
RUN . /env/bin/activate
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

CMD gunicorn --workers 4 --max-requests 1000 \
    --timeout 240 --bind :8000 --capture-output \
    --error-logfile - --log-file - \
    --worker-tmp-dir ./tmpfs/  main:app
