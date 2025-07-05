# 🧠 MCP EduChain for Claude Desktop

This project provides an **MCP (Model Context Protocol)** server for Claude Desktop that exposes educational tools powered by the [EduChain](https://github.com/satvik314/educhain) library. It allows Claude to dynamically generate:

- ❓ MCQs (Multiple Choice Questions)
- 📘 Lesson plans
- 🧠 Flashcards

Built using [`mcp`](https://pypi.org/project/mcp/) and `uv`, this setup ensures Claude can communicate with the tools via a local MCP server.

---

## 🔧 Features

- ✅ Easy setup with `uv` and `mcp`
- 🧠 Integrates EduChain’s educational tools
- 🧪 CLI test runner for tools
- 🧾 Claude-ready configuration file

---

## 📁 Project Structure

```
mcp-educhain/
├── main.py                   # The MCP server with tools/resources
├── test_endpoints.py         # CLI test runner for tools
├── .env.example              # Example env file (add your OpenAI key here)
├── claude_desktop_config.json # MCP config for Claude Desktop
├── sample_responses.txt      # Sample responses from each endpoint
├── README.md                 # This file
├── pyproject.toml            # Project dependencies
├── .gitignore                # Ignore venv, pycache, etc.
```

---

## 🚀 Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/leoperator/mcp-educhain.git
cd mcp-educhain
```

### 2. Install EduChain from Source

```bash
pip install git+https://github.com/satvik314/educhain.git
```

### 3. Setup Environment Variables

```bash
cp .env.example .env
```

Then open `.env` and insert your key:

```
OPENAI_API_KEY=your_openai_api_key_here
```

### 4. Install Dependencies Using `uv`

```bash
pip install uv
uv pip install -e .
```

### 5. Run the Server

```bash
uv run main.py
```

---

## 🧠 Claude Desktop Setup

### 1. Open Claude → Settings → Developer Tab

Click **"Add MCP Server"** and set:

```
Command: uv
Arguments:
  run
  --with
  mcp[cli]
  mcp
  run
  main.py
```

Or use the provided `claude_desktop_config.json`.

---

## 🧪 Testing Tools Without Claude

Use the CLI tester:

```bash
python test_endpoints.py
```

---

## ✨ Endpoints Provided

### 🛠️ Tools

- `generate_mcqs(topic: str, num_questions: int) -> list`
- `generate_flashcards(topic: str, num_cards: int) -> list`

### 📚 Resource

- `lessonplan://{topic}` → returns a detailed lesson plan

---
## 🛠️ Challenges Faced

### 1. Port Conflicts and Server Startup Issues
- **Issue**: Claude failed to connect due to overlapping port usage or unexpected debug output.
- **Fix**: Suppressed Flask's startup banner and ensured a consistent, clean JSON response by switching to `FastMCP` instead of Flask.

### 2. EduChain Import Errors
- **Issue**: Educhain module couldn't be resolved in the MCP project.
- **Fix**: Installed Educhain using `pip install -e <path>` and ensured it's referenced properly in `pyproject.toml`.

### 3. Claude Not Recognizing Resources
- **Issue**: Claude didn't detect the `lessonplan://{topic}` resource.
- **Fix**: Restructured the resource return format using recursive `__dict__` flattening, and simplified types for better parsing.

