import json
from functools import lru_cache
from pathlib import Path
from typing import Any, Dict, List, Optional


DATA_DIR = Path(__file__).resolve().parent / "data"


@lru_cache(maxsize=None)
def load_collection(name: str) -> List[Dict[str, Any]]:
    path = DATA_DIR / f"{name}.json"
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def find_by_id(collection: str, item_id: str, id_field: str = "id") -> Optional[Dict[str, Any]]:
    expected = item_id.lower()
    for item in load_collection(collection):
        value = str(item.get(id_field, "")).lower()
        if value == expected:
            return dict(item)
    return None


def find_doc(slug: str) -> Optional[Dict[str, Any]]:
    return find_by_id("docs", slug, id_field="slug")


def find_service(service_name: str) -> Optional[Dict[str, Any]]:
    return find_by_id("services", service_name, id_field="service")

