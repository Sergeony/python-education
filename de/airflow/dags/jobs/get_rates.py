from datetime import datetime
from os import getenv
from json import dumps

from boto3 import session
import requests


services = {
  'bitfinex': 'https://api.bitfinex.com/v1/trades/btcusd?limit_trades=500',
  'bitmex': 'https://www.bitmex.com/api/v1/trade?symbol=XBTUSD&count=500&reverse=true',
  'poloniex': 'https://poloniex.com/public?command=returnTradeHistory&currencyPair=USDT_BTC',
}

s3 = session.Session().resource(service_name="s3",
                                endpoint_url="http://s3:9000",
                                aws_access_key_id=getenv("MINIO_ROOT_USER"),
                                aws_secret_access_key=getenv("MINIO_ROOT_PASSWORD"))


def load_to_bucket(exchanger_title: str):
    response = requests.get(services[exchanger_title])
    data = bytes(dumps(response.json()), encoding="utf-8")

    if not s3.Bucket(exchanger_title) in s3.buckets.all():
        s3.create_bucket(Bucket=exchanger_title)

    s3.Bucket(exchanger_title).put_object(Key=f'batch-{datetime.now()}.json',
                                          Body=data)


def main():
    for service in services:
        load_to_bucket(service)


if __name__ == "__main__":
    main()
