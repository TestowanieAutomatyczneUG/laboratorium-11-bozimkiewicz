import os


class FileOperations:
    def read_files(self, file):
        with open(file, 'r') as f:
            content = f.read()
        return content

    def write_files(self, file, content):
        with open(file, 'w') as f:
            f.write(content)

    def delete_files(self, file):
        if os.path.isfile(file):
            os.remove(file)
        else:
            raise(Exception, 'File doesn\'t exist')