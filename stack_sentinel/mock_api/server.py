import argparse
from typing import Any, Dict, Optional

from stack_sentinel.data_loader import find_by_id, find_doc, find_service, load_collection


def resolve_mock_route(path: str) -> tuple[int, Dict[str, Any]]:
    """Resolve rotas da mock API sem subir servidor.

    Esta funcao existe para smoke tests rapidos e para manter os testes do
    scaffolding independentes de rede. O servidor real abaixo expoe as mesmas
    rotas usando FastAPI.
    """
    parts = [part for part in path.strip("/").split("/") if part]

    if path == "/health":
        return 200, {"ok": True, "service": "stack-sentinel-mock-api"}

    if path == "/tickets":
        return 200, {"ok": True, "data": load_collection("tickets")}
    if path == "/builds":
        return 200, {"ok": True, "data": load_collection("builds")}
    if path == "/docs":
        return 200, {"ok": True, "data": load_collection("docs")}
    if path == "/services":
        return 200, {"ok": True, "data": load_collection("services")}
    if path == "/incidents":
        return 200, {"ok": True, "data": load_collection("incidents")}

    item: Optional[Dict[str, Any]] = None
    if len(parts) == 2 and parts[0] == "tickets":
        item = find_by_id("tickets", parts[1])
    elif len(parts) == 2 and parts[0] == "builds":
        item = find_by_id("builds", parts[1])
    elif len(parts) == 2 and parts[0] == "docs":
        item = find_doc(parts[1])
    elif len(parts) == 3 and parts[0] == "services" and parts[2] == "health":
        item = find_service(parts[1])
    elif len(parts) == 2 and parts[0] == "incidents":
        item = find_by_id("incidents", parts[1])

    if item is None:
        return 404, {"ok": False, "error": f"not found: {path}"}
    return 200, {"ok": True, "data": item}


def _payload_or_json_response(path: str):
    from fastapi.responses import JSONResponse

    status, payload = resolve_mock_route(path)
    if status >= 400:
        return JSONResponse(status_code=status, content=payload)
    return payload


def create_app():
    """Cria a aplicacao FastAPI da mock API.

    A logica continua mockada: os endpoints apenas leem dados locais em JSON.
    O formato HTTP, porem, e realista o suficiente para os alunos chamarem com
    cliente HTTP, browser, curl ou docs interativas do FastAPI.
    """
    try:
        from fastapi import FastAPI
    except ImportError as exc:
        raise RuntimeError(
            "FastAPI nao esta instalado. Rode `python run.py setup` antes de subir a mock API."
        ) from exc

    app = FastAPI(
        title="Stack Sentinel Mock API",
        version="0.1.0",
        description="Mock API local para tickets, builds, docs, servicos e incidentes.",
    )

    @app.get("/health")
    def health():
        return _payload_or_json_response("/health")

    @app.get("/tickets")
    def list_tickets():
        return _payload_or_json_response("/tickets")

    @app.get("/tickets/{ticket_id}")
    def get_ticket(ticket_id: str):
        return _payload_or_json_response(f"/tickets/{ticket_id}")

    @app.get("/builds")
    def list_builds():
        return _payload_or_json_response("/builds")

    @app.get("/builds/{build_id}")
    def get_build(build_id: str):
        return _payload_or_json_response(f"/builds/{build_id}")

    @app.get("/docs")
    def list_docs():
        return _payload_or_json_response("/docs")

    @app.get("/docs/{slug}")
    def get_doc(slug: str):
        return _payload_or_json_response(f"/docs/{slug}")

    @app.get("/services")
    def list_services():
        return _payload_or_json_response("/services")

    @app.get("/services/{service_name}/health")
    def get_service_health(service_name: str):
        return _payload_or_json_response(f"/services/{service_name}/health")

    @app.get("/incidents")
    def list_incidents():
        return _payload_or_json_response("/incidents")

    @app.get("/incidents/{incident_id}")
    def get_incident(incident_id: str):
        return _payload_or_json_response(f"/incidents/{incident_id}")

    return app


def run_server(host: str = "127.0.0.1", port: int = 8000) -> None:
    try:
        import uvicorn
    except ImportError as exc:
        raise RuntimeError(
            "Uvicorn nao esta instalado. Rode `python run.py setup` antes de subir a mock API."
        ) from exc

    print(f"Stack Sentinel mock API running at http://{host}:{port}")
    print(f"Interactive docs at http://{host}:{port}/docs")
    uvicorn.run(create_app(), host=host, port=port)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8000)
    args = parser.parse_args()
    run_server(args.host, args.port)


try:
    app = create_app()
except RuntimeError:
    app = None


if __name__ == "__main__":
    main()
