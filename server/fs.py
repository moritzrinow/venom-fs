import os
import shutil
import ntpath
from server.cache import FileCache

class FileService(object):

  def __init__(self, mount='data'):
    self.root = mount
    self.cache = FileCache()

  def valid_path(self, path):
    if ntpath.isabs(path):
      return False

    return True

  def has_file(self, path):
    full_path = ntpath.join(self.root, path)
    return ntpath.isfile(full_path)

  def get_file(self, path):
    full_path = ntpath.join(self.root, path)
    if not ntpath.isfile(full_path):
      return None

    if self.cache.has(full_path):
      return self.cache.get(full_path)
    
    with open(full_path, "rb") as f:
      data = f.read()

    self.cache.put(full_path, data)
    return data

  def put_file(self, path, data):
    full_path = ntpath.join(self.root, path)
    os.makedirs(ntpath.dirname(full_path), exist_ok=True)

    with open(full_path, "wb") as f:
      f.write(data)

    self.cache.put(full_path, data)

  def del_file(self, path):
    full_path = ntpath.join(self.root, path)

    if ntpath.isfile(full_path):
      os.remove(full_path)
      self.cache.pop(full_path)

  def has_dir(self, path):
    full_path = ntpath.join(self.root, path)
    return ntpath.isdir(full_path)

  def put_dir(self, path):
    full_path = ntpath.join(self.root, path)

    if not ntpath.isdir(full_path):
      os.mkdir(path)

  def del_dir(self, path):
    full_path = ntpath.join(self.root, path)

    if ntpath.isdir(full_path):
      shutil.rmtree(full_path)

  def list_dir(self, path):
    full_path = ntpath.join(self.root, path)

    if not ntpath.isdir(full_path):
      return None

    dir = next(os.walk(full_path))[1]
    return dir

  def list_file(self, path):
    full_path = ntpath.join(self.root, path)

    if not ntpath.isdir(full_path):
      return None

    files = next(os.walk(full_path))[2]
    return files
