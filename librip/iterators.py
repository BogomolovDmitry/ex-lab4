import itertools

# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):
        self.items = iter(items) if isinstance(items, list) else items
        self.ignore_case = False
        self.duplicates = []
        self.ignore_case = kwargs.get('ignore_case', False)

    def __next__(self):
        while True:
            try:
                cur = next(self.items)
                if isinstance(cur, str) and self.ignore_case is True:
                    cur_check = cur.upper()
                else:
                    cur_check = cur

                if not cur_check in self.duplicates:
                    self.duplicates.append(cur_check)
                    return cur
            except Exception:
                raise StopIteration

    def __iter__(self):
        return self
