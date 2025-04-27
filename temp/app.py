import aiohttp
import asyncio
from flask import Flask, render_template, request
from asgiref.wsgi import WsgiToAsgi  

app = Flask(__name__)

API_KEY = "AIzaSyAQHP4NWzOsupleD4WMJx5n45xh6GbG-WI"
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-pro:generateContent?key={API_KEY}"

async def generate_argument_async(topic, stance):
    prompt = f"Give a detailed philosophical argument {stance} the idea: '{topic}'."
    headers = {"Content-Type": "application/json"}
    body = {
        "contents": [{"parts": [{"text": prompt}]}]
    }
    async with aiohttp.ClientSession() as session:
        try:
            async with session.post(API_URL, json=body, headers=headers) as response:
                response.raise_for_status()
                data = await response.json()
                argument = data['candidates'][0]['content']['parts'][0]['text']
                return argument.strip()
        except Exception as e:
            return f"⚠️ Error generating response: {str(e)}"

@app.route('/', methods=['GET', 'POST'])
async def index(): 
    if request.method == 'POST':
        topic = request.form['topic']
        for_argument = await generate_argument_async(topic, "in favor of")
        against_argument = await generate_argument_async(topic, "against")
        return render_template('index.html', topic=topic, for_argument=for_argument, against_argument=against_argument)
    return render_template('index.html', topic=None)

if __name__ == '__main__':
    from uvicorn import run
    asgi_app = WsgiToAsgi(app)
    run(asgi_app, host="0.0.0.0", port=5000)