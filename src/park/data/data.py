import os


class DataDir:
    def __init__(self, path: str):
        self.root_path = path
        if not os.path.exists(self.root_path):
            os.makedirs(self.root_path)

    def _list_dir(self, path: str):
        target_path = os.path.join(self.root_path, path)
        if os.path.exists(target_path):
            return os.listdir(target_path)
        else:
            return []

    def _get(self, path: str):
        target_path = os.path.join(self.root_path, path)
        if os.path.exists(target_path):
            with open(target_path, "rb") as f:
                return f.read()
        else:
            return None

    def _put(self, path: str, data: bytes):
        target_path = os.path.join(self.root_path, path)
        os.makedirs(os.path.dirname(target_path), exist_ok=True)
        with open(target_path, "wb") as f:
            f.write(data)

    def list_namespaces(self):
        files = self._list_dir("")
        return [f for f in files if os.path.isdir(os.path.join(self.root_path, f))]

    def list_environments(self, namespace: str):
        files = self._list_dir(namespace)
        return [f for f in files if os.path.isdir(os.path.join(self.root_path, namespace, f))]
    
    def list_checkpoints(self, namespace: str, environment: str):
        files = self._list_dir(os.path.join(namespace, environment))
        return [f for f in files if os.path.isfile(os.path.join(self.root_path, namespace, environment, f))]

    def write_checkpoint(self, namespace: str, environment: str, checkpoint: str, data: bytes):
        self._put(os.path.join(namespace, environment, checkpoint), data)

    def read_checkpoint(self, namespace: str, environment: str, checkpoint: str):
        return self._get(os.path.join(namespace, environment, checkpoint))
