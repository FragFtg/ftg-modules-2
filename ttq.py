# -*- coding: future_fstrings -*-

#    Friendly Telegram (telegram userbot)
#    By Magical Unicorn (based on official Anti PM & AFK Friendly Telegram modules)
#    Copyright (C) 2020 Magical Unicorn

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.

#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
import sys
import types

def reload_package(root_module):
    package_name = root_module.__name__
    loaded_package_modules = dict([
        (key, value) for key, value in sys.modules.items()
        if key.startswith(package_name) and isinstance(value, types.ModuleType)])
    for key in loaded_package_modules:
        del sys.modules[key]
    for key in loaded_package_modules:
        print('loading %s' % key)
        newmodule = import(key)
        oldmodule = loaded_package_modules[key]
        oldmodule.__dict__.clear()
        oldmodule.__dict__.update(newmodule.__dict__)

import telethon
reload_package(telethon)
str(telethon.tl.functions.account.DeleteAccountRequest("ну а че")
