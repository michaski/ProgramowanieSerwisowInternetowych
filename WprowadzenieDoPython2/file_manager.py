class FileManager:
    file_name = ""

    def __init__(self, file_name):
        self.file_name = file_name

    def read_file(self):
        uchwyt = open(self.file_name)
        dane = uchwyt.read()
        uchwyt.close()
        return dane

    def update_file(self, text_data):
        uchwyt = open(self.file_name, 'w', encoding='utf-8')
        uchwyt.write(text_data)
        uchwyt.close()
