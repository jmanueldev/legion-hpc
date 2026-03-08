from fastapi import FastAPI
from legionx.telemetry import collect_telemetry
from pydantic import BaseModel
from typing import List

app = FastAPI(title="LegionX Telemetry Server")

class NodeTelemetry(BaseModel):
    node_name: str

@app.post("/telemetry/")
def report_telemetry(data: NodeTelemetry):
    metrics = collect_telemetry(data.node_name)
    return metrics

@app.get("/status/")
def cluster_status():
    # Example aggregated telemetry
    return {"status": "online"}
