FROM python:3.10.12-slim

WORKDIR /app

COPY docker_requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN python3 -m nltk.downloader stopwords

COPY app.py /app/
COPY preprocessing.py /app/
COPY pipeline.pickle /app

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]