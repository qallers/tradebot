import time
import datetime
import MetaTrader4 as mt4
import forex_python.converter as conv
from forex_python.converter import CurrencyRates
from forex_python.bitcoin import BtcConverter

# Connect to MetaTrader 4
if not mt4.initialize():
    print("initialize failed")
    quit()

# Get the current time in UTC
now = datetime.datetime.utcnow()

# Get the economic calendar for the current week
cal = mt4.request_calendar(now.year, now.month, now.day, 7)

# Get the high-impact US events
us_events = [e for e in cal if e.importance == mt4.EVENT_IMPORTANCE_HIGH and e.country == "US"]

# Get the current USD/JPY price
c = CurrencyRates()
usd_jpy = c.get_rate('USD', 'JPY')

# Determine the time remaining until the next high-impact US event
next_event = us_events[0]
time_remaining = next_event.timestamp - time.mktime(now.timetuple())

# Place buy and sell orders if the event is within 30 seconds
if time_remaining <= 30:
    buy_price = usd_jpy + 0.15
    sell_price = usd_jpy - 0.15
    mt4.ordersend(symbol="USDJPY", cmd=mt4.OP_BUY, volume=0.1, openprice=buy_price, slippage=3)
    mt4.ordersend(symbol="USDJPY", cmd=mt4.OP_SELL, volume=0.1, openprice=sell_price, slippage=3)

    # Set a timer to check if an order has been executed within 60 seconds
    start_time = time.time()
    while time.time() - start_time < 60:
        orders = mt4.orders_get(symbol="USDJPY")
        for order in orders:
            # If an order has been executed, close the position and cancel all remaining orders
            if order.open_price == buy_price or order.open_price == sell_price:
                mt4.orderclose(order.ticket, order.volume, mt4.bid if order.type == mt4.ORDER_TYPE_BUY else mt4.ask, slippage=3)
                mt4.ordersend(symbol="USDJPY", cmd=mt4.OP_DELETE)
                break
        else:
            # If no order has been executed within 60 seconds, cancel all orders
            mt4.ordersend(symbol="USDJPY", cmd=mt4.OP_DELETE)

