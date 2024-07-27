import _pickle


def read_from_file(filename):
    try:
        with open(filename, "rb") as file:
            filedata = _pickle.load(file)
            file.close()
            return filedata

    except Exception as err:
        pass


def write_to_file(filename, data):
    try:
        with open(filename, "wb") as file:
            _pickle.dump(data, file)
        file.close()
    except Exception as err:
        pass
