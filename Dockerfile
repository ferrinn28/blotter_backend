FROM python:3.11-alpine

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 8000

CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "-w", "4", "-b", "0.0.0.0:8000", "src:app", "--access-logfile", "-"]

