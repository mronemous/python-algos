import os


class BigFileReader:
    file = None

    def __init__(self, path, filter_index=None, filter_value=None):
        try:
            self.filter_index = filter_index
            self.filter_value = filter_value

            stats = os.stat(path)
            if stats.st_size == 0:
                return

            print("opening file")
            self.file = open(path, encoding='utf8')
        except FileNotFoundError:
            print("Bad file path {0}".format(path))

    def lazy_read(self):
        if not self.file:
            return

        for row in self.file:
            if row is not None:
                split_row = row.split(",")
                if self.filter_index is not None and self.filter_value is not None:
                    if split_row[self.filter_index] == self.filter_value:
                        yield split_row
                    else:
                        continue
                else:
                    yield split_row
            else:
                return

        return

    def read(self):
        for row in self.lazy_read():
            print("{0}".format(row))

        if self.file is not None:
            print("closing file")
            self.file.close()
