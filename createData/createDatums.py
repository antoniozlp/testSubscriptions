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

def postValialveLoop(varialeCode, rangeValues, frequency, increment):
    value = randint(rangeValues['min'], rangeValues['max'])
    while True:
        print(varialeCode + ': ' + str(value))
        _, errors_userMut = gql.mutate(createDatum, variables={"code": varialeCode,"value":value})
        if(errors_userMut):
            print(errors_userMut)

        if type(increment) == str:
            if increment == 'randint':
                value = randint(rangeValues['min'], rangeValues['max'])
            elif increment == 'randgauss':
                value = gauss(rangeValues['mean'], rangeValues['std'])
        else:    
            value=value+increment
            if(value>rangeValues['max']):
                value=rangeValues['min']
            if(value<rangeValues['min']):
                value=rangeValues['max']
        time.sleep(frequency)

if __name__ == "__main__":
    for variableI in postVaribles:
        threading.Thread(target=postValialveLoop, args=(variableI['varialeCode'], variableI['rangeValues'], variableI['frequency'], variableI['increment'])).start()
        time.sleep(randint(1,5))


