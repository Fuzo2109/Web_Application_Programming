from flask import Flask, render_template, request
import os

app = Flask(__name__)
UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        if f.filename != '':
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
            return 'File uploaded successfully!'
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True, port=5005)