from langchain_core.output_parsers import StrOutputParser

from app.core.logs import logger
from app.graph.state import TrackState
from app import prompts as prompt
from app.services.llm_client import llm_model_flash, llm_model_lite

class GraphNodes:

    def __init__(self):
        self.flash_model = llm_model_flash
        self.lite_model = llm_model_lite

    def refine_question(self, state: TrackState):
        try:
            question = state.question
            chat_history = state.messages

            if not question:
                raise ValueError("Missing or empty question")

            parser = StrOutputParser()

            chain = (prompt.refine_query_prompt | self.lite_model | parser)

            response = chain.invoke({
                    "question": question,
                    "chat_history": chat_history,
            })

            return {"refined_question": response.strip()}

        except Exception as e:
            logger.error(str(e), exc_info=True)
            return {"refined_question": state.question}


    def final_answer(self, state: TrackState):
        try:
            question = state.refined_question
            section_data = state.relevant_section_data
            report_title = state.relevant_report_title

            report_data = None

            if report_title:
                for report in section_data.get("reports", []):
                    normalized_title = (
                        report.get("title", "")
                        .lower()
                        .replace(" ", "_")
                        .replace(".", "_")
                    )

                    if normalized_title == report_title:
                        report_data = (
                            f"{report_title}: {report.get('data')}"
                        )
                        break

            

            response = self.flash_model.invoke(
                prompt.final_answer_prompt.format_messages(
                    question=question
                )
            )

            return {"answer": response.content}

        except Exception as e:
            logger.error(str(e), exc_info=True)
            return {
                "answer": "An error occurred while generating the answer."
            }


    def update_history(self, state: TrackState):
        try:
            question = state.question
            answer = state.answer

            if not question or not answer:
                raise ValueError(
                    "Both question and answer must be present."
                )

            new_message = {
                "role": "assistant",
                "content": f"Q: {question}\nA: {answer}",
            }

            updated_messages = (
                state.messages + [new_message]
                if state.messages
                else [new_message]
            )

            return {"messages": updated_messages}

        except Exception as e:
            logger.error(str(e), exc_info=True)
            return {"messages": state.messages}
        

