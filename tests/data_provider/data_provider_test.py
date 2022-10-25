class DataProviderTest:
    def __init__(self, file_name):
        self.file_name = file_name

    def __enter__(self):
        return self.file_name

    def __exit__(self):
        pass
        