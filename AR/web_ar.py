from flask import Flask, current_app
app = Flask(__name__)

@app.route('/')
def hello_world():
  return current_app.send_static_file('index.html')

if __name__ == '__main__':
    #app.run(host='0.0.0.0',debug=True,port=4000)
    app.run(host='0.0.0.0',debug=True,port=4000, ssl_context='adhoc')
    # https://jeromeetienne.github.io/AR.js/three.js/examples/marker-training/examples/generator.html