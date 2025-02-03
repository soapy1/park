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
$ curl -i -X POST -H "Content-Type: multipart/form-data" -F "file=@sample/1bc3a3a434454437a9f72061672b8189" http://localhost:8000/my-namespace/my-environment/1bc3a3a434454437a9f72061672b8189 
```

## Retrieving

```bash
# list all namespaces
$ curl -i http://localhost:8000/namespaces

# list all environments in a namespace
$ curl -i http://localhost:8000/my-namespace/

# list all checkpoints in an environment
$ curl -i http://localhost:8000/my-namespace/my-environment/

# retrieve a checkpoint
$ curl -i http://localhost:8000/my-namespace/my-environment/1bc3a3a434454437a9f72061672b8189
```
