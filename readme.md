# flask-jsonrpc

Demonstrates python json-rpc package with Flask.

## Build

```bash
$ pip install -r requirements.txt
$ python main.py

$ curl localhost:4000 -d '{"method":"echo", "params":["ass"], "jsonrpc":"2.0", "id":0}'
{"result": "ass", "id": 0, "jsonrpc": "2.0"}

$ curl localhost:4000 -d '{"method":"add", "params":["10", "20"], "jsonrpc":"2.0", "id":0}'
{"result": 30, "id": 0, "jsonrpc": "2.0"}

$ curl localhost:4000 -d '{"method":"square", "params":["14"], "jsonrpc":"2.0", "id":0}'
{"result": 196, "id": 0, "jsonrpc": "2.0"}
```
