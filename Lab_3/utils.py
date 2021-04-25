from timeit import default_timer
from collections import namedtuple
from os import walk
from os import stat
from os import path


def profile(func):
    def wrapper():
        start = default_timer()
        func()
        print("Execution time is {} seconds".format(default_timer() - start))
    return wrapper


class timer:
    def __init__(self):
        self._start = 0

    def __enter__(self):
        self._start = default_timer()
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print("Execution time is {} seconds".format(default_timer() - self._start))


def calculate_stats(path_):
    try:
        file_number = 0
        file_size = 0
        for new_path, dirs, files in walk(path_):
            file_number += len(files)
            file_size += sum(stat(path.join(new_path, file)).st_size for file in files)
        return namedtuple('DirectoryStats', ['total_files', 'total_size'])(file_number, file_size)
    except FileNotFoundError:
        raise FileNotFoundError("That directory does not exist u dumb")
