from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/', methods=["POST", "GET"])
def calculate():
    num1 = request.args['num1']
    num2 = request.args['num2']
    operation = request.args['operation']

    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        response = "INCORRECT INPUT"
        return response, 400

    if operation == 'add':
        result = num1 + num2

    elif operation == 'sub':
        result = num1 - num2

    elif operation == 'mult':
        result = num1 * num2

    elif operation == 'div':
        try:
            result = num1 / num2
        except ZeroDivisionError:
            response = "ZeroDivisionError"
            return response, 400
    else:
        response = "INCORRECT OPERATION"
        return response, 400

    response = {"First number": num1,
                "Second number": num2,
                "operation": operation,
                "result": result}
    return response, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False)
