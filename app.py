from flask import Flask, render_template, request, redirect
import os

from database import connection, cursor
from document_reader import read_document
from classifier import classify_document

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


# ---------------- HOME PAGE ---------------- #

@app.route("/")
def home():
    return render_template("index.html")


# ---------------- UPLOAD DOCUMENT ---------------- #

@app.route("/upload", methods=["POST"])
def upload():

    file = request.files["document"]

    if file.filename == "":
        return "No file selected."

    # Save uploaded file
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    # Read document text
    text = read_document(filepath)

    # Classify document
    category = classify_document(text)

    # Save to MySQL
    query = """
    INSERT INTO documents(filename, category)
    VALUES(%s,%s)
    """

    cursor.execute(query, (file.filename, category))
    connection.commit()

    return render_template(
        "result.html",
        filename=file.filename,
        category=category
    )


# ---------------- VIEW DOCUMENTS ---------------- #

@app.route("/documents")
def documents():

    cursor.execute("SELECT * FROM documents ORDER BY id DESC")

    documents = cursor.fetchall()

    return render_template(
        "documents.html",
        documents=documents
    )


# ---------------- DELETE DOCUMENT ---------------- #

@app.route("/delete/<int:id>")
def delete_document(id):

    # Get filename
    cursor.execute(
        "SELECT filename FROM documents WHERE id=%s",
        (id,)
    )

    file = cursor.fetchone()

    if file:

        filepath = os.path.join(
            app.config["UPLOAD_FOLDER"],
            file[0]
        )

        # Delete file from uploads folder
        if os.path.exists(filepath):
            os.remove(filepath)

        # Delete record from database
        cursor.execute(
            "DELETE FROM documents WHERE id=%s",
            (id,)
        )

        connection.commit()

    return redirect("/documents")


if __name__ == "__main__":
    app.run(debug=True)