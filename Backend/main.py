from fastapi import FastAPI
from groq import Groq
import os

app = FastAPI()

client =Groq(api_key = os.getenv("api_key"))




@app.get("/")
def home():
    return {"message": "Backend Running Successfully"}



@app.post("/generate")
def generate(topic:str,technology:str,content:str,tone:str):

    prompt = f"""
        Generate a {content} on Topic name : {topic} with technology is{technology} and tone as {tone}

    """

    response = client.chat.completions.create(
        model = "llama-3.1-8b-instant",
        messages = [
            {
                "role" : "user",
                "content":prompt

            }
        ]
    )

    return{
        "response": response.choices[0].message.content
    }