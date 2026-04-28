from typing import Any, Dict, Optional

from stack_sentinel.clients.mock_service_client import MockServiceClient


def fetch_ticket_context(ticket_id: str, client: Optional[MockServiceClient] = None) -> Dict[str, Any]:
    """Contrato do Ex02: retorna contexto normalizado de um ticket."""
    client = client or MockServiceClient()
    if ticket_id == (""):
        return {"ok": False, "error": "Ticket inválido"}

    try:
        response = client.get_ticket(ticket_id)
        if response["ok"]:
            data = response["data"]
            return {
                "ok": True,
                "id": data["id"],
                "summary": data["summary"],
                "severity": data["severity"],
                "service": data["service"],
                "status": data["status"],
                "build_id": data["build_id"]
            }
        else:
           return {"ok": False, "error": "Não encontrado"}
    except Exception:
        return {"ok": False, "error": "Não encontrado"}

def fetch_build_status(build_id: str, client: Optional[MockServiceClient] = None) -> Dict[str, Any]:
    """Contrato do Ex05: retorna status normalizado de um build."""
    raise NotImplementedError("Ex05 ainda nao implementado")
