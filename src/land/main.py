from fastapi import FastAPI, File, UploadFile

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/{namespace}")
async def get_repo(namespace: str):
    return {"message": f"listing namespaces in {namespace}"}


@app.get("/{namespace}/{environment}")
async def get_repo(namespace: str, environment: str):
    return {"message": f"listing checkpoints for {namespace}/{environment}"}


@app.get("/{namespace}/{environment}/{checkpoint}")
async def get_repo(namespace: str, environment: str, checkpoint: str):
    return {"message": f"getting checkpoint {checkpoint} {namespace}/{environment}"}


@app.post("/{namespace}/{environment}/{checkpoint}")
async def post_repo(namespace: str, environment: str, checkpoint: str, file: UploadFile = File(...)):
    return {"message": f"uploading checkpoint {checkpoint} {namespace}/{environment}"}

