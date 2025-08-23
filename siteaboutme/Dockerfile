FROM python:3.13.5-slim
RUN groupadd -r groupflask && useradd -r -g groupflask userflask

RUN pip install --upgrade pip
WORKDIR /app/www/easysite-docker
COPY requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 4000

COPY . .
USER userflask

CMD ["python", "main.py"]