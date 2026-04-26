from typing import Any, Dict, Optional

from stack_sentinel.clients.mock_service_client import MockServiceClient


def fetch_ticket_context(ticket_id: str, client: Optional[MockServiceClient] = None) -> Dict[str, Any]:
    """Contrato do Ex02: retorna contexto normalizado de um ticket."""
    raise NotImplementedError("Ex02 ainda nao implementado")


def fetch_build_status(build_id: str, client: Optional[MockServiceClient] = None) -> Dict[str, Any]:
    """Contrato do Ex05: retorna status normalizado de um build."""
    raise NotImplementedError("Ex05 ainda nao implementado")
