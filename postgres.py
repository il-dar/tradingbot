import psycopg2
from threading import Timer
from time import sleep
import random
import time as time_
import asyncio
import ib_insync
from ib_insync import * # PENDING can minimize the imports based on what we will need
# from cadFutures import buyCADfutureLMT, sellCADfutureLMT

ib = IB()
ib.connect('127.0.0.1', 7497, clientId=13)

print("connecting")
# commands = (
#    """
#    CREATE TABLE completed (
#             order_id SERIAL PRIMARY KEY,
#             order_type VARCHAR(255) NOT NULL,
#             order_source VARCHAR(255) NOT NULL
#             )
#     """,
#     """
#     CREATE TABLE orders (
#         order_id SERIAL PRIMARY KEY,
#         order_type VARCHAR(255) NOT NULL,
#         order_filled BOOLEAN NOT NULL
#     )
#     """)
#
# try:
#     # conn = None
#     conn = psycopg2.connect("dbname='ordersdb' user='postgres' host='localhost' password='pgpass'")
# except:
#     print ("I am unable to connect to the database")
# print("Connected")
#
# try:
#     cur = conn.cursor()
#     # cur.execute("""CREATE TABLE role(role_id serial PRIMARY KEY,role_name VARCHAR (255) UNIQUE NOT NULL)""")
#     for command in commands:
#         if command != "":
#             cur.execute(command)
#     # print(cur.execute("""\l"""))
#     cur.close()
#     conn.commit()
# except (Exception, psycopg2.DatabaseError) as error:
#     print(error)
# finally:
#     if conn is not None:
#         conn.close()
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
        # close communication with the database
        # cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    # finally:
        # if conn is not None:
       # conn.close()

    return order_id

async def sellCADfutureLMT(date,exchange,order_id):
    # print("running trade")
    # await asyncio.sleep(1)
    # sql = """UPDATE orders SET order_type = 'SELL PENDING' WHERE order_id =(%s);"""
    # print("sql trying")
    # # conn = None
    # try:
    #     # read database configuration
    #     # params = config()
    #     # connect to the PostgreSQL database
    #     # pull variables eventually from a config file
    #     # conn = psycopg2.connect("dbname='ordersdb' user='postgres' host='localhost' password='pgpass'")
    #     # create a new cursor
    #     # cur = conn.cursor()
    #     # execute the INSERT statement
    #     print("try execute")
    #     cur.execute(sql, (order_id,))
    #
    #     # get the generated id back
    #     # order_id = cur.fetchone()[0]
    #     # commit the changes to the database
    #     conn.commit()
    #
    #     # close communication with the database
    #     # cur.close()
    # except (Exception, psycopg2.DatabaseError) as error:
    #     print(error,"error Printed")
    # # finally:
    #     # if conn is not None:
    #         # conn.close()
    # return None
    #
    #
    # # contractFuture = Contract('CAD','20190514','GLOBEX')
    # contractFuture = Contract('CAD',date,exchange)
    #
    # ib.qualifyContracts(contractFuture)
    #
    #
    # order               = Order()
    # order.action        = 'BUY'
    # order.totalQuantity =  1
    # order.orderType     = 'LMT'
    # order.lmtPrice      = 10.00
    #
    # placedOrder = ib.placeOrder(contractFuture, order)
    #
    # ib.sleep(4)
    #
    # return order_id

async def orderGenerator():
    # randInt = random.randint(1,101)
    #
    # if (randInt > 50):
    #     order_id = int(round(time_.time()))
    #     print("BUY:",order_id)
    #     insert_order(order_id,"BUY")
    # elif (randInt < 50):
    #     order_id = int(round(time_.time()))
    #     print("SELL:",order_id)
    #     insert_order(order_id,"SELLY")

    # print(int(round(time_.time() * 1000)), randInt)
    order_id = int(round(time_.time()))
    await asyncio.sleep(1.0)


    await sellCADfutureLMT('20190514','GLOBEX',order_id)


    # t = Timer(3,orderGenerator)
    # t.start()
    # print(orderx.result())

# t = Timer(3, orderGenerator)
#
# t.start()

# order = orderGenerator()
# print(await order)

loop = asyncio.get_event_loop()
loop.run_until_complete(orderGenerator())
loop.close()
