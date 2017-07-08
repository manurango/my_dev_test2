# my_dev_test2
Technologies
python 3.4,
sqlite3 db,
Apache activeMQ 5.14, 
and other python libraries for intergration>> pip install>> pandas, json, stompest, csv, json, random

The python aplication creates  a csv file by running create_csv.py, then reads column5 of the generated csv file by running producer_create_db.py connects to both Apache activeMQ and sqlite3 and stores the csv file rows on either or both Apache activeMQ and sqlite3 based on certain conditions of the csv input.
Consumer.py  script produces output on python shell acknowledging that it has recived
the messages sent by the producer.

You can access Apache activeMQ on http://127.0.0.1:8161/admin/ on localhost

 
