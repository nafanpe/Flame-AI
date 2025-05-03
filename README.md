# 🔥 Flame AI

Flame AI is a personal AI assistant project built in Python, designed to handle tasks like automation, intelligent conversation, image generation, and real-time web search. It brings together multiple AI APIs and Python libraries to offer a smart, speech-driven assistant experience.

---

## 🚀 Features

- 🎙️ **Text-to-Speech (TTS)** using `edge-tts`
- 🗣️ **Speech Recognition** via browser automation (`selenium`)
- 🎨 **AI Image Generation** with Hugging Face
- 🤖 **Conversational Chatbot** powered by Cohere and Groq APIs
- 🔎 **Real-Time Search Engine** integration
- ⚙️ **Automation Capabilities** (open/close apps, reminders, play music, system control)

---

## 🛠️ Tech Stack

- **Core Language**: Python  
- **Libraries Used**:
  - `python-dotenv`, `pywhatkit`, `bs4`, `pillow`, `requests`, `keyboard`, `pygame`, `rich`
  - `selenium`, `webdriver-manager`, `mtranslate`, `AppOpener`, `googlesearch-python`
  - `PyQt5` (for UI), `edge-tts` (TTS engine)
  - `groq`, `cohere` (AI chat handling)
  - `pywin32` (Windows automation)

---

## ⚙️ How to Run

No installation steps needed — just open the project folder and click the **Run** button in your IDE.

> **Note**: This project depends on API keys stored in a `.env` file, which is not included in this repo for security reasons.

---

## 📁 .env File Template

To run this project, create a `.env` file in the root directory with the following variables:

```dotenv
CohereAPIKey=your_cohere_api_key
GroqAPIKey=your_groq_api_key
HuggingFaceAPIKey=your_huggingface_api_key
Username=YourName
Assistantname=Flame
InputLanguage=en-IN
AssistantVoice=en-GB-RyanNeural

👤 Author
Crafted with passion by @nafanpe
