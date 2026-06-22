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
# app.include_router(trackers_router, prefix="/api/v1", tags=["Trackers"])
# app.include_router(assistant_router, prefix="/api/v1", tags=["Assistant"])
# app.include_router(watchlist_router, prefix="/api/v1", tags=["Watchlist"])

from src import test

if __name__ == "__main__":
    test.run_test2()
    # uvicorn.run("main:app", host="localhost", port=port, reload=False)