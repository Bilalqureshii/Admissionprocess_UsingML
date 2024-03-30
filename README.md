# Admission Process Using Machine Learning

This is a Flask-based web application for managing the admission process using machine learning algorithms. It allows users to register, log in, view colleges, analyze admission results based on SSC percentage, and access information about the admission process and scholarships.

## Technologies Used
- Flask: A micro web framework for Python.
- MySQL: A relational database management system.
- Flask-MySQLdb: A Flask extension for MySQL connectivity.
- Pandas: A powerful data analysis and manipulation library for Python.
- HTML/CSS: For front-end web development.

## Installation
1. Clone the repository: `git clone git@github.com:Bilalqureshii/Admission_process_using_ML.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Set up MySQL database and configure connection details in `app.py`.
4. Run the Flask application: `python app.py`

## Features
- **User Authentication**: Users can register, log in, and log out securely.
- **Admission Result Analysis**: Users can input their SSC percentage to analyze college admission results.
- **Dynamic College Information**: Information about colleges and their branches is loaded dynamically from a CSV file.
- **Responsive Design**: The web application is designed to be responsive and accessible on various devices.

## File Structure
- `app.py`: Main Flask application file containing route definitions and database configurations.
- `templates/`: Contains HTML templates for rendering web pages.
- `static/`: Contains static assets such as CSS files.
- `result_data.csv`: CSV file containing college admission data.

