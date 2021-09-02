FROM python:3

WORKDIR /app

VOLUME ./app /app

RUN pip install Flask
RUN pip install -r requirements.txt

CMD ["python", "index.py"]

