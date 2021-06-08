from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import json
import numpy as np
import yfinance as yf
import pandas as pd


class handler(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header('Access-Control-Allow-Headers', '*')
        self.send_header('Access-Control-Allow-Methods', '*')
        self.end_headers()

    def do_GET(self):
        self._set_response()
        parsed = urlparse(self.path)
        query = parse_qs(parsed.query)
        symbol = query.get("symbol",["MSFT"])[0]
        period = query.get("period",["1d"])[0]
        interval = query.get("interval",["1m"])[0]
        print(symbol, period, interval)
        data = self.yf_history(symbol, period, interval)
        self.wfile.write(json.dumps(data).encode('utf-8'))
        return
    


    def yf_history(self, symbol="MSFT", period='1d', interval='1m'):
        """ Ticker historical data.

        Args:
            symbol (str, optional): A ticker symbol. Defaults to "MSFT".
            period (str, optional): Valid periods are: 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max. Defaults to '1d'.
            interval (str, optional): valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo. Defaults to '1m'.

        Returns:
            list: list of dictionaries with fields t,o,h,l,c
        """
        df = self.yf_history_dataframe(symbol, period, interval)
        return df.to_dict(orient='records')


    def yf_history_dataframe(self, symbol="MSFT", period='1d', interval='1m') -> pd.DataFrame:
        """ Ticker historical data.

        Args:
            symbol (str, optional): A ticker symbol. Defaults to "MSFT".
            period (str, optional): Valid periods are: 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max. Defaults to '1d'.
            interval (str, optional): valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo. Defaults to '1m'.

        Returns:
            pandas dataframe: list of records with fields t,o,h,l,c
        """
        ticker = yf.Ticker(symbol)
        df = ticker.history(period, interval)
        df['Time'] = df.index.astype(np.int64) // 10**9
        df = df[['Time', 'Open', 'High', 'Low', 'Close']]
        df.reset_index(drop=True, inplace=True)
        df.columns = ['t', 'o', 'h', 'l', 'c',]
        return df



if __name__ == '__main__':
    from http.server import HTTPServer
    httpd = HTTPServer(('localhost', 8000), handler)
    httpd.serve_forever()