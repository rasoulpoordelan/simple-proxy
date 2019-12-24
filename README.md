# Simple Proxy

### it's get every request and send it to specific endpoint

  

## Run

for debuging

```

  python3 app.py

```
for production
```
gunicorn app:webapp --bind localhost:9000 -w 4 --worker-class aiohttp.GunicornWebWorker
```
