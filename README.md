# 🏟️ FIFA 2026 Multilingual Fan Concierge

An AI-powered stadium routing agent designed to help fans navigate FIFA 2026 World Cup venues. This application utilizes a generative AI agent to process natural language requests, query physical stadium routes from a cloud data warehouse, and fetch live wait times for dynamic routing.

## 🚀 Tech Stack
* **Frontend:** Streamlit
* **Backend:** FastAPI, Uvicorn
* **AI/Agent Capability:** Google GenAI / Antigravity Agent framework
* **Database:** Google Cloud BigQuery
* **Deployment:** Render

## ✨ Features
* **Natural Language Processing:** Fans can ask routing questions in plain text to receive precise navigation assistance.
* **Dynamic AI Tool Calling:** The agent autonomously executes tools (e.g., `get_stadium_route`) to query BigQuery for static physical paths while prioritizing accessibility.
* **Live Telemetry:** The agent provides real-time congestion updates, such as elevator or gate delays, for optimized routing.
* **Microservices Architecture:** A decoupled frontend and backend, independently containerized for maximum portability and scalability.

## 🎓 Campus AI Workshop & Demonstration
This repository serves as a practical demonstration of integrating Generative AI with enterprise cloud architecture, ideal for technical campus workshops to illustrate:
* Transitioning from static data to live database querying using BigQuery.
* Building dynamic AI agent tool-calling capabilities.
* Deploying multi-container microservices to the cloud.

## 💻 Local Development
This project uses Docker to run the frontend and backend microservices in isolated environments.
<img width="1276" height="765" alt="image" src="https://github.com/user-attachments/assets/fe321c6c-27c1-4c7d-b7f9-fa2d549a2819" />

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/ganeshcharantej/stadium-agent.git](https://github.com/ganeshcharantej/stadium-agent.git)
   cd stadium-agent
