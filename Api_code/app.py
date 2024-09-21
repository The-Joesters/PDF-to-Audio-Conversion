from flask import Flask, render_template, request, send_from_directory, redirect, url_for, flash
from PyPDF2 import PdfReader
from langdetect import detect
from gtts import gTTS
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure key
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'pdf'}
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB limit

# Ensure the upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def detect_language_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text
    if not text.strip():
        raise ValueError("No extractable text found in the PDF.")
    language = detect(text)
    return language, text

def text_to_audio(text, language, output_path):
    # Map detected language to gTTS supported languages if necessary
    lang_code = language if language in ['en', 'ar'] else 'en'  # Default to English
    tts = gTTS(text=text, lang=lang_code)
    tts.save(output_path)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'pdf_file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['pdf_file']
        # If user does not select file, browser may submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            pdf_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(pdf_path)
            try:
                language, text = detect_language_from_pdf(pdf_path)
                audio_filename = f"{os.path.splitext(filename)[0]}.mp3"
                audio_path = os.path.join(app.config['UPLOAD_FOLDER'], audio_filename)
                text_to_audio(text, language, audio_path)
                return send_from_directory(app.config['UPLOAD_FOLDER'], audio_filename, as_attachment=True)
            except Exception as e:
                flash(f"An error occurred: {str(e)}")
                return redirect(request.url)
        else:
            flash('Allowed file types are PDF')
            return redirect(request.url)
    return render_template('index.html')

@app.errorhandler(413)
def request_entity_too_large(error):
    flash('File is too large. Maximum size is 16MB.')
    return redirect(request.url), 413

if __name__ == '__main__':
    app.run(debug=True)
