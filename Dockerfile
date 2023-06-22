FROM python:3.10.12-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app.py /app/app.py

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]