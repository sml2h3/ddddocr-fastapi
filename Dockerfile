FROM python:3.10-slim-buster

RUN mkdir /app

COPY ./*.txt ./*.py ./*.sh ./*.onnx /app/

RUN cd /app \
    && python3 -m pip install -U pip\
    && pip3 install --no-cache-dir -r requirements.txt \
    && rm -rf /tmp/* && rm -rf /root/.cache/* \
    && apt-get --allow-releaseinfo-change update && apt install libgl1-mesa-glx libglib2.0-0 -y

WORKDIR /app

CMD ["python3", "ocr_server.py", "--port", "9898", "--ocr"]
