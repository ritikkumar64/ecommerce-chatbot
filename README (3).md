# 🛍️ E-commerce Customer Support Chatbot

This project is a simple chatbot that supports customer queries on an E-commerce Clothing Website. It is built with **Flask (Python)** for the backend and **React** for the frontend. The app is also fully containerized using **Docker** and **Docker Compose**.

---

## 🚀 Features

- Check the status of orders  
- View top-selling products  
- Query product stock (e.g., "How many Classic T-Shirts are left?")

---

## 📁 Project Structure

```
ecommerce-chatbot/
├── backend/
│   ├── app.py
│   ├── chatbot_logic.py
│   ├── requirements.txt
│   └── data/
├── frontend/
│   ├── src/
│   │   └── App.js
│   └── ...
├── Dockerfile.backend
├── Dockerfile.frontend
├── docker-compose.yml
└── README.md
```

---

## ⚙️ Tech Stack

- **Backend**: Python, Flask, Pandas  
- **Frontend**: React, Axios  
- **Containerization**: Docker, Docker Compose  

---

## 🛠️ Setup Instructions

### ✅ Prerequisites

- Docker Desktop installed: [https://www.docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop)
- Git + VS Code (recommended)

---

### 🔧 1. Clone the Repository

```bash
git clone https://github.com/your-username/ecommerce-chatbot.git
cd ecommerce-chatbot
```

---

### 📦 2. Add Dataset Files

Place the following CSV files inside:  
`/backend/data/`

- `orders.csv`
- `order_items.csv`
- `inventory_items.csv`
- `products.csv`
- `users.csv`
- `distribution_centers.csv`

---

### 🐳 3. Run with Docker Compose

Build and run both backend and frontend:

```bash
docker compose up --build
```

- React App: `http://localhost:3000`
- Flask Backend: `http://localhost:5000/chat`

---

## 💬 Chatbot Sample Questions

Try asking in the UI:

- `What are the top 5 most sold products?`
- `Show me the status of order ID 12345.`
- `How many Classic T-Shirts are left in stock?`

---

## 🧠 Logic (backend/chatbot_logic.py)

The chatbot uses simple rule-based logic with Pandas to filter and query the uploaded CSV dataset.

You can improve this by integrating an NLP model or LLM later.

---

## 🛑 To Stop the App

Press `Ctrl + C` in the terminal  
Then run:
```bash
docker compose down
```

---

## ✨ Future Improvements

- Add LLM/NLP for natural language understanding
- Deploy to cloud (Render / Railway / Vercel)
- Add user authentication
- Expand chatbot intents

---

## 🙋‍♂️ Author

**Ritik Kumar & Kiran**  
Built as a hands-on project for understanding full-stack + containerized app development.

---

## 📜 License

Free to use for learning purposes.
