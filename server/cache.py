
class FileCache(object):

  def __init__(self, limit=1000):
    self.table = {}
    self.limit = limit

  def __del__(self):
    self.flush()

  def __len__(self):
    return len(self.table)

  def has(self, id):
    return id in self.table

  def get(self, id):
    return self.table.get(id)

  def put(self, id, data):
    if id in self.table:
      self.table[id] = data
    else:
      if len(self.table) >= self.limit:
        for key in self.table.keys():
          self.table.pop(key)
          break
      self.table[id] = data

  def pop(self, id):
    self.table.pop(id)

  def flush(self):
    self.table.clear()