import asyncio
import psycopg2
from threading import Timer
import ib_insync
from ib_insync import *
import time as time_

ib = IB()
ib.connect('127.0.0.1', 7497, clientId=18)

print("connecting, running console logs")

ib_insync.util.logToConsole(level=20)

conn = psycopg2.connect("dbname='ordersdb' user='postgres' host='localhost' password='pgpass'")
cur = conn.cursor()

def insert_order(order_id,order_type, order_filled=False):
    """ insert a new vendor into the vendors table """
    sql = """INSERT INTO orders
             VALUES(%s,%s,%s) RETURNING order_id;"""
    # conn = None
    try:
        # read database configuration
        # params = config()
        # connect to the PostgreSQL database
        # pull variables eventually from a config file
        # create a new cursor
        # execute the INSERT statement
        cur.execute(sql, (order_id,order_type,order_filled,))
        # get the generated id back
        order_id = cur.fetchone()[0]
        # commit the changes to the database
        conn.commit()
        print("Added order to database | %s" % (sql))
        # close communication with the database
        # cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    # finally:
        # if conn is not None:
       # conn.close()

    return order_id



# ***************************************************
# ***************************************************
# ***************************************************

def update_order(order_id,order_type):
    """ insert a new vendor into the vendors table """
    sql = """UPDATE orders SET order_type = (%s) WHERE order_id =(%s);"""

    # sql = """INSERT INTO orders
    #          VALUES(%s,%s,%s) RETURNING order_id;"""
    # conn = None
    try:
        # read database configuration
        # params = config()
        # connect to the PostgreSQL database
        # pull variables eventually from a config file
        # create a new cursor
        # execute the INSERT statement
        cur.execute(sql, (order_type, order_id,))
        # get the generated id back
        # order_id = cur.fetchone()[0]
        # commit the changes to the database
        conn.commit()
        print("Order - %s - Updated to to database | %s" % (order_id, order_type,))
        # close communication with the database
        # cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    # finally:
        # if conn is not None:
       # conn.close()

    return order_id




# ***************************************************
# ***************************************************
# ***************************************************




def buy(date,exchange,order_id):

    contractFuture = Future('CAD',date,exchange)

    print("Completing order %s | %s | %s ..." % (date, exchange,order_id))
    print("Inserting into Database")

    print("\n updateing order")
    update_order(order_id,'BUYTESTPOSTED')
    print("\n\n order updated")

    ib.qualifyContracts(contractFuture)


    order               = Order()
    order.action        = 'BUY'
    order.totalQuantity =  1
    order.orderType     = 'LMT'
    order.lmtPrice      = 5.00

    placedOrder = ib.placeOrder(contractFuture, order)
    placedOrder

    ib.sleep(4)






def order_gen(date, exchange):
    order_id = int(round(time_.time()))
    insert_order(order_id,'BUYTEST')l
    order = buy(date,exchange,order_id)
    print("order_gen running %s | %s | %s" % (date, exchange, order_id))
    print(order)

x = range(2)
for n in x:
    print("\no Running order %s" %  (n))
    order_gen('20190514','GLOBEX')
    ib.sleep(5)

while true


print("sleep over")
