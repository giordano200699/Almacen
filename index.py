from flask import Flask, render_template, request,session 

aplicacion = Flask(__name__)

aplicacion.secret_key = 'esto-es-mi-clave-secreta'

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
	return render_template('panel/panel.html')

@aplicacion.route('/logout',methods = ['POST'])
def logout():
	session['nombreAdministrador'] = ''
	try:
		session['clave'] = ''
	except:
		print("Boto error")
	return render_template('index/index.html')


if __name__ == '__main__':
	aplicacion.run(debug=True)