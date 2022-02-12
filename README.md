# yfinance-server

a wraper around yfinance library

https://yfinance-server.vercel.app/



``` 
Ticker historical data.

Args:
    symbol (str, optional): A ticker symbol. Defaults to "MSFT".
    period (str, optional): Valid periods are: 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max. Defaults to '1d'.
    interval (str, optional): valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo. Defaults to '1m'.

Returns:
    list: list of dictionaries with fields t,o,h,l,c

```
