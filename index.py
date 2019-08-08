from flask import Flask, render_template

aplicacion = Flask(__name__)

@aplicacion.route('/')
def index():
	return render_template('index/index.html')

if __name__ == '__main__':
	aplicacion.run(debug=True)