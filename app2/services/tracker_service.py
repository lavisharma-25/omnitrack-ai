from pathlib import Path
from uuid import uuid4

import pandas as pd

from app.core.settings import settings
from app.exceptions.excel_errors import (
    RecordNotFoundError,
    TrackerAlreadyExistsError,
    TrackerNotFoundError,
)
from app.services.excel_service import ExcelService




class TrackerService:
    """
    Business logic for tracker management.
    """

    def __init__(self):
        self.storage_dir = settings.TRACKERS_DIR

    def _tracker_path(
        self,
        tracker_name: str,
    ) -> Path:
        return self.storage_dir / f"{tracker_name}.xlsx"

    def create_tracker(
        self,
        tracker_name: str,
        columns: list[str],
    ) -> str:

        file_path = self._tracker_path(tracker_name)

        if file_path.exists():
            raise TrackerAlreadyExistsError(
                tracker_name
            )

        base_columns = [
            "record_id",
            *columns,
        ]

        ExcelService.create_excel(
            file_path=file_path,
            columns=base_columns,
        )

        return f"Tracker '{tracker_name}' created successfully."

    def list_trackers(
        self,
    ) -> list[str]:

        return [
            file.stem
            for file in self.storage_dir.glob("*.xlsx")
        ]

    def add_record(
        self,
        tracker_name: str,
        data: dict,
    ) -> str:

        file_path = self._tracker_path(
            tracker_name
        )

        if not file_path.exists():
            raise TrackerNotFoundError(
                tracker_name
            )

        df = ExcelService.read_excel(
            file_path
        )

        record = {
            "record_id": str(uuid4()),
            **data,
        }

        df = pd.concat(
            [
                df,
                pd.DataFrame([record]),
            ],
            ignore_index=True,
        )

        ExcelService.write_excel(
            file_path,
            df,
        )

        return record["record_id"]

    def list_records(
        self,
        tracker_name: str,
    ) -> list[dict]:

        file_path = self._tracker_path(
            tracker_name
        )

        if not file_path.exists():
            raise TrackerNotFoundError(
                tracker_name
            )

        df = ExcelService.read_excel(
            file_path
        )

        return df.fillna("").to_dict(
            orient="records"
        )

    def delete_record(
        self,
        tracker_name: str,
        record_id: str,
    ) -> str:

        file_path = self._tracker_path(
            tracker_name
        )

        if not file_path.exists():
            raise TrackerNotFoundError(
                tracker_name
            )

        df = ExcelService.read_excel(
            file_path
        )

        if record_id not in df[
            "record_id"
        ].astype(str).values:
            raise RecordNotFoundError(
                record_id
            )

        df = df[
            df["record_id"].astype(str)
            != record_id
        ]

        ExcelService.write_excel(
            file_path,
            df,
        )

        return (
            f"Record '{record_id}' "
            f"deleted successfully."
        )

    def update_record(
        self,
        tracker_name: str,
        record_id: str,
        updates: dict,
    ) -> str:

        file_path = self._tracker_path(
            tracker_name
        )

        if not file_path.exists():
            raise TrackerNotFoundError(
                tracker_name
            )

        df = ExcelService.read_excel(
            file_path
        )

        mask = (
            df["record_id"]
            .astype(str)
            == record_id
        )

        if not mask.any():
            raise RecordNotFoundError(
                record_id
            )

        for column, value in updates.items():
            if column in df.columns:
                df.loc[
                    mask,
                    column,
                ] = value

        ExcelService.write_excel(
            file_path,
            df,
        )

        return (
            f"Record '{record_id}' "
            f"updated successfully."
        )