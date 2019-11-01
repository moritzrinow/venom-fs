import os
import shutil
import platform
from .cache import FileCache

system = platform.system()

class FileService(object):

  def __init__(self, mount='', safe_paths=True):
    self.root = mount
    self.cache = FileCache()
    self.safe = safe_paths

  def _get_full_path(self, path):
    return os.path.join(self.root, path)

  def is_safe_path(self, path):
    # This function ensures that the path does not go outside the root directory

    if not self.safe:
      return True

    if os.path.isabs(path):
      return True

    full_path = os.path.join(self.root, path)
    norm_path = os.path.normpath(full_path)

    if full_path.startswith('..'):
      return False

    return True

  def has_file(self, path):
    full_path = self._get_full_path(path)
    return os.path.isfile(full_path)

  def get_file(self, path):
    full_path = self._get_full_path(path)
    if not os.path.isfile(full_path):
      return None

    if self.cache.has(full_path):
      return self.cache.get(full_path)
    
    with open(full_path, "rb") as f:
      data = f.read()

    self.cache.put(full_path, data)
    return data

  def put_file(self, path, data):
    full_path = self._get_full_path(path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)

    with open(full_path, "wb") as f:
      f.write(data)

    self.cache.put(full_path, data)

  def del_file(self, path):
    full_path = self._get_full_path(path)

    if os.path.isfile(full_path):
      os.remove(full_path)
      self.cache.pop(full_path)

  def has_dir(self, path):
    full_path = self._get_full_path(path)
    return os.path.isdir(full_path)

  def put_dir(self, path):
    full_path = self._get_full_path(path)

    if not os.path.isdir(full_path):
      os.mkdir(path)

  def del_dir(self, path):
    full_path = self._get_full_path(path)

    if os.path.isdir(full_path):
      shutil.rmtree(full_path)

  def list_dir(self, path):
    full_path = self._get_full_path(path)

    print(full_path)
    if not os.path.isdir(full_path):
      return None

    dir = next(os.walk(full_path))[1]
    return dir

  def list_file(self, path):
    full_path = self._get_full_path(path)

    if not os.path.isdir(full_path):
      return None

    files = next(os.walk(full_path))[2]
    return files
