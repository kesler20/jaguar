import os
from path import Path

class File(object):
    '''Object Description'''

    def __init__(self, filename) -> None:
        self.filename: str = filename

    def read(self) -> str:
        '''signature description'''
        with open(self.filename, "r") as file:
            content = file.read()
        return content

    def write(self, content: str) -> None:
        '''signature description'''
        with open(self.filename, "w") as file:
            file.write(content)

    def readlines(self) -> 'list[str]':
        '''signature description'''
        with open(self.filename, "w") as file:
            content = file.readlines()
        return content

    def writeline(self, content: str) -> None:
        '''signature description'''
        with open(self.filename, "w") as file:
            file.write(f"{content}\n")

    def read_line_by_condition(self, condition) -> 'list[str]':
        '''
        condition should be a function which is applied 
        to filter through the list of the lines of the file
        '''
        with open(self.filename, "w") as file:
            content = file.readlines()

        return list(filter(condition, content))

    def delete(self) -> None:
        '''signature description'''
        os.remove(self.filename)


class OperatingSystemInterface(object):
    '''
    you can access the interface like a resource manager such as
    ```python
    with OperatingSystemInterface(directory) as osi:
        osi.do_something()
    # alternatively if there are multiple calls that you want to make you can use
    osi = OperatingSystemInterface()
    with osi as oi:
        oi.system("echo hello world")
    ```
    '''

    def __init__(self, directory=os.getcwd()) -> None:
        self.directory: str = directory

    def __enter__(self) -> os:
        '''signature description'''
        os.chdir(self.directory)
        return os

    def __exit__(self, *args) -> os:
        '''signature description'''
        os.chdir(os.getcwd())

    def move_folder_resources(self, destination_path: str) -> None:
        '''the directory passed as a property will be used as a source path'''
        for resource in os.listdir(self.directory):
            destination_dir = os.path.join(destination_path, resource)
            source_dir = os.path.join(self.directory, resource)
            os.rename(source_dir, destination_dir)

    def read_word_in_directory(self, word: str) -> 'list[str]':
        '''signature description'''
        result = []
        for root, directories, file in os.walk(self.directory):
            for file in file:
                print(file)
                with open(file) as f:
                    content = f.read()
                    if content.find(word) != -1:
                        result.append(file)
                        
        return result


