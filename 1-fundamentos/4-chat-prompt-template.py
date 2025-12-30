from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

google_genai = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.5)

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "Você é um assistente de IA que responde perguntas sobre o LangChain. Utilize o estilo de escrita {style}"),
    ("user", "{input}")
])

messages = chat_prompt.format_messages(input="Quem é o criador do langchain?", style="humoristico")

for message in messages:
    print(message.content)
    
response = google_genai.invoke(messages)

print(response.content)