from google import genai
from google.genai import types
import os
from dotenv import load_dotenv

load_dotenv()  



def get_gemini_resposne(prompt,system_prompt="You are helpful assistant."):

    client=genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

    config=types.GenerateContentConfig(
        system_instruction=system_prompt,
         temperature=0.1
    )

    response=client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt,
    config=config
    )

    return response.text



