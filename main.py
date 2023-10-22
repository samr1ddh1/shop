from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    """_summary_
    """
    return render_template('index.html')

@app.route('/port')
def port():
    """_summary_
    """
    return render_template('port.html')

if __name__ == '__main__':
    app.run(port=3000, debug=True)
