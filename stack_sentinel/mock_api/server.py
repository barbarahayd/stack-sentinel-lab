import argparse
import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from typing import Any, Dict, Optional
from urllib.parse import urlparse

from stack_sentinel.data_loader import find_by_id, find_doc, find_service


def _json_response(handler: BaseHTTPRequestHandler, status: int, payload: Dict[str, Any]) -> None:
    body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    handler.send_response(status)
    handler.send_header("Content-Type", "application/json; charset=utf-8")
    handler.send_header("Content-Length", str(len(body)))
    handler.end_headers()
    handler.wfile.write(body)


def resolve_mock_route(path: str) -> tuple[int, Dict[str, Any]]:
    parts = [part for part in path.strip("/").split("/") if part]
    if path == "/health":
        return 200, {"ok": True, "service": "stack-sentinel-mock-api"}

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


class StackSentinelHandler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        parsed = urlparse(self.path)
        status, payload = resolve_mock_route(parsed.path)
        _json_response(self, status, payload)

    def log_message(self, format: str, *args: object) -> None:
        return


def run_server(host: str = "127.0.0.1", port: int = 8000) -> None:
    server = ThreadingHTTPServer((host, port), StackSentinelHandler)
    print(f"Stack Sentinel mock API running at http://{host}:{port}")
    print("Press Ctrl+C to stop.")
    server.serve_forever()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8000)
    args = parser.parse_args()
    run_server(args.host, args.port)


if __name__ == "__main__":
    main()

