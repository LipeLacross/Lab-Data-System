# Water Quality Management System

This project is a web application developed with Flask to manage water quality data. It allows user registration and authentication with different access levels (admin and operator), management of monitoring stations, and the insertion and visualization of analysis data for parameters such as BOD (DBO), COD (DQO), and pH.

## 🔨 Project Features

- **User Authentication**: Register and log in users with distinct roles (admin and operator).
- **Station Management**: Add and view water quality monitoring stations.
- **User Management**: Admins can add new users with different roles.
- **Data Insertion**: Operators can submit water quality analysis data.
- **Data Visualization**: View historical analysis data for each station.
- **Customized Dashboards**: Separate interfaces for administrators and operators.

### Project Visual Example



## ✔️ Technologies and Tools Used

- **Language**: Python
- **Framework**: Flask
- **Database**: SQLite with SQLAlchemy
- **Authentication**: JWT (JSON Web Tokens)
- **Frontend**: HTML, CSS (with basic styling)
- **Templates**: Jinja2
- **Other Libraries**:
  - `flask_jwt_extended` for JWT token management
  - `flask_sqlalchemy` for ORM

## 📁 Project Structure

```
├── LICENSE
├── anotations.txt
├── app.py
├── static/
│   ├── style.css
│   └── images/
│       ├── dashboard_admin.png
│       └── dashboard_operator.png
└── templates/
├── dashboard_admin.html
├── dashboard_operator.html
├── login.html
├── README.md
└── README_EN.md
```

- **LICENSE**: Project license file.
- **anotations.txt**: Possibly for additional notes or documentation.
- **app.py**: Main Flask application file containing routes, models, and business logic.
- **static/**: Directory for static files like CSS and images.
  - **style.css**: Stylesheet for the frontend.
  - **images/**: Images used in the templates (visual examples).
- **templates/**: Directory for HTML templates rendered by Flask.
  - **dashboard_admin.html**: Interface for administrators.
  - **dashboard_operator.html**: Interface for operators.
  - **login.html**: Login page.

## 🛠️ How to Open and Run the Project

To run the project locally, follow the steps below:

1. **Ensure Python is Installed**:
   - [Python](https://www.python.org/) is required to run the project. You can check if it's already installed by running:
     
     ```bash
     python --version
     ```

   - If not installed, download and install the recommended version.

2. **Clone the Repository**:
   - Copy the repository URL and execute the following command in your terminal:
     
     ```bash
     git clone <REPOSITORY_URL>
     ```

3. **Navigate to the Project Directory**:
   
   ```bash
   cd <PROJECT_DIRECTORY_NAME>
   ```

4. **Create a Virtual Environment** (recommended):

   ```bash
   python -m venv venv
   ```

5. **Activate the Virtual Environment**:
    - **On Windows**:

      ```bash
      venv\Scripts\activate
      ```

    - **On macOS/Linux**:

      ```bash
      source venv/bin/activate
      ```

6. **Install Dependencies**:
    - If a `requirements.txt` file does not exist, create one with the following dependencies:

      ```
      Flask
      Flask_SQLAlchemy
      Flask_JWT_Extended
      ```

    - Then, install the dependencies with:

      ```bash
      pip install -r requirements.txt
      ```

7. **Set Environment Variables** (optional):
    - You can define variables such as `SECRET_KEY` or other specific configurations if necessary.

8. **Initialize the Database**:
    - Run the application once to create the database tables:

      ```bash
      python app.py
      ```

    - After the initial run, you can stop the server (`Ctrl+C`).

9. **Run the Application**:

   ```bash
   python app.py
   ```

    - The application will be available at `http://127.0.0.1:5000/`.

## 🌐 Deployment

To deploy the application, you can use platforms like **Heroku**, **Render**, or **DigitalOcean**. Below is a basic guide for deploying on Heroku:

1. **Install the Heroku CLI**:
    - The [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) is required to interact with the platform.

2. **Log in to Heroku**:

   ```bash
   heroku login
   ```

3. **Create a New Heroku Application**:

   ```bash
   heroku create your-app-name
   ```

4. **Add a `Procfile`**:
    - Create a file named `Procfile` in the root of the project with the following content:

      ```
      web: python app.py
      ```

5. **Commit and Push to Heroku**:

   ```bash
   git add .
   git commit -m "Deploy to Heroku"
   git push heroku main
   ```

6. **Configure Environment Variables on Heroku**:
    - Set the `SECRET_KEY` and other necessary configurations through the Heroku dashboard or via CLI:

      ```bash
      heroku config:set SECRET_KEY='your_secret_key'
      ```

7. **Access the Application**:
    - After a successful deployment, the application will be available at the URL provided by Heroku.
