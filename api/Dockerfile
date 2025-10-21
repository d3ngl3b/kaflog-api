FROM python:3.12.6-slim-bookworm
WORKDIR /usr/src/api
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]