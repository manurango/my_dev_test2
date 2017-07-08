from stompest.config import StompConfig
from stompest.protocol import StompSpec
from stompest.sync import Stomp
#the consumer connects to apacheMQ via
#the consumer script produces output on python shell acknowledging that it has recived
#the messages sent by the producer

CONFIG = StompConfig('tcp://localhost:61613')
QUEUE = '/queue/test'

if __name__ == '__main__':
    client = Stomp(CONFIG)
    client.connect()
    client.subscribe(QUEUE, {StompSpec.ACK_HEADER: StompSpec.ACK_CLIENT_INDIVIDUAL})
    while True:
        frame = client.receiveFrame()
        print('Got %s' % frame.info())
        client.ack(frame)
    client.disconnect()
