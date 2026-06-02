from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from app.prompts import check_relevance_prompt, refine_question_prompt, final_answer_prompt

prompt_templates = {
    "check_relevance": check_relevance_prompt,
    "refine_question": refine_question_prompt,
    "final_answer": final_answer_prompt
}

print("Prompt templates loaded successfully.")