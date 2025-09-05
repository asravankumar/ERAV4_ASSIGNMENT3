# Gemini OCR Analysis Web Application

A Python Flask web application that performs OCR (Optical Character Recognition) on uploaded images using Google's Gemini generative AI API. The app detects text segments, draws bounding boxes around each detected text in the image, displays extracted text, and also provides a brief summary of the extracted content.

---

## Features

- Upload images via a simple, Bootstrap-powered UI.
- Extract text segments with their bounding boxes using Gemini OCR.
- Display original image with interactive bounding boxes overlay.
- Highlight corresponding text and bounding box on hover/click.
- Copy extracted texts to clipboard easily.
- Generate and show a brief summary of the extracted text automatically.
- Responsive and user-friendly design.

---

---

## Getting Started

### Prerequisites

- Python 3.8 or above
- Google Gemini API access and API key
- Pip package manager

### Installation

1. Clone the repository:

git clone https://github.com/asravankumar/ERAV4_Assignment3.git
cd ERAV4_Assignment3


2. Create and activate a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate


3. Install dependencies:

pip install -r requirements.txt


4. Set your Gemini API key in `app.py`:

app.config["GEMINI_API_KEY"] = "YOUR_GEMINI_API_KEY"


### Running the Application

flask run --host=0.0.0.0 --port=5000


Then open your browser to `http://localhost:5000` or your server IP.

---

## Usage

- Click **Upload Image** to select an image file.
- The app will perform OCR and display the image with bounding boxes.
- Extracted text segments appear below the image.
- Hover or click on text or bounding boxes to highlight counterparts.
- Use the copy button to copy any extracted text.
- View the brief summary of all extracted text below the list.

---

## Project Structure


.
├── app.py # Flask application
├── ocr_gemini.py # OCR and summary logic using Gemini API
├── requirements.txt # Python dependencies
├── static/ # Static files like uploaded images
└── templates/
└── index.html # Main HTML template with Bootstrap UI


---

## Dependencies

- Flask
- google-genai (Google Gemini Python SDK)
- Pillow (PIL)
- Bootstrap 5 (via CDN)

---

## Contributing

Contributions are welcome! If you find bugs or want to add features:
- Fork the repo
- Create a feature branch
- Submit a pull request

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Acknowledgements

- Google Gemini API for powerful OCR and text generation.
- Bootstrap for responsive UI.
- Inspiration from community templates and docs.

---

Feel free to open issues or discussions for help or feature requests!


This README template follows best practices with clear sections describing the project purpose, setup, usage, and contribution guidelines. It can be customized further with project-specific links, screenshots, or deployment info as desired.
