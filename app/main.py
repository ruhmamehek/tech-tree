import os
#import magic
import urllib.request
from app import app
from flask import Flask, flash, request, redirect, render_template
from werkzeug.utils import secure_filename

ALLOWED_FILE_UPLOAD_EXTENSIONS = set(['csv','pdf'])
ALLOWED_PDF_UPLOAD_EXTENSIONS = set(['pdf'])
ADMIN_LOGGED_IN = True

def allowed_csv_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_FILE_UPLOAD_EXTENSIONS

def allowed_pdf_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_PDF_UPLOAD_EXTENSIONS
	
@app.route('/')
def tech_table():
	return render_template('index.html')

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

@app.route('/uploadfiles')
def render_file_upload_page():
	if(ADMIN_LOGGED_IN):
		return render_template('fileUpload.html')
	else:
		return render_template('permission_denied.html')

@app.route('/uploadfiles', methods=['POST'])
def upload_csv_file():
	if request.method == 'POST' and ADMIN_LOGGED_IN:
        # check if the post request has the files part
		if 'files[]' not in request.files:
			flash('No file part')
			return redirect(url_for('render_file_upload_page'))
		files = request.files.getlist('files[]')
		for file in files:
			if file and allowed_csv_file(file.filename):
				filename = secure_filename(file.filename)
				file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		flash('File successfully uploaded')
		return redirect(url_for('render_file_upload_page'))

# @app.route('/admin/pdfUpload')
# def render_pdf_upload_page():
# 	if(ADMIN_LOGGED_IN):
# 		return render_template('pdfUpload.html')
# 	else:
# 		return render_template('permission_denied.html')

# @app.route('/pdfUploaded', methods=['POST'])
# def upload_pdf_file():
# 	if request.method == 'POST' and ADMIN_LOGGED_IN:
#         # check if the post request has the files part
# 		if 'files[]' not in request.files:
# 			flash('No file part')
# 			return redirect(request.url)
# 		files = request.files.getlist('files[]')
# 		for file in files:
# 			if file and allowed_pdf_file(file.filename):
# 				filename = secure_filename(file.filename)
# 				file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
# 		flash('File(s) successfully uploaded')
# 		return redirect(url_for('pdfUploaded'))

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

