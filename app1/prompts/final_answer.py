from langchain_core.prompts import ChatPromptTemplate

system_prompt = """You are a helpful assistant that provides final answers to questions based on the information provided by the user."""

human_prompt = """Based on the information provided, please provide a final answer to the question. If you are unsure, please indicate that you do not have enough information to provide a final answer."""

final_answer_prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", human_prompt)
])