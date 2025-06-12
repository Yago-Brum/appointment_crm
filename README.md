# 📅 Appointment CRM

A **Customer Relationship Management (CRM)** system designed for scheduling appointments. Built with a **Django backend** and a **React frontend**, this application allows for efficient management of clients and their appointments.

---

## ✨ Features

- 🔐 User authentication (Login, Registration, Logout)  
- 👤 Customer management (Create, Read, Update, Delete)  
- 📆 Appointment management (Create, Read, Update, Delete)  
- 💻 Responsive and user-friendly interface built with **React** and styled with **Tailwind CSS**  
- 🔁 RESTful API for seamless communication between backend and frontend  

---

## 🛠 Technologies

The project is divided into two main parts: **backend** and **frontend**.

### 🔙 Backend

- **Python** – Primary programming language  
- **Django** – Web framework for rapid and secure development  
- **Django REST Framework** – Toolset for building APIs  
- **SQLite3** – Default database for development  
- **Pytest** – Testing framework  

### 🌐 Frontend

- **React** – JavaScript library for building user interfaces  
- **Tailwind CSS** – Utility-first CSS framework for fast styling  
- **JavaScript (ES6+)** – Language used for frontend logic  
- **Node.js & npm** – Environment and package manager for frontend development  

---

## 🚀 Getting Started

Follow the steps below to set up and run the project locally.

### 📦 Clone the Repository

```bash
git clone https://github.com/Yago-Brum/appointment_crm
cd appointment_crm
```

---

### ⚙️ Backend Setup

1. Navigate to the backend directory:

```bash
cd backend  # or the correct folder if different
```

2. Create a virtual environment:

```bash
python -m venv venv
```

3. Activate the virtual environment:

```bash
# On Windows
venv\Scripts\activate

# On Linux/Mac
source venv/bin/activate
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

5. Apply database migrations:

```bash
python manage.py migrate
```

6. Run the development server:

```bash
python manage.py runserver
```

> The backend will be accessible at: `http://127.0.0.1:8000/`

---

### 💻 Frontend Setup

1. Open a new terminal and navigate to the frontend directory:

```bash
cd frontend  # or the correct folder if different
```

2. Install npm dependencies:

```bash
npm install
```

3. Start the React development server:

```bash
npm start
```

> The frontend will be available at: `http://localhost:3000/`, communicating with the backend API.

---

## 🧪 Running Tests

The backend includes a suite of tests to ensure API quality and functionality.

To run tests, activate your virtual environment and execute:

```bash
pytest
```
