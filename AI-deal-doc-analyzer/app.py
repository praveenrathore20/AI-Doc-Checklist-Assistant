from flask import Flask, render_template, request
import pdfplumber
import os
from docx import Document
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Upload folder
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Max upload size (16 MB)
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024

# Allowed file types
ALLOWED_EXTENSIONS = {"pdf", "docx"}

# Create uploads folder automatically
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


# Check file type
def allowed_file(filename):
    return "." in filename and \
           filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


# Extract text from PDF
def extract_pdf_text(pdf_path):

    try:

        text = ""

        with pdfplumber.open(pdf_path) as pdf:

            for page in pdf.pages:

                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"

        return text

    except Exception as e:

        return f"PDF Error: {str(e)}"


# Extract text from DOCX
def extract_docx_text(docx_path):

    try:

        doc = Document(docx_path)

        text = ""

        for para in doc.paragraphs:
            text += para.text + "\n"

        return text

    except Exception as e:

        return f"DOCX Error: {str(e)}"


# Organize checklist
def organize_checklist(text):

    lines = text.split("\n")

    cleaned = []

    for line in lines:

        line = line.strip()

        if len(line) > 2:
            cleaned.append(line)

    cleaned = list(dict.fromkeys(cleaned))

    output = ""

    heading_number = 1

    for line in cleaned:

        # Heading detection
        if (
            line.isupper()
            and len(line) < 60
        ):

            output += f"\n{heading_number}. {line}\n"

            heading_number += 1

        else:

            output += f"   • {line}\n"

    return output


# Home Page
@app.route("/")
def home():
    return render_template("index.html")


# Upload Route
@app.route("/upload", methods=["POST"])
def upload():

    if "pdf" not in request.files:

        return render_template(
            "result.html",
            checklist="Error: No file selected."
        )

    file = request.files["pdf"]

    if file.filename == "":

        return render_template(
            "result.html",
            checklist="Error: Please select a file."
        )

    if not allowed_file(file.filename):

        return render_template(
            "result.html",
            checklist="Error: Only PDF and DOCX files are allowed."
        )

    filename = secure_filename(file.filename)

    filepath = os.path.join(
        app.config["UPLOAD_FOLDER"],
        filename
    )

    try:

        file.save(filepath)

    except Exception as e:

        return render_template(
            "result.html",
            checklist=f"Error saving file: {str(e)}"
        )

    file_extension = filename.rsplit(".", 1)[1].lower()

    if file_extension == "pdf":

        extracted_text = extract_pdf_text(filepath)

    elif file_extension == "docx":

        extracted_text = extract_docx_text(filepath)

    else:

        extracted_text = ""

    if extracted_text.startswith("PDF Error"):

        return render_template(
            "result.html",
            checklist=extracted_text
        )

    if extracted_text.startswith("DOCX Error"):

        return render_template(
            "result.html",
            checklist=extracted_text
        )

    if not extracted_text.strip():

        return render_template(
            "result.html",
            checklist="Error: No readable content found."
        )

    checklist = organize_checklist(extracted_text)

    return render_template(
        "result.html",
        checklist=checklist
    )


# 404 Error
@app.errorhandler(404)
def page_not_found(error):

    return render_template(
        "result.html",
        checklist="Error 404: Page not found."
    ), 404


# 500 Error
@app.errorhandler(500)
def internal_server_error(error):

    return render_template(
        "result.html",
        checklist="Error 500: Internal server error."
    ), 500


if __name__ == "__main__":

    print("====================================")
    print(" AI Deal Checklist Assistant")
    print("====================================")
    print(" Supported Files: PDF, DOCX")
    print(" http://127.0.0.1:5000")
    print("====================================")

    app.run(debug=True)