FROM python:3.12.6-slim-bookworm
WORKDIR /usr/src/appender
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

CMD ["python", "-m", "app.main"]