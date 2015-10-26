from __future__ import unicode_literals
from fileCatcher import _FileCatcher


class Windows2003Files(_FileCatcher):
    def __init__(self, params):
        super(Windows2003Files, self).__init__(params)

    def _changeroot(self, dir):
        return dir

    def _list_files(self):
        return super(Windows2003Files, self)._list_files

    def csv_print_infos_files(self):
        super(Windows2003Files, self)._csv_infos_fs(self._list_files())
