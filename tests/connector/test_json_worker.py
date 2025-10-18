import os
import tempfile
import json
from typing import Dict

from src.connector.json_worker import JSONWorker


def test_add_vacancy_data(tmp_path, vacancy_data1: Dict[str, str | Dict]) -> None:
    """Проверяем работу метода add_vacancy_data"""
    file_path = tmp_path / "test.json"
    worker = JSONWorker(str(file_path))
    worker.add_vacancy_data(vacancy_data1)

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    assert isinstance(data, list)
    assert len(data) == 1
    assert data[0]["name"] == "Python Developer"
