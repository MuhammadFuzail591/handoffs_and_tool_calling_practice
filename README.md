
# 🧠 Handoffs and Tool Calling with Custom Agents

This project demonstrates how to implement **multiple AI agents** and **tool calling** with structured Python modules using `venv` and `pyproject.toml`. It’s designed to make it easier to test modular agents like weather checkers, content summarizers, and copywriting tools—all powered by OpenAI.

---

## 📁 Project Structure

```
project-root/
│
├── config/
│   ├── __init__.py               # Makes the directory a package
│   └── openai_config.py          # Contains OpenAI API key and client setup
│
├── custom_agents/
│   ├── __init__.py               # Package initializer
│   ├── copywriting.py            # Agent for generating marketing copy
│   ├── lead_agent.py             # Directs tasks to appropriate sub-agents
│   ├── summarizer.py             # Summarizes large content using OpenAI
│   └── weather_agent.py          # Calls the weather tool agent
│
├── tools/
│   ├── __init__.py               # Package initializer
│   └── get_weather_tool.py       # Tool function to fetch weather data
│
├── main_content_agent.py         # Entrypoint for content-related tasks
├── main_weather_agent.py         # Entrypoint for weather-related tasks
├── pyproject.toml                # Project metadata and dependencies
├── .env                          # Environment variables (e.g., OpenAI API key)
└── .venv/                        # Python virtual environment
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/MuhammadFuzail591/handoffs-and-tool-calling.git
cd handoffs-and-tool-calling
```

---

### 2. Set Up the Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate      # On Windows: .venv\Scripts\activate
```

---

### 3. Install Dependencies

Install all dependencies using `pyproject.toml`:

```bash
pip install -e .
```

If that doesn’t work, you can use `pip install` manually with dependencies listed in `pyproject.toml`.

---

### 4. Set Up Your `.env` File

Create a `.env` file in the root directory and add:

```
OPENAI_API_KEY=your_openai_key_here
```

---

### 5. Run the Agents

#### 🌤 Weather Agent

```bash
python main_weather_agent.py
```

#### ✍️ Content Agent

```bash
python main_content_agent.py
```

---

## 📦 Features

* **Agent Handoffs**: Main agents route tasks to specialized sub-agents.
* **Tool Calling**: Custom tools like `get_weather_tool.py` are dynamically invoked.
* **Modular Design**: Clean separation of config, agents, and tools for maintainability.

---

## 🛠 Technologies Used

* Python 3.10+
* OpenAI SDK
* `python-dotenv`
* `pyproject.toml` for modern dependency management

---

## 🤝 Contributing

Pull requests and improvements are welcome! Please ensure you follow the structure and clean code practices.

---

## 📄 License

MIT License. Free to use and modify for educational and commercial use.

---

Let me know if you'd like me to generate an image for this project structure (folder tree), or want to convert this README into a nicely designed webpage too!
