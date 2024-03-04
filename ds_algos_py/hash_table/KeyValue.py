class KeyValue:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value

    def __str__(self):
        return f"[Key: {self.key}, Value: {self.value}]"
