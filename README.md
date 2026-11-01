# 🧠 AI Philosophy Debate Assistant

## 📌 About the Project

AI Philosophy Debate Assistant is a web-based application developed using Python and Flask. It uses the Google Gemini API to generate philosophical arguments from two different perspectives: **in favor of** and **against** a given topic.

The main goal of this project is to help users understand different viewpoints, explore philosophical ideas, and improve their critical thinking skills.

## 🎯 Problem Statement

Understanding philosophical topics requires examining different perspectives. However, developing arguments both in favor of and against a topic can be challenging and time-consuming.

This project solves this problem by using Generative AI to automatically generate structured arguments from both sides of a given topic.

## ✨ Features

- Generate arguments in favor of a topic.
- Generate arguments against a topic.
- Integration with Google Gemini API.
- Dynamic topic input from users.
- Asynchronous API communication using aiohttp.
- Interactive web interface using Flask, HTML, and CSS.
- Error handling for API requests.

## 🛠️ Technologies Used

- Python
- Flask
- Google Gemini API
- aiohttp
- asyncio
- HTML
- CSS

## ⚙️ How It Works

1. The user enters a philosophical topic.
2. Flask receives the topic through an HTTP POST request.
3. The application creates two prompts:
   - One for an argument in favor of the topic.
   - One for an argument against the topic.
4. aiohttp sends asynchronous HTTP POST requests to the Google Gemini API.
5. Gemini generates arguments based on the prompts.
6. The application extracts the generated text from the JSON responses.
7. Both arguments are displayed on the webpage.

## 📂 Project Structure

```text
AI-Philosophy-Debate-Assistant/
│
├── app.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── requirements.txt
└── README.md
```

## 🚀 Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the project directory

```bash
cd AI-Philosophy-Debate-Assistant
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the environment

For Windows:

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure API Key

Get your Gemini API key from [Google AI Studio](https://aistudio.google.com/apikey).

Configure the API key securely as an environment variable. Do not upload your actual API key to GitHub.

### 7. Run the application

```bash
python app.py
```

### 8. Open in browser

```text
http://127.0.0.1:5000/
```

## 🧠 Asynchronous Programming

This project uses asynchronous programming to handle communication with the Google Gemini API.

- `async def` defines asynchronous functions.
- `await` waits for asynchronous operations.
- `aiohttp.ClientSession()` manages HTTP sessions.
- `session.post()` sends API requests.
- `await response.json()` reads API responses asynchronously.

This approach allows the application to handle I/O operations without blocking the event loop.

## ⚠️ Challenges Faced

- Integrating the Google Gemini API with Flask.
- Handling asynchronous API requests.
- Designing effective prompts for both debate perspectives.
- Extracting generated arguments from JSON responses.
- Handling API errors and unexpected responses.

## 📚 What I Learned

- Python application development.
- Flask web development.
- Generative AI integration.
- Google Gemini API.
- Prompt engineering.
- Asynchronous programming using Python.
- HTTP requests and JSON response handling.

## 👨‍💻 Author

**Challa Linga Reddy**

- GitHub: https://github.com/LINGAREDDYCHALLA
- LinkedIn: https://linkedin.com/in/lingareddy

---

⭐ If you find this project interesting, please consider giving it a star!
