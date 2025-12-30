from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
load_dotenv()

google_genai = init_chat_model(model="gemini-2.5-flash", model_provider="google_genai", temperature=0.5)

response = google_genai.invoke("Quem é o criador do langchain?")

print(response.content)