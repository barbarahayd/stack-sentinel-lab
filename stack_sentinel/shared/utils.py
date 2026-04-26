import re
from typing import Optional


def extract_ticket_id(text: str) -> Optional[str]:
    match = re.search(r"\bTCK-\d+\b", text.upper())
    return match.group(0) if match else None


def extract_build_id(text: str) -> Optional[str]:
    match = re.search(r"\bBLD-\d+\b", text.upper())
    return match.group(0) if match else None


def normalize_text(text: str) -> str:
    return " ".join(text.strip().split())

