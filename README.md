
# Pharmacy Voice Agent 💊🎙️

This project is a **voice-enabled pharmacy assistant** that integrates **Deepgram, Twilio, and ngrok**.  
It allows users to:

- 📄 Get detailed **drug information**  
- 🛒 Place orders with **customer name and medicine**  
- 📦 Check **order status** by order ID  

The agent listens to voice input from Twilio, processes it using **Deepgram’s Speech-to-Speech API**, executes pharmacy functions, and replies with synthesized speech.  

---

## 🚀 Features
- In-memory **drug database** with popular medicines in Bangladesh.  
- **Order management system** (place & lookup orders).  
- **Real-time voice interaction** using Twilio WebSockets.  
- **Deepgram STS** for transcription + text-to-speech.  
- **OpenAI function-calling** for reasoning and decision-making.  
- Secure configuration with **.env**.  

---

## ⚙️ Requirements

Install dependencies with [**uv**](https://docs.astral.sh/uv/):

```bash
uv venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
uv pip install -r requirements.txt
````

### Python Packages

* `websockets`
* `asyncio`
* `python-dotenv`

---

## 🔑 Environment Variables

Create a `.env` file:

```ini
DEEPGRAM_API_KEY=your_deepgram_api_key
```

---

## ▶️ Run the Server

```bash
uv run main.py
```

The WebSocket server will start at:

```
ws://localhost:5000
```

---

## 🌍 Expose with ngrok

Since Twilio needs a public endpoint:

```bash
ngrok http 5000
```

Copy the **ngrok HTTPS URL** and configure it in your **Twilio voice settings**.

---

## 📞 Workflow

1. User calls your Twilio number.
2. Twilio sends the audio to your **local server** via WebSocket.
3. **Deepgram STS** transcribes and generates responses.
4. Functions like `get_drug_info`, `place_order`, or `lookup_order` are executed.
5. Response is spoken back to the caller.

---

## 📌 Example Interactions

**Get Drug Info**

> "Tell me about aspirin."
> ✅ Returns description, price, and available stock.

**Place Order**

> "I want to order Metformin. My name is Rahim Uddin."
> ✅ Confirms details and places order.

**Lookup Order**

> "Check order number 2."
> ✅ Returns order status.

---

## ⚠️ Notes

* All orders & drugs are stored **in-memory** (reset on restart).
* Always confirm customer name **spelled out clearly** before placing orders.
* For production, connect to a **real database**.
