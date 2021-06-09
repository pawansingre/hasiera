from flask import Flask, jsonify,render_template, request
app = Flask(__name__)
@app.route("/")
def hello():
    return render_template('hostingstart-python.html')

if __name__ == '__main__':
    app.run(port=5002, threaded=True)
