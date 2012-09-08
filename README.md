# uwsgi-websockets

Provides a WSGI middleware that wraps geventwebsocket's WebSocketHandler,
allowing it to be used with uwsgi. All the websocket parsing is provided by
geventwebsocket, this just turns it into a WSGI middleware that knows how to
pass uwsgi's socket into WebSocketHandler.


# Usage with Django
I'm using this by creating another WSGI module, so I can still use gevent's WSGI server etc.

### `myapp.ws_wsgi.py`
```python
from uwsgi_websockets.middleware import ws_middleware

from myapp.wsgi import application

application = ws_middleware(application)
```

### `run_wsgi.sh`
```sh
exec uwsgi --http :8000 --loop gevent --module myapp.ws_wsgi\
           --async 1000 --http-raw-body
```
