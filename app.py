from flask import Flask, render_template, request, redirect, flash
from werkzeug.utils import secure_filename

import face_analyzer

UPLOAD_FOLDER = '/Users/triv/images/uploads/'
# ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.secret_key = 'mysecretkey'


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def upload_file():
    return render_template('upload.html')


@app.route('/uploaded', methods=['GET', 'POST'])
def uploaded_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        f = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if f.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if f and allowed_file(f.filename):
            # f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            f.save('/Users/triv/images/uploads/' + secure_filename(f.filename))
            image_file = '/Users/triv/images/uploads/' + secure_filename(f.filename)
            json_image_data = face_analyzer.get_data(image_file)
            return render_template('uploaded.html', result=json_image_data)
        else:
            return render_template('uploaded.html', result=f.filename + ': NOT AN IMAGE FILE!')


if __name__ == '__main__':
    app.run(debug=True)
