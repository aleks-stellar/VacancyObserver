from typing import Dict, List

import pytest


@pytest.fixture
def vacancies_list() -> Dict[str, List]:
    """Мок данных с API: разные минимальные зарплаты"""
    return {"items": [
        {"name": "Python Dev 1", "alternate_url": "url1", "salary": {"from": 120000, "to": 150000},
         "snippet": {"requirement": "Req1"}},
        {"name": "Python Dev 2", "alternate_url": "url2", "salary": {"from": 100000, "to": 130000},
         "snippet": {"requirement": "Req2"}},
        {"name": "Python Dev 3", "alternate_url": "url3", "salary": {"from": 200000, "to": 250000},
         "snippet": {"requirement": "Req3"}},
        {"name": "Python Dev 4", "alternate_url": "url4", "salary": {"from": 90000, "to": 120000},
         "snippet": {"requirement": "Req4"}},
    ]}
