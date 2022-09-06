FROM python:3

RUN apt-get update && apt-get -y install cron vim

WORKDIR /app

COPY crontab /etc/cron.d/crontab

COPY download_prices.py /app/download_prices.py

COPY Stock_Prices.py /app/Stock_Prices.py

COPY requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

RUN chmod 0644 /etc/cron.d/crontab

RUN /usr/bin/crontab /etc/cron.d/crontab

CMD ["cron", "-f"]
