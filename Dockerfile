FROM python:3.12-slim

WORKDIR /app

COPY . /app

RUN pip install --no--chache--dir -r requirements.txt

EXPOSE 5000

CMD ["python","app.py"]