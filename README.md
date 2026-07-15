Document Management System with Automated Categorization

Project Overview

A web-based Document Management System developed using Python, Flask,
MySQL, HTML, and CSS. The application allows users to upload,
categorize, store, view, and delete documents. It supports PDF, DOCX,
and TXT files and uses rule-based keyword matching to automatically
categorize uploaded documents.

Features

-   Upload PDF, DOCX, and TXT documents
-   Automatic document categorization using Python
-   Store document metadata in MySQL
-   View all uploaded documents
-   Delete documents from both the database and uploads folder
-   Simple and responsive user interface

Tech Stack

-   Python
-   Flask
-   MySQL
-   HTML5
-   CSS3
-   PyMySQL
-   PyPDF2
-   python-docx

Project Structure

DOCUMENT_CLASSIFIER/ - app.py - classifier.py - document_reader.py -
database.py - document_management.sql - requirements.txt - static/ -
templates/ - uploads/

Database

Database Name: document_management

Table: documents - id - filename - category - upload_date

How to Run

1.  Install Python 3.8 or above.
2.  Install dependencies: pip install flask pymysql PyPDF2 python-docx
    cryptography
3.  Create the MySQL database using document_management.sql.
4.  Update database.py with your MySQL username and password.
5.  Run: python app.py
6.  Open: http://127.0.0.1:5000

Future Enhancements

-   Search documents
-   Download documents
-   Category filters
-   User authentication
-   Power BI dashboard integration

Author

Developed as a portfolio project for Data Analyst and Business
Intelligence roles.
