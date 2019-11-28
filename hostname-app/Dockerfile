FROM python:3.8-alpine

ENV FLASK_ENV DEVELOPMENT
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["flask", "run", "--host", "0.0.0.0"]