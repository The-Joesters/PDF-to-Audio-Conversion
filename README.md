# Arabic and Englisah Books PDF to Audio Conversion Pipeline

## Overview
This repository provides a simple pipeline to convert PDF documents into audio files using Python. The process involves extracting text from the PDF, detecting the language of the extracted text, and converting it into an audio file (MP3 format) using Google Text-to-Speech (gTTS).

---

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Error Handling](#error-handling)
- [Directory Structure](#directory-structure)
- [Limitations](#limitations)
- [License](#license)
- [Contributing](#contributing)
- [Acknowledgements](#acknowledgements)

## Features

- **PDF Upload**: Upload PDF files up to 16 MB.
- **Text Extraction**: Extracts text content from PDFs using `PyPDF2`.
- **Language Detection**: Automatically detects the language of the extracted text with `langdetect`.
- **Text-to-Speech Conversion**: Converts text to speech using `gTTS`.
- **Audio Download**: Provides an MP3 audio file for download.
- Supports both **English** and **Arabic** for text-to-speech conversion.

## Requirements

- Python 3.6 or higher
- [Flask](https://palletsprojects.com/p/flask/)
- [PyPDF2](https://pypi.org/project/PyPDF2/)
- [langdetect](https://pypi.org/project/langdetect/)
- [gTTS](https://pypi.org/project/gTTS/)
- [Werkzeug](https://palletsprojects.com/p/werkzeug/)

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/pdf-to-audio-converter.git
   cd pdf-to-audio-converter
   ```

2. **Create a Virtual Environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**

   ```bash
   python app.py
   ```

   The application will be accessible at `http://127.0.0.1:5000/`.

## Usage

1. **Access the Web Interface**

   Open your web browser and navigate to `http://127.0.0.1:5000/`.

2. **Upload a PDF File**

   - Click on the "Choose File" button and select a PDF file.
   - Ensure the file size does not exceed 16 MB.

3. **Convert and Download**

   - Click the "Upload" button to start the conversion.
   - After processing, a download prompt for the MP3 file will appear.

## Configuration

- **Secret Key**

  Replace `'your_secret_key'` in `app.secret_key` with a secure, random string.

- **Upload Folder**

  The default upload folder is `uploads`. You can change this by modifying `app.config['UPLOAD_FOLDER']`.

- **Allowed Extensions**

  By default, only PDF files are allowed. Modify `app.config['ALLOWED_EXTENSIONS']` to add more file types.

- **Maximum File Size**

  The maximum upload size is set to 16 MB. Adjust `app.config['MAX_CONTENT_LENGTH']` to change this limit.

## Error Handling

- **413 Request Entity Too Large**

  Triggered when the uploaded file exceeds the maximum size limit.

- **No File Selected**

  If no file is selected or the file part is missing, an appropriate message is displayed.

- **Invalid File Type**

  Only files with allowed extensions are processed. Others will prompt an error message.

- **Text Extraction Failure**

  If the application cannot extract text from the PDF, an error message is shown.

## Directory Structure

```
pdf-to-audio-converter/
├── README.md
├── convert pdf book into audio.ipynb
├── requirements.txt
├── Api_code/
│   ├── static/
│   │   └── css/
│   │       └── style.css
│   └── templates/
│       └── index.html

```

- **app.py**: The main Flask application script.
- **requirements.txt**: Contains all the Python dependencies.
- **uploads/**: Stores uploaded PDFs and generated MP3 files.
- **templates/**: Contains the HTML template(s) for the web interface.

## Limitations

- **Language Support**

  Currently, the application explicitly supports English (`'en'`) and Arabic (`'ar'`). Other languages default to English in text-to-speech conversion.

- **PDF Content**

  The application may not extract text from scanned PDFs or those without extractable text content.

- **gTTS Limitations**

  gTTS relies on Google's text-to-speech API, which may have usage limits or restrictions.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for enhancements or bug fixes.
