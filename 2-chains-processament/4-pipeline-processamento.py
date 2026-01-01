from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

template_translate = PromptTemplate(
    input_variables=["initial_language"],
    template="Translate the following text to English:\n ```{initial_language}```"
)

template_summary = PromptTemplate(
    input_variables=["text"],
    template="Summarize the following text in a four words:\n ```{text}```"
)

gemini = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.1)

translate_chain = template_translate | gemini | StrOutputParser()

summary_chain = template_summary | gemini | StrOutputParser()

pipeline = {"text": translate_chain} | summary_chain

response = pipeline.invoke({"initial_language": "LangChain é um framework para Python que facilita o desenvolvimento de aplicações de IA."})

print(response)
