import os
import time
from pygqlc import GraphQLClient
import logging
import json
import datetime
# from multiprocessing 
logging.basicConfig(filename='test_suscriptions.log',level=logging.INFO)

gql = GraphQLClient()
gql.addEnvironment(
    'dev',
    url=os.environ.get('API'),  # should be an https url
    wss=os.environ.get('WSS'),  # should be an ws/wss url
    headers={'Authorization': os.environ.get('TOKEN')},
    timeoutWebsocket=35,
    default=True)

subscription_all_variables = """subscription{
  datumCreated{
      result{variable{name} value insertedAt}
  }
}"""

subscription_notifications = """subscription{
  notificationCreated
  {
    successful
    result{title, content}
  }
}"""

last_time_received = time.perf_counter()

def on_datum_created(message):
    global last_time_received
    # logging.info(message)
    last_time_received = time.perf_counter()


def on_notification_created(message):
    global last_time_received
    now = datetime.datetime.now()
    nowS = now.strftime("%Y-%m-%d %H:%M:%S")
    logging.info(f'[{nowS}] {message}')
    print(f'[{nowS}] {message}')
    last_time_received = time.perf_counter()


unsub1 = gql.subscribe(subscription_all_variables,
                      callback=on_datum_created)
unsub2 = gql.subscribe(subscription_notifications,
                      callback=on_notification_created)


def testResetSubsConnection():

  gql.resetSubsConnection()
  time.sleep(10)

  #para provocar un error dentro de _sub_routing_loop
  payload = {'type': 'connection_terminate'}
  gql._conn.send(json.dumps(payload))
  time.sleep(2)

  gql.resetSubsConnection()

def monitor_subscriptions():
  while True:
    elapsed_time = time.perf_counter() - last_time_received
    if elapsed_time > 45:
      now = datetime.datetime.now()
      nowS = now.strftime("%Y-%m-%d %H:%M:%S")
      logging.warning(f'[{nowS}]: No datos Subs, Reintentando conectar ...')
      print(f'[{nowS}]: No datos Subs, Reintentando conectar ...')
      gql.resetSubsConnection()
      time.sleep(15)


if __name__ == "__main__":
  time.sleep(5)
  # testResetSubsConnection()
  now = datetime.datetime.now()
  nowS = now.strftime("%Y-%m-%d %H:%M:%S")
  logging.info(f'[{nowS}]: Program starting ...')
  print(f'[{nowS}]: Program starting ...')
  monitor_subscriptions()