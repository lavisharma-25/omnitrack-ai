from agent.router import AgentRouter
from core.logs import logger


def main() -> None:
    """
    TrackFlow AI CLI Entry Point.
    """

    agent_router = AgentRouter()

    print("\n🚀 Welcome to TrackFlow AI")
    print("Type 'exit' to quit.\n")

    while True:
        try:
            user_input = input("You: ").strip()

            if not user_input:
                continue

            if user_input.lower() in {"exit", "quit", "bye", "goodbye"}:
                print("\n👋 Goodbye!")
                break

            response = agent_router.invoke(user_input)

            print("\nTrackFlow AI:")

            if isinstance(response, dict):
                messages = response.get("messages", [])

                if messages:
                    print(messages[-1].content)
                else:
                    print(response)

            else:
                print(response)

            print()

        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            break

        except Exception as exc:
            logger.exception("Agent execution failed")

            print(f"\n❌ Error: {str(exc)}\n")


if __name__ == "__main__":
    main()











# import uvicorn
# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware

# from app.core.settings import port
# from app.api.api_routers import router
# # from app.api.routes.assistant import router as assistant_router
# # from app.api.routes.trackers import router as trackers_router
# # from app.api.routes.watchlist import router as watchlist_router

# app = FastAPI(title="TrackFlow AI")

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# app.include_router(router, prefix="/api", tags=["Health Check"])
# # app.include_router(trackers_router, prefix="/api/v1", tags=["Trackers"])
# # app.include_router(assistant_router, prefix="/api/v1", tags=["Assistant"])
# # app.include_router(watchlist_router, prefix="/api/v1", tags=["Watchlist"])


# if __name__ == "__main__":
#     uvicorn.run("main:app", host="localhost", port=port, reload=False)