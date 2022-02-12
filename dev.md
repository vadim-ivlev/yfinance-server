## preparation

install env and libraries
```
python3 -m venv venv3.9
source venv3.9/bin/activate.fish
pip install -r requrements.txt

```
## development

run

```
python api/history.py
```



open

http://localhost:8000/api/history?symbol=MSFT&period=1d&interval=1m


upgrade yfinance
```
pip install yfinance --upgrade --no-cache-dir

```

## push and deploy to vercel

```
git add -A .
git commit -m "ddd"
git push github master
```

