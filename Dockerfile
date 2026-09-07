FROM python:3.12

RUN apt-get update && apt-get install -y --no-install-recommends ffmpeg \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . /app

CMD [ "python3", "doot.py" ]
