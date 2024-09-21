# PDF to Audio Conversion Pipeline

## Overview
This repository provides a simple pipeline to convert PDF documents into audio files using Python. The process involves extracting text from the PDF, detecting the language of the extracted text, and converting it into an audio file (MP3 format) using Google Text-to-Speech (gTTS).

### Key Features:
- **PDF Text Extraction**: Uses `PyPDF2` to extract text from PDF files.
- **Language Detection**: Automatically detects the language of the text using the `langdetect` library.
- **Text-to-Audio Conversion**: Converts text to audio using the `gTTS` (Google Text-to-Speech) API.
- Supports both English and Arabic for text-to-speech conversion.

---

## Requirements

To use this pipeline, you need the following Python libraries:
- `PyPDF2`: For reading and extracting text from PDF files.
- `langdetect`: For detecting the language of the extracted text.
- `gTTS`: For converting text to speech in MP3 format.

### Install Dependencies:
To install the necessary dependencies, run the following command:
```bash
pip install PyPDF2 langdetect gtts
```

---

## How It Works

The notebook implements the following steps:

1. **Extract Text from PDF**: Read the PDF file and extract text using `PyPDF2`.
2. **Detect Language**: Identify the language of the extracted text using the `langdetect` library.
3. **Convert Text to Audio**: Convert the extracted text into an audio file using Google Text-to-Speech (`gTTS`).

---

## File Structure

```
.
├── PDF_to_Audio_Conversion.ipynb  # Jupyter notebook implementing the pipeline
├── README.md                      # This README file
└── requirements.txt               # Python dependencies
```

---

## Usage

### 1. Clone the repository

```bash
git clone https://github.com/your-username/pdf-to-audio-conversion.git
cd pdf-to-audio-conversion
```

### 2. Run the Jupyter Notebook

You can open and run the notebook `PDF_to_Audio_Conversion.ipynb` in Jupyter. Follow the steps in the notebook to convert your PDF files into audio.

Alternatively, you can use the following example Python script:

### 3. Example Script

```python
from langdetect import detect
from PyPDF2 import PdfReader
from gtts import gTTS

def detect_language_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    language = detect(text)
    return language, text

def text_to_audio(text, language, output_path):
    lang_code = 'en' if language == 'en' else 'ar'
    tts = gTTS(text=text, lang=lang_code)
    tts.save(output_path)

def pdf_to_audio_pipeline(pdf_path, audio_output_path):
    # Step 1: Detect Language and Extract Text
    language, text = detect_language_from_pdf(pdf_path)

    # Step 2: Convert Text to Audio and Save as MP3
    text_to_audio(text, language, audio_output_path)

# Example usage
pdf_path = "example.pdf"
audio_output_path = "output_audio.mp3"
pdf_to_audio_pipeline(pdf_path, audio_output_path)
```

---

## Example

To convert a PDF into an MP3 audio file:

1. Place your PDF file in the same directory as the notebook or script.
2. Set the `pdf_path` and `audio_output_path` in the script or notebook.
3. Run the pipeline, and it will generate an audio file from the extracted text.

Example:
```python
pdf_path = "example.pdf"
audio_output_path = "output_audio.mp3"
pdf_to_audio_pipeline(pdf_path, audio_output_path)
```

---

## Customization

- **Language Support**: Currently, the script supports English (`en`) and Arabic (`ar`). You can add support for more languages by modifying the `text_to_audio` function.
- **Error Handling**: The script assumes valid PDFs and text extraction. Add error handling to manage different file formats or empty pages.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---
