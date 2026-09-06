import os
import time
from random import random
from fastapi import FastAPI, Response
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST

app = FastAPI(title="SRE Reliability Lab", version="1.0.0")
REQUESTS = Counter("http_requests_total", "HTTP requests", ["path", "method", "status"])
LATENCY = Histogram("http_request_duration_seconds", "Request latency", ["path"])
FAULT_MODE = os.getenv("FAULT_MODE", "none")

@app.get("/healthz")
def healthz():
    return {"status": "ok"}

@app.get("/readyz")
def readyz():
    return {"status": "ready"}

@app.get("/api")
def api():
    start = time.perf_counter()
    status = "200"
    try:
        if FAULT_MODE == "latency":
            time.sleep(1.5)
        if FAULT_MODE == "error" or (FAULT_MODE == "random-error" and random() < 0.5):
            status = "503"
            REQUESTS.labels("/api", "GET", status).inc()
            return Response("dependency unavailable", status_code=503)
        REQUESTS.labels("/api", "GET", status).inc()
        return {"service": "reliability-lab", "status": "healthy"}
    finally:
        LATENCY.labels("/api").observe(time.perf_counter() - start)

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
