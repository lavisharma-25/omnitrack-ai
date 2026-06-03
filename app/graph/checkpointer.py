import sqlite3
from langgraph.checkpoint.sqlite import SqliteSaver

from app.config import chat_history_path

_checkpointer = None

def get_checkpointer():
    global _checkpointer

    if _checkpointer is None:
        chat_history_path.mkdir(parents=True, exist_ok=True)
        path = chat_history_path / "memory.db"
        conn = sqlite3.connect(path, check_same_thread=False)
        _checkpointer = SqliteSaver(conn)

    return _checkpointer


def reset_checkpointer():
    global _checkpointer

    if _checkpointer and hasattr(_checkpointer, "conn"):
        _checkpointer.conn.close()

    _checkpointer = None