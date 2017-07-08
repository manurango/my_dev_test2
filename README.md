# my_dev_test2
Technologies
1. python 3.4
2.sqlite3 db
3 Apache activeMQ 5.14
4.and other python libraries for intergration>> pip install>> pandas, json, stompest, csv, json, random

The python aplication creates  a csv file by running create_csv.py, then reads column5 of the generated csv file by running producer_create_db.py connects to both Apache activeMQ and sqlite3 on certain conditions based on the csv input.
Consumer.py  script produces output on python shell acknowledging that it has recived
the messages sent by the producer.

You can access Apache activeMQ on http://127.0.0.1:8161/admin/ on localhost

 
