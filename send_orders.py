import MetaTrader5 as mt5


def buy_stocks(symbol, direction, volume, comment=" "):
    if direction == 1:
        price = mt5.symbol_info_tick(symbol).ask
        type_ = mt5.ORDER_TYPE_BUY
    else:
        price = mt5.symbol_info_tick(symbol).bid
        type_ = mt5.ORDER_TYPE_SELL

    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "type": type_,
        "price": price,
        "volume": volume,
        "deviation": 0,
        "type_time":  mt5.ORDER_TIME_GTC,
        "comment": comment,
        "type_filling": mt5.ORDER_FILLING_FOK,
    }
    result = mt5.order_send(request)


def sell_stocks(symbol, volume):
    for i in mt5.positions_get(symbol=symbol):
        position_id = i[7]
        price = mt5.symbol_info_tick(symbol).bid

        if i[5] == 0:
            action = mt5.ORDER_TYPE_SELL
        else:
            action = mt5.ORDER_TYPE_BUY

        request = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": symbol,
            "volume": volume,
            "type": action,
            "position": position_id,
            "price": price,
            "deviation": 20,
            "magic": 234000,
            "type_time": mt5.ORDER_TIME_GTC,
        }

        result = mt5.order_send(request)
