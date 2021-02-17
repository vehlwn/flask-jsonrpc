import flask
import jsonrpc

app = flask.Flask(__name__)

jsonrpc.dispatcher["echo"] = lambda s: s
jsonrpc.dispatcher["square"] = lambda s: int(s) ** 2
jsonrpc.dispatcher["add"] = lambda x, y: int(x) + int(y)


@app.route("/", methods=["POST"])
def root():
    data = flask.request.get_data()
    response = jsonrpc.JSONRPCResponseManager.handle(data, jsonrpc.dispatcher)
    ret_str = response.json
    return flask.Response(ret_str, mimetype="application/json")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000, debug=True, threaded=True, use_reloader=False)
