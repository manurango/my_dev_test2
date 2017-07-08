import pandas as pd
import sqlite3
from stompest.config import StompConfig
from stompest.sync import Stomp
import json

fields = ['id', 'num5']
df = pd.read_csv('tests.csv', skipinitialspace=True, usecols=fields)
x = df.name.values
q = str(x)
if 'C' or 'G' in q:
    conn = sqlite3.connect("test.sqlite")
    conn.execute("CREATE TABLE if not exists Data (id TEXT, col5 TEXT)")
    df = pd.read_csv("tests.csv")
    df.to_sql("Data", conn, if_exists='append', index=False)

elif 'A' and 'T'in q:
    CONFIG = StompConfig('tcp://localhost:61613')
    QUEUE = '/queue/test'
    if __name__ == '__main__':
        
        client = Stomp(CONFIG)
        client.connect()
        #client.send(QUEUE, json.dumps{(q)}.encode())
        client.send(QUEUE, q.encode())
        #client.send(QUEUE, 'test  2'.encode())
        client.disconnect()
          
else:
    print ('No matches found')
