🏠 Housing Price Analysis & Prediction Web Application

A full-stack web application built using Flask that integrates Tableau dashboards for housing market analysis and provides a simple house price prediction feature based on user inputs.

📌 Project Overview

This project combines:

📊 Interactive Tableau Dashboard for housing sales trends

📈 Data storytelling using Tableau

🧮 House price prediction form (Flask backend)

🔁 Proper POST → Redirect → GET (PRG) implementation

🎨 Responsive UI using Bootstrap

It demonstrates frontend-backend integration along with embedded data visualization.

🚀 Features

Embedded Tableau Dashboard

Embedded Tableau Story

House price prediction based on:

Number of Bedrooms

Number of Bathrooms

Square Feet

Smooth UI with animations

Clean Flask project structure

Refresh-safe form submission (No resubmit warning)

🛠 Tech Stack
Layer	Technology Used
Frontend	HTML, CSS, Bootstrap
Backend	Python (Flask)
Visualization	Tableau
Template Engine	Jinja2
📁 Project Structure
House_Prediction/
│
├── Source_code/
│   ├── app.py
│   └── index.html
│
├── Demo Video/
│   └── Demo video.mp4
│
├── Document/
│   └── revise_document_house.docx
│
├── Project Files/
│   ├── dashboard.twb
│   ├── sheet1.twb
│   ├── sheet2.twb
│   ├── sheet3.twb
│   ├── sheet4.twb
│   └── story.twb
│
└── README.md
⚙️ How To Run This Project Locally

⚠️ The virtual environment (venv) is NOT included in this repository.
You must create your own virtual environment before running the project.

1️⃣ Clone the Repository
git clone <your-repository-url>
cd House_Prediction
2️⃣ Create a Virtual Environment
python -m venv venv
3️⃣ Activate the Virtual Environment
▶ Windows:
venv\Scripts\activate
▶ Mac / Linux:
source venv/bin/activate
4️⃣ Install Required Dependencies
pip install flask
5️⃣ Run the Application
python app.py
6️⃣ Open in Browser

Go to:

http://127.0.0.1:5000
💡 Important Notes

Recommended Python version: Python 3.10 or 3.11

Do NOT upload the venv folder to GitHub

Always activate the virtual environment before running the project

If errors occur, create a fresh virtual environment

📊 About the Prediction Feature

The prediction module:

Accepts user input via form (POST request)

Performs backend calculation

Uses PRG (Post → Redirect → Get) pattern

Displays result dynamically on the webpage

Currently, the prediction uses a sample calculation logic.
It can be upgraded by integrating a trained Machine Learning model (.pkl file).

🔮 Future Improvements

Integrate real ML model

Store predictions in database

Add user authentication

Deploy to cloud (Render / Railway / AWS)

Convert prediction to AJAX (no page reload)
