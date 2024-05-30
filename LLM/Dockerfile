# Dockerfile
FROM nvidia/cuda:11.8.0-cudnn8-devel-ubuntu22.04
USER root

RUN apt-get update
RUN apt-get -y install python3 python3-pip vim 
RUN apt-get -y install locales && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm
ENV PYTHONPATH "${PYTHONPATH}:/app"

COPY requirements.txt /root/

RUN apt-get install -y vim less
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools

RUN pip install -r /root/requirements.txt

COPY ./app /app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
