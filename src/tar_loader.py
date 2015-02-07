# -*- coding:utf-8 -*-
#
# Copyright (C) 2015  Michell Stuttgart

# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option)
# any later version.

# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
# more details.

# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.

import tarfile


from PyQt4.QtCore import QCoreApplication

from loader import Loader
import progress_dialog
from page import Page
from utility import Utility


class TarLoader(Loader):

    def __init__(self):
        super(TarLoader, self).__init__()

    def load(self, file_name):

        file_name = str(file_name)

        if not self.is_tar_file(file_name):
            return False

        try:
            tar = tarfile.open(file_name, 'r')
        except tarfile.CompressionError, err:
            print '%20s  %s' % (file_name, err)
            return False

        name_list = tar.getnames()
        name_list.sort()

        # dlg = progress_dialog.ProgressDialog("Please Wait", "Cancel", 0,
        #                                      len(name_list))
        # dlg.setWindowTitle('Loading Comic File')
        # dlg.show()
        #
        # count_page = 1
        for name in name_list:
            # file_extension = Utility.get_file_extension(name)

            # dlg.setValue(name_list.index(name))
            # QCoreApplication.instance().processEvents()
            # if dlg.wasCanceled():
            #     raise GeneratorExit

            if not tar.getmember(name).isdir():
                if Utility.get_file_extension(name).lower() in self.extension:

                    data = None
                    try:
                        data = tar.extractfile(name).read()
                    except tarfile.ExtractError, err:
                        print '%20s  %s' % (name, err)
                    except tarfile.ReadError, err:
                        print '%20s  %s' % (name, err)

                    if data:
                        self.data.append({'data': data, 'name': name})
                        # count_page += 1

        tar.close()

        return True

    # def _load_core(self, pages, file_name):
    #
    #     file_name = str(file_name)
    #
    #     try:
    #         tar = tarfile.open(file_name, 'r')
    #     except:
    #         raise tarfile.CompressionError
    #
    #     name_list = tar.getnames()
    #     name_list.sort()
    #
    #     dlg = progress_dialog.ProgressDialog("Please Wait", "Cancel", 0,
    #                                          len(name_list))
    #     dlg.setWindowTitle('Loading Comic File')
    #     dlg.show()
    #
    #     count_page = 1
    #     for name in name_list:
    #         _, file_extension = os.path.splitext(name)
    #
    #         dlg.setValue(name_list.index(name))
    #         QCoreApplication.instance().processEvents()
    #         if dlg.wasCanceled():
    #             raise GeneratorExit
    #
    #         if not tar.getmember(
    #                 name).isdir() and file_extension.lower() in self.extension:
    #
    #             data = None
    #             try:
    #                 data = tar.extractfile(name).read()
    #             except tarfile.ExtractError, err:
    #                 print '%20s  %s' % (name, err)
    #             except tarfile.ReadError, err:
    #                 print '%20s  %s' % (name, err)
    #
    #             if data:
    #                 pages.append(Page(data, name, count_page))
    #                 count_page += 1
    #
    #     tar.close()

    @staticmethod
    def is_tar_file(file_name):
        return tarfile.is_tarfile(str(file_name))
