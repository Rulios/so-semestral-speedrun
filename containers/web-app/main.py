from flask import Flask
import os
import logging

SERVER_PORT = os.getenv("SERVER_PORT", 3000)


app = Flask(__name__)

app.logger.setLevel(logging.DEBUG)  # Set the desired log level

# Counter to keep track of the number of requests
request_count = 0

@app.route('/')
def index():
    global request_count
    request_count += 1
    app.logger.info("Number of requests received: " + str(request_count))
    return "OK"

if __name__ == '__main__':
    app.run(port=SERVER_PORT, host='0.0.0.0')
