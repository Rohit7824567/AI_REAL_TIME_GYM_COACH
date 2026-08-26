import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

print("API KEY FOUND:", bool(api_key))

if not api_key:
    print("❌ GROQ_API_KEY nahi mili")
    exit()

print("✅ API key mil gayi")

client = Groq(api_key=api_key)

try:
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": "Say hello in one short sentence."
            }
        ],
        temperature=0.4
    )

    print("\n✅ GROQ API WORKING")
    print("Response:")
    print(response.choices[0].message.content)

except Exception as e:
    print("\n❌ GROQ API FAILED")
    print("Error type:", type(e).__name__)
    print("Error:", e)