from pybit.unified_trading import HTTP

def get_price(pair):
    '''Get the price of a cryptocurrency pair on the ByBit exchange'''
    session = HTTP(testnet=True)
    time_end = int(session.get_server_time()['result']['timeNano'])//1_000_000 # from ns to ms
    time_start = time_end - 3_600_000
    response = session.get_index_price_kline(
        category="linear",
        symbol=pair,
        interval=60,
        start=time_start,
        end=time_end,
        limit=1,
    )
    
    return response