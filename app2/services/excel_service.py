import pandas as pd
from pathlib import Path

from app.exceptions.excel_errors import ExcelOperationError


class ExcelService:
    """
    Handles all Excel operations.
    """

    @staticmethod
    def create_excel(file_path: Path, columns: list[str]) -> None:
        try:
            df = pd.DataFrame(columns=columns)
            df.to_excel(file_path, index=False)

        except Exception as exc:
            raise ExcelOperationError(f"Failed to create Excel file: {exc}") from exc

    @staticmethod
    def read_excel(file_path: Path) -> pd.DataFrame:
        try:
            return pd.read_excel(file_path)

        except Exception as exc:
            raise ExcelOperationError(f"Failed to read Excel file: {exc}") from exc

    @staticmethod
    def write_excel(file_path: Path, dataframe: pd.DataFrame) -> None:
        try:
            dataframe.to_excel(file_path, index=False)

        except Exception as exc:
            raise ExcelOperationError(f"Failed to write Excel file: {exc}") from exc