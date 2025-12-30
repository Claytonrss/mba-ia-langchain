from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.runnables import chain
from dotenv import load_dotenv
load_dotenv()

@chain
def square(input_dict: dict) -> dict:
    x = input_dict["x"]
    return {"square_result": x * x}

gemini = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.5)

question_template = PromptTemplate(
    input_variables=["square_result"],
    template="{square_result} é o resultado do quadrado de qual número?"
)

chain = square | question_template | gemini

response = chain.invoke({"x": 10})

print(response.content)