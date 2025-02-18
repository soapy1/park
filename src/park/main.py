import os
import yaml
from typing import Dict, Any
from fastapi import FastAPI, File, UploadFile, Body

from park.data.data import DataDir

app = FastAPI()
data_dir = DataDir(os.environ.get("PARK_DATA_DIR", "/tmp/park/data"))


@app.get("/status")
async def get_namespaces():
    return {
        "ok": "sure am"
    }


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
            "checkpoint_data": yaml.load(checkpoint_data, yaml.FullLoader)
        }
    }


@app.post("/{namespace}/{environment}/{checkpoint}/file")
async def upload_checkpoint(
    namespace: str,
    environment: str,
    checkpoint: str,
    file: UploadFile = File(...)
):
    data_dir.write_checkpoint(namespace, environment, checkpoint, file.file.read())
    return {"message": f"uploading checkpoint '{checkpoint}' in {namespace}/{environment}"}


@app.post("/{namespace}/{environment}/{checkpoint}/json")
async def upload_checkpoint_data(
    namespace: str,
    environment: str,
    checkpoint: str,
    data: Dict[str, Any] = Body(None),
):
    bytes_data = yaml.dump(data).encode("utf-8")
    data_dir.write_checkpoint(namespace, environment, checkpoint, bytes_data)
    return {"message": f"uploading checkpoint '{checkpoint}' in {namespace}/{environment}"}
