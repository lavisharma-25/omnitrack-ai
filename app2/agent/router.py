from app.agent.agent_setup import build_agent


class AgentRouter:
    """
    Entry point for agent execution.
    """

    def __init__(self):
        self.agent = build_agent()

    async def ainvoke(self, query: str):
        """
        Async execution.
        """
        result = await self.agent.ainvoke(
            {
                "messages": [
                    {
                        "role": "user",
                        "content": query,
                    }
                ]
            }
        )

        return result

    def invoke(self, query: str):
        """
        Sync execution.
        """
        result = self.agent.invoke(
            {
                "messages": [
                    {
                        "role": "user",
                        "content": query,
                    }
                ]
            }
        )

        return result