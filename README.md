

---

# 🎤 Voice Notes App

A modern web app to **record, save, share, and manage your voice notes**. Built with **Python Flask** and hosted on **Railway**.

**Live Demo:** [https://voice-notes-app-production.up.railway.app](https://voice-notes-app-production.up.railway.app)

---

## Features

* 🎙 **Voice Recording**: Capture notes using your microphone.
* 💾 **Save Notes**: Save recordings as text on the server.
* 📤 **Share Notes**: Share your notes directly via WhatsApp.
* 🗑 **Delete Notes**: Remove unwanted notes easily.
* 🌙 **Dark Mode**: Toggle between light and dark themes.
* Modern UI with gradient buttons and responsive design.

---

## Screenshots

![Voice Notes App Screenshot](./screenshot.png)


---

## Installation & Usage

### 1. Clone the repository

```bash
git clone https://github.com/Methni0616/voice-notes-app.git
cd voice-notes-app
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
python app.py
```

Visit `http://127.0.0.1:5000` in your browser.

---

## Deployment

This app is deployed on **Railway**. Use the following settings:

* **Build Command:** `pip install -r requirements.txt`
* **Start Command:** `gunicorn app:app`
* **Environment:** Python 3

**Live Deployment:** [https://voice-notes-app-production.up.railway.app](https://voice-notes-app-production.up.railway.app)

---

## Folder Structure

```
voice-notes-app/
│
├─ app.py
├─ requirements.txt
├─ notes.txt          # stores saved notes
├─ templates/
│   └─ index.html
├─ static/
│   ├─ style.css
│   └─ service-worker.js
└─ manifest.json
```

---

## Technologies Used

* Python 3 & Flask
* HTML, CSS, JavaScript
* Web Speech API for voice recognition
* Railway.app for cloud hosting

---

## License

This project is licensed under the **MIT License**.

---



