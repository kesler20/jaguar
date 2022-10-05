
class File(object):

    def __init__(self, filename: str, mode : str):
        self.filename = filename
        self.mode = mode
    
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_value, exc_tracebac):
        self.file.close()
    
# this can be consumed as
if __name__ == "__main__":
    
    with File("test_file.txt", "w") as f:
        f.write("test")

