from flask import Flask, request
import logging
import sys

logging.basicConfig(stream=sys.stderr)

app = Flask(__name__)

TEMPLATE = """
<!doctype html>
<html>
    <head>
        <title>Request Parrot</title>
    </head>
    <body>
        <h1>Request Parrot</h1>
        <p>Request type: {req_type}</p>
        <p>Request parameters:</p>
        <ul>
            {params}
        </ul>
    </body>
</html>
"""

@app.route("/request-parrot", methods=['POST', 'GET'])
def print_form_values():
    params = ""
    for field in request.values.keys():
        value = request.values.getlist(field)
        if len(value) == 1:
            value = value[0]
        params += "<li><b>{key}</b>: {value}</li>".format(key=field, value=value)

    return TEMPLATE.format(req_type = request.method,
                params=params)

if __name__ == "__main__":
    app.run()
