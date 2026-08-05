# AI Deal Doc Checklist Assistant

## Overview

AI Deal Doc Checklist Assistant is a web-based application built with Python and Flask that allows users to upload PDF checklist documents and automatically organize their contents into a structured, easy-to-read checklist.

The application is designed to simplify document review by extracting key checklist items from PDF files and presenting them in a clean and organized format. It acts as a lightweight digital assistant for reviewing deal documents, due diligence checklists, compliance lists, and other business-related documentation.

---

## Features

### PDF Upload

* Upload PDF checklist documents through a simple web interface.
* Supports standard text-based PDF files.

### Automatic Text Extraction

* Reads PDF content using PDF processing libraries.
* Extracts text from all pages of the uploaded document.

### Checklist Organization

* Identifies meaningful checklist items.
* Removes duplicate entries.
* Generates a structured numbered checklist.

### User-Friendly Interface

* Clean and responsive design.
* Easy navigation between upload and results pages.

### Scalable Architecture

* Flask-based backend.
* Ready for integration with AI models such as OpenAI GPT.
* Can be extended for advanced document analysis.

---

## Technology Stack

### Backend

* Python 3.x
* Flask

### Frontend

* HTML5
* CSS3

### PDF Processing

* pdfplumber

### Environment Management

* python-dotenv

### Optional AI Integration

* OpenAI API

---

## Project Structure

deal-checklist-ai/

├── app.py

├── .env

├── uploads/

├── static/

│ └── style.css

├── templates/

│ ├── index.html

│ └── result.html

└── README.md

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/praveenrathore20/AI-Doc-Checklist-Assistant.git
cd deal-checklist-ai
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

Windows:

```bash
venv\Scripts\activate
```

Linux / Mac:

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Application

```bash
python app.py
```

### 5. Open Browser

```text
http://127.0.0.1:5000
```

---

## Usage

1. Launch the application.
2. Upload a PDF checklist document.
3. The application extracts text from the PDF.
4. Checklist items are organized automatically.
5. Results are displayed in a structured format.

---

## Future Enhancements

### AI-Powered Document Analysis

* Intelligent extraction of key obligations.
* Identification of missing checklist items.
* Automatic prioritization of tasks.

### Export Options

* Export checklist as PDF.
* Export checklist as Excel.

### Advanced Features

* Drag and drop upload.
* User authentication.
* Dashboard analytics.
* Document history tracking.
* Cloud storage integration.

---

## Error Handling

The application includes handling for:

* Missing file uploads
* Empty PDFs
* Invalid file formats
* PDF extraction failures

---

## Author

Praveen Rathor

---

## License

This project is developed for educational and internship purposes.
