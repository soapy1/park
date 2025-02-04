# Park

Goal of this project is to create a simple server for uploading and retrieving DOF checkpoints.

## Getting Started

Install the dependencies:
```bash
$ pixi install
```

Run the server:
```bash
$ pixi run dev
```

Or, using docker
```
$ docker build -t park:local .

$ docker run -p 8000:8000 -it park:local
```

## Uploading

```bash
# upload a file
$ curl -i -X POST -H "Content-Type: multipart/form-data" -F "file=@sample/1bc3a3a4" http://localhost:8000/my-namespace/my-environment/1bc3a3a4/file

# upload a json blob
$ curl -i -X POST -H "Content-Type: application/json" -d '{"data": "hello"}' http://localhost:8000/my-namespace/other-env/data/json
```

## Retrieving

```bash
# list all namespaces
$ curl http://localhost:8000/namespaces

# list all environments in a namespace
$ curl http://localhost:8000/my-namespace/

# list all checkpoints in an environment
$ curl http://localhost:8000/my-namespace/my-environment/

# retrieve a checkpoint
$ curl http://localhost:8000/my-namespace/my-environment/1bc3a3a4

# retrieve a checkpoint
$ curl http://localhost:8000/my-namespace/other-env/data
```
