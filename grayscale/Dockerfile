FROM python:3.8
MAINTAINER Francesco Fanchin
LABEL version="0.1"

COPY grayscale.py .
ADD download download
ADD upload upload
COPY requirements.txt .
RUN pip install -r requirements.txt
ENTRYPOINT ["python3", "grayscale.py"]