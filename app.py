from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from itertools import count
from typing import List

from flask import Flask, jsonify, redirect, render_template, request, url_for

app = Flask(__name__)


@dataclass
class AppService:
    id: int
    name: str
    runtime: str
    repo_url: str
    instances: int = 1
    status: str = "Running"
    created_at: datetime = field(default_factory=datetime.utcnow)


_id_counter = count(1)
_services: List[AppService] = []


@app.route("/")
def index() -> str:
    return render_template("index.html", services=_services)


@app.post("/apps")
def create_app() -> str:
    name = request.form.get("name", "").strip()
    runtime = request.form.get("runtime", "").strip() or "Python"
    repo_url = request.form.get("repo_url", "").strip()

    if not name:
        return redirect(url_for("index"))

    service = AppService(
        id=next(_id_counter),
        name=name,
        runtime=runtime,
        repo_url=repo_url or "-",
    )
    _services.append(service)
    return redirect(url_for("index"))


@app.post("/apps/<int:app_id>/scale")
def scale_app(app_id: int) -> str:
    instances = max(int(request.form.get("instances", 1)), 0)
    service = _get_service(app_id)
    if service:
        service.instances = instances
    return redirect(url_for("index"))


@app.post("/apps/<int:app_id>/toggle")
def toggle_app(app_id: int) -> str:
    service = _get_service(app_id)
    if service:
        service.status = "Stopped" if service.status == "Running" else "Running"
    return redirect(url_for("index"))


@app.post("/apps/<int:app_id>/delete")
def delete_app(app_id: int) -> str:
    global _services
    _services = [service for service in _services if service.id != app_id]
    return redirect(url_for("index"))


@app.get("/api/apps")
def api_apps() -> str:
    payload = [
        {
            "id": service.id,
            "name": service.name,
            "runtime": service.runtime,
            "repo_url": service.repo_url,
            "instances": service.instances,
            "status": service.status,
            "created_at": service.created_at.isoformat() + "Z",
        }
        for service in _services
    ]
    return jsonify(payload)


def _get_service(app_id: int) -> AppService | None:
    return next((service for service in _services if service.id == app_id), None)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
