from flask import Flask, request, jsonify
import re

app = Flask(__name__)

# Helper function to check the length of the input.


def checkInputLength(inputString):
    # Assumption: if the input string is greater than 2000 then the string will be unsanitized.
    if (len(inputString) <= 2000):
        return True
    return False

# Helper function to check whether input is safe.


def isSafe(inputString):
    if (checkInputLength(inputString)):
        if re.search("([^a-zA-Z0-9</>,?:.\@\s])+", inputString):
            return False
        else:
            return True
    return False

# Function to validate the input value against SQL injection.


@app.route('/v1/sanitized/input/', methods=['POST'])
def validate_data():
    # handle the POST request
    try:
        value = request.get_json()
        userInput = value['payload']
        if(isSafe(userInput)):
            response = jsonify(result="sanitized")
            response.status_code = 200
        else:
            response = jsonify(result="unsanitized")
            response.status_code = 400

        return response

    except Exception as e:
        return jsonify(error="Some error occured")


if __name__ == '__main__':
    app.run(debug=True, port=5000)
