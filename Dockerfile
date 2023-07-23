FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
python3-pip \
git

RUN git clone https://github.com/SUhlemeyer/docker-playground.git /home/semseg
WORKDIR /home/semseg
RUN git pull
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN gdown --id 1P4kPaMY-SmQ3yPJQTJ7xMGAB_Su-1zTl

CMD ["python3", "main.py"]

