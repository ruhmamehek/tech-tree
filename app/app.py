import os
from jsongenerator import generate_tableJson, generate_graphJson
from preprocessing import check_csv_format
import urllib.request
from flask import Flask, flash, request, redirect, render_template, url_for
from werkzeug.utils import secure_filename
port = int(os.environ.get("PORT",5000))

csvFilePath = "./static/Courses.csv"
tableJsonFilePath = "./static/Courses.json"
graphJsonFilePath = "./static/graph.json"

UPLOAD_PDF_FOLDER = './static/files/'
UPLOAD_CSV_FOLDER = './static/'
UPLOAD_TEMP_CSV_FOLDER = './temp/'

app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_TEMP_CSV_FOLDER'] = UPLOAD_TEMP_CSV_FOLDER
app.config['UPLOAD_PDF_FOLDER'] = UPLOAD_PDF_FOLDER

ALLOWED_FILE_UPLOAD_EXTENSIONS = set(['csv'])
ALLOWED_PDF_UPLOAD_EXTENSIONS = set(['pdf'])
ADMIN_LOGGED_IN = True

def allowed_csv_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_FILE_UPLOAD_EXTENSIONS

def allowed_pdf_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_PDF_UPLOAD_EXTENSIONS
	
@app.route('/')
def tech_table():
	return render_template('index.html')

@app.route('/testing')
def render_cise():
	return render_template('demo_cise.html')

@app.route('/techtree')
def tech_tree():
	return render_template('graph.html')

@app.route('/credits')
def render_credits():
	return render_template('credits.html')

@app.route('/admin/login')
def render_login_page():
	ADMIN_LOGGED_IN = True
	return render_template('admin_login_page.html')

@app.route('/admin/logout')
def log_out_admin():
	ADMIN_LOGGED_IN = False
	return render_template('logged_out.html')

@app.route('/upload_csv')
def render_csv_upload_page():
	return render_template('fileUpload.html')

@app.route('/upload_csv', methods=['POST'])
def upload_csv_file():
	if request.method == 'POST' and ADMIN_LOGGED_IN:
        # check if the post request has the files part
		if 'files[]' not in request.files:
			flash('No file part')
			return redirect(request.url)
		files = request.files.getlist('files[]')
		for file in files:
			if file and allowed_csv_file(file.filename):
				filename = secure_filename(file.filename)
				file.save(os.path.join(app.config['UPLOAD_TEMP_CSV_FOLDER'], filename))
				result = check_csv_format()
				if(result[0]==False):
					os.system('mv ./temp/Courses.csv ./static/')
					generate_tableJson();
					generate_graphJson();
				flash(result[1])
			else:
				flash("Incorrect file extension. Only CSV file can be uploaded.")
		return redirect(url_for('render_csv_upload_page'))

@app.route('/upload_pdf')
def render_pdf_upload_page():
	return(render_template('pdfUpload.html'))

@app.route('/upload_pdf', methods=['POST'])
def upload_pdf_file():
	if request.method == 'POST':
        # check if the post request has the files part
			if 'files[]' not in request.files:
				flash('No file part')
				return redirect(request.url)
			files = request.files.getlist('files[]')
			for file in files:
				if file and allowed_pdf_file(file.filename):
					filename = secure_filename(file.filename)
					file.save(os.path.join(app.config['UPLOAD_PDF_FOLDER'], filename))
					flash('File(s) successfully uploaded')
				else:
					flash("Incorrect file extension. Only PDF(s) can be uploaded.")
			return redirect(url_for('render_pdf_upload_page'))

@app.route('/viewDescription/filename', methods=['POST','GET'])
def render_pdf_viewer():
	filename = request.args[""]
	filename = "./files/"+filename+".pdf"
	return render_template('simple.html', pdf=filename)

@app.errorhandler(404)
def file_not_found(error):
	return render_template('file_not_found.html')

if __name__ == "__main__":
    app.run(debug=True)
