from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

gemini = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.5)

question_template = PromptTemplate(
    input_variables=["name"],
    template="Olá, meu nome é {name}! Crie uma piada com o meu nome."
)

chain = question_template | gemini

response = chain.invoke({"name": "Clayton"})

print(response.content)