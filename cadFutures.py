import ib_insync
from ib_insync import * # PENDING can minimize the imports based on what we will need
import psycopg2

ib = IB()
ib.connect('127.0.0.1', 7497, clientId=14)


def buyCADfutureLMT(month,exchange):
    # contractFuture = Contract('CAD','20190514','GLOBEX')
    contractFuture = Contract('CAD',month,exchange)

    ib.qualifyContracts(contractFuture)


    order               = Order()
    order.action        = 'BUY'
    order.totalQuantity =  1
    order.orderType     = 'LMT'
    order.lmtPrice      = 10.00

    placedOrder = ib.placeOrder(contractFuture, order)


def sellCADfutureLMT(date,exchange,order_id):

    sql = """UPDATE orders SET order_type = 'BUY PENDING' WHERE order_id =(%s);"""
    conn = None
    try:
        # read database configuration
        # params = config()
        # connect to the PostgreSQL database
        # pull variables eventually from a config file
        conn = psycopg2.connect("dbname='ordersdb' user='postgres' host='localhost' password='pgpass'")
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (order_id,))
        # get the generated id back
        order_id = cur.fetchone()[0]
        # commit the changes to the database
        conn.commit()

        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


    # contractFuture = Contract('CAD','20190514','GLOBEX')
    contractFuture = Contract('CAD',date,exchange)

    ib.qualifyContracts(contractFuture)


    order               = Order()
    order.action        = 'SELL'
    order.totalQuantity =  1
    order.orderType     = 'LMT'
    order.lmtPrice      = 10.00

    placedOrder = ib.placeOrder(contractFuture, order)

    return order_id
