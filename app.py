from re import DEBUG
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello Nitesh!'

# print(__name__)
if __name__ == "__main__":
  # print("I am inside if")
  app.run(host='0.0.0.0', debug = True)