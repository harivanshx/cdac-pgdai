
FROM python:3.13-slim


COPY requirements.txt .

RUN pip install -r requirements.txt


EXPOSE 5000

COPY . .

CMD ["python", "harivansh.py"]

