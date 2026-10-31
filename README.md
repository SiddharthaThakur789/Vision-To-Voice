# Vision To Voice 👁️ 🔊

This is a Python script I put together that extracts text from an image and reads it out loud—but only when you give it a specific voice command. 

It uses Tesseract for Optical Character Recognition (OCR), cleans up the image for better accuracy using Pillow (converting to grayscale and applying a binary threshold), and then listens via the microphone. If it hears the trigger word ("Mahadev"), the script speaks the extracted text back to you.

## Prerequisites

Because this relies on Tesseract and audio hardware, you need a couple of system-level dependencies:

1. **Tesseract-OCR**: You must install the actual Tesseract executable on your machine, not just the Python wrapper. 
   * Windows users: Download the installer and ensure it's installed at `C:\Program Files\Tesseract-OCR\tesseract.exe`. If you install it somewhere else, you'll need to update line 6 in the script.
2. **A working microphone**

## Installation

Install the required Python libraries:

```bash
pip install Pillow pytesseract pyttsx3 SpeechRecognition

(Note: If you are on Windows and run into microphone/PyAudio errors with SpeechRecognition, you may also need to run pip install PyAudio.)

How to Use
Open the script and update the image path. Change img=Image.open(...) to the actual path of the image you want to read.

Run the script:

Bash
python main.py
The script will print the text it managed to extract from the image into your terminal.

When you see Listening... appear, say "Mahadev".

If recognized, the system's text-to-speech engine will read the extracted text out loud.

Quirks & Notes
Accuracy: I added a custom config (oem 3 psm 6) and a basic thresholding filter to help Tesseract read the text better, but OCR isn't always perfect. Lighting and image quality matter.

Timeout: The microphone listens for 5 seconds. If you have a lot of background noise, Google's speech recognition might struggle to isolate the trigger word.