import os
import time
from pygqlc import GraphQLClient 
import threading
from mutations_queries import createDatum, updateVariableState, createVariableState, variableStates
from postVariables import postVaribles
from random import randint
from random import gauss
from datetime import datetime

gql = GraphQLClient()
gql.addEnvironment(
    'dev',
    url=os.environ.get('API'), # should be an https url
    wss=os.environ.get('WSS'), # should be an ws/wss url
    headers={'Authorization': os.environ.get('TOKEN')},
    default=True)


def postVarialeState():
    variableState = ['DANGER', 'SUCCESS', 'WARNING']

    data, errors = gql.query_one(variableStates, variables={'variableCode':'Test_RTF'})
    if errors:
        print(errors)
        return

    lastID = data['id']

    while True:
        for varState in variableState:
            dateTimeUTC = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
            __, errors = gql.mutate(updateVariableState, variables={'id':lastID, 'endAt':dateTimeUTC})
            if errors:
                print(errors)
            data, errors = gql.mutate(createVariableState, variables={'variableCode':'Test_RTF', 'startAt':dateTimeUTC, 'state':varState})
            if errors:
                print(errors)
            else:
                lastID = data['result']['id']
                print('Test_RTF state -> ' + varState)
            
            time.sleep(10)

if __name__ == "__main__":
  postVarialeState()
# threading.Thread(target=postVarialeState, args=()).start()

