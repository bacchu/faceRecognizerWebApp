from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

import face_analyzer

face_vector_data = {'Data': 'empty'}

app = Flask(__name__)
app.secret_key = 'mysecretkey'


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    json_image_data = {'data': 'empty'}

    if request.method == 'POST':
        f = request.files['filefield']
        f.save('/Users/triv/images/uploads/' + secure_filename(f.filename))
        image_file = '/Users/triv/images/uploads/' + f.filename
        json_image_data = face_analyzer.get_data(image_file)
        # return redirect(url_for('upload_file'))
    return render_template('index.html', result=json_image_data)


if __name__ == "__main__":
    app.run(debug=True)
