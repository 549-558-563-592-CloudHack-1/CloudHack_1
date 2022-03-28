
FROM python:3.6-slim

RUN apt-get update
ADD /app /app
WORKDIR /app

RUN pip install -r requirements.txt 

EXPOSE 5001
CMD ["python3", "records.py"]
CMD ["python3", "app.py"]