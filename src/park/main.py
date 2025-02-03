import os
from fastapi import FastAPI, File, UploadFile

from park.data.data import DataDir

app = FastAPI()
data_dir = DataDir(os.environ.get("park_DATA_DIR", "/tmp/park/data"))

@app.get("/namespaces")
async def get_namespaces():
    namespaces = data_dir.list_namespaces()
    return {
        "data": {
            "namespaces": namespaces,
        }
    }

@app.get("/{namespace}")
async def get_environments(namespace: str):
    environments = data_dir.list_environments(namespace)
    return {
        "data": {
            "namespace": namespace,
            "environments": environments,
        }
    }


@app.get("/{namespace}/{environment}")
async def get_checkpoints(namespace: str, environment: str):
    checkpoints = data_dir.list_checkpoints(namespace, environment)
    return {
        "data": {
            "namespace": namespace,
            "environment": environment,
            "checkpoints": checkpoints,
        }
    }


@app.get("/{namespace}/{environment}/{checkpoint}")
async def get_checkpoint(namespace: str, environment: str, checkpoint: str):
    checkpoint_data = data_dir.read_checkpoint(namespace, environment, checkpoint)
    return {
        "data": {
            "namespace": namespace,
            "environment": environment,
            "checkpoint": checkpoint,
            "checkpoint_data": checkpoint_data
        }
    }


@app.post("/{namespace}/{environment}/{checkpoint}")
async def upload_checkpoint(namespace: str, environment: str, checkpoint: str, file: UploadFile = File(...)):
    data_dir.write_checkpoint(namespace, environment, checkpoint, file.file.read())
    return {"message": f"uploading checkpoint '{checkpoint}' in {namespace}/{environment}"}
