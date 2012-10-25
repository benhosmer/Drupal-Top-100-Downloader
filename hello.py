from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def hello(name=None, current_time=datetime.now()):
	return render_template('index.html', name=name, current_time=current_time)




if __name__ == "__main__":
    app.run(debug=True)