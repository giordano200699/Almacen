from flask import Flask, render_template, request,session
from pymongo import MongoClient

aplicacion = Flask(__name__)

aplicacion.secret_key = 'esto-es-mi-clave-secreta'



client = MongoClient("mongodb+srv://giordano:waldo@cluster0-p2txm.mongodb.net/Almacen?retryWrites=true")
mydb = client["Almacen"]

stands = mydb["stands"]


@aplicacion.route('/')
def index():
	return render_template('index/index.html')

@aplicacion.route('/panel',methods = ['POST'])
def panel():
	if(request.form.get('nombreAdministrador')!='Mirian' or request.form.get('clave')!='mayra'):
		return 'Los datos ingresados son inválidos'

	session['nombreAdministrador'] = request.form.get('nombreAdministrador')
	try:
		session['clave'] = request.form.get('clave')
	except:
		print("Boto error")
	return render_template('panel/panel.html')

@aplicacion.route('/panel',methods = ['GET'])
def panel2():
	if(session['nombreAdministrador']!='Mirian' or session['clave']!='mayra'):
		return 'Usted no ha iniciado sesión'
	standsC = stands.find()
	return render_template('panel/panel.html',standsC=standsC)

@aplicacion.route('/logout',methods = ['POST'])
def logout():
	session['nombreAdministrador'] = ''
	try:
		session['clave'] = ''
	except:
		print("Boto error")
	return render_template('index/index.html')

@aplicacion.route('/crearStand',methods = ['GET'])
def crearStand():
	if(session['nombreAdministrador']!='Mirian' or session['clave']!='mayra'):
		return 'Usted no ha iniciado sesión'
	return render_template('panel/crearStand.html')

@aplicacion.route('/crearStand',methods = ['POST'])
def crearStandP():
	if(session['nombreAdministrador']!='Mirian' or session['clave']!='mayra'):
		return 'Usted no ha iniciado sesión'
	if(request.form.get('nombreStand')==''):
		return 'Los datos ingresados son inválidos'
	standArrU = []
	standU = stands.find().sort('standId', -1).limit(1)
	for standEU in standU:
		standArrU.append(standEU)
	if(len(standArrU)>0):
		standId = standArrU[0]['standId'] + 1
	else:
		standId = 1
	
	x = stands.insert_one({ "nombreStand": request.form.get('nombreStand'), "standId":standId })
	standsC = stands.find()
	return render_template('panel/panel.html',standsC=standsC)

if __name__ == '__main__':
	aplicacion.run(debug=True)