FROM python:3.11-slim 

WORKDIR / CICD

COPY requirements.txt .

RUN pip install -r requirements.txt  

COPY . .

CMD ["python", "etl.py"]