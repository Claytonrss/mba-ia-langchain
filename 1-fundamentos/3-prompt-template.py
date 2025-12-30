from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    input_variables=["name"],
    template="Olá, meu nome é {name}! Crie uma piada com o meu nome."
)

print(template.format(name="Clayton"))