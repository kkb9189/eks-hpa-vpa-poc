from time import perf_counter

from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello from EKS"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/cpu")
def cpu():
    start = perf_counter()
    deadline = start + 3.0
    iterations = 0
    value = 1

    while perf_counter() < deadline:
        value = (value * 1664525 + 1013904223) % (2**32)
        iterations += 1

    return {
        "message": "CPU work completed",
        "duration_seconds": round(perf_counter() - start, 2),
        "iterations": iterations,
    }
