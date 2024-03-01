import MetaTrader5 as mt5
import send_orders


def main():
    mt5.initialize()
    print("Connected to mt5!")
    send_orders.buy_stocks(symbol="YM", direction=1, volume=1)


if __name__ == '__main__':
    main()
