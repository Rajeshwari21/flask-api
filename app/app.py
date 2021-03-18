from flask import Flask, request, jsonify
import re

app = Flask(__name__)

# Input Test scenarios:

# "This is a nice content and I will rate it as 7 out of 10. This is a nice content and I will rate it as 7 out of 10. This is a nice content and I will rate it as 7 out of 10. This is a nice content and I will rate it as 7 out of 10. This is a nice content and I will rate it as 7 out of 10. ;SELECT first_name, last_name FROM users UNION SELECT username, password FROM login;",
# "SELECT first_name, last_name FROM users WHERE user_id = '5'';",
# "<b>flask api: check if html tags work <h1></h1> <h2></h2> </b>",
# "1' UNION SELECT 1,2;- -",
# "Nice blog written by so and so person please have a look 1 ; \\' UNION SELECT 1,table_name FROM information_schema.tables;- -",
# "https://example.com/ex=' or 1==1;--",
# "Your team number is 105; DROP TABLE users",
# This is a nice content and I will rate it as 7 out of 10. This is a nice content and I will rate it as 7 out of 10. This is a nice content and I will rate it as 7 out of 10. This is a nice content and I will rate it as 7 out of 10. This is a nice content and I will rate it as 7 out of 10 check this out variar.rajeshwari@gmal.com",
# "The scenario above indicates that a blind SQL Injection attack is possible. Moving forward with identifying the number of columns, we use the following payload: 1' and 1=1 UNION SELECT 1;- -",
# "To extract the list of tables, we can use: 1' UNION SELECT 1, table_name FROM information_schema.tables - - The scenario above indicates that a blind SQL Injection attack is possible. Moving forward with identifying the number of columns, we use the following payload: 1' and 1 = 1 UNION SELECT 1--",
# """1 AND Select "mysql" UNION Select @@version""",
# "1 AND (SELECT 1 FROM (SELECT Count(*), concat(version(), FLOOR(rand(0)*2))x FROM information_schema.TABLES GROUP BY x)a)--",
# "1+AND+IF(version()+LIKE+'5%', true, false",
# "1+AND+IF(version()+LIKE+'5%', sleep(3), false",
# """this is a nice "meeting" all""",
# "abc' or 1 = 1 LIMIT--",
# "101 or 1=1 LIMIT",
# "abc' ORDER BY 1, 2, 3, 4, 5, 6,7--"

# Function to validate the input data against SQL injection like Error-based, Union based, boolean based, time-based.


@app.route('/v1/sanitized/input/', methods=['POST'])
def validateData():
    # handle the POST request
    try:
        data = request.get_json()
        userInput = data['payload']
        # handle empty input
        if not userInput:
            return jsonify(result="Input in Empty")
        elif userInput:
            # as said character length should be 2000.
            if (len(userInput) <= 2000):
                if re.search("([^a-zA-Z0-9</>,?:.\@\s])+", userInput):
                    return jsonify(result="unsanitized")
                else:
                    return jsonify(result="sanitized")
            else:
                return jsonify(result="Input is greater than 2000 character")
    except Exception as e:
        return jsonify(error="Some error occured")


if __name__ == '__main__':
    app.run(debug=True, port=5000)
