# -*- coding: utf-8 -*-
import fnmatch,os
from sys import modules
import time, os, stat
import datetime

def delete_module(modname, paranoid=None):
    try:
        thismod = modules[modname]
    except KeyError:
        raise ValueError(modname)
    these_symbols = dir(thismod)
    if paranoid:
        try:
            paranoid[:]  # sequence support
        except:
            raise ValueError('must supply a finite list for paranoid')
        else:
            these_symbols = paranoid[:]
    del modules[modname]
    for mod in modules.values():
        try:
            delattr(mod, modname)
        except AttributeError:
            pass
        if paranoid:
            for symbol in these_symbols:
                if symbol[:2] == '__':  # ignore special symbols
                    continue
                try:
                    delattr(mod, symbol)
                except AttributeError:
                    pass

def search_files(src,match) :
    matches = []
    for root, dirnames, filenames in os.walk(src):
        for filename in fnmatch.filter(filenames, match):
            matches.append(os.path.join(root, filename))
    return matches

def reimport(modname) :
    delete_module(modname)
    import modname

def get_modification_time(file) :
    if os.path.exists(file):
        mod_time_flt=os.stat(file).st_mtime
        mod_time = datetime.datetime.fromtimestamp(mod_time_flt)
        
    else :
        mod_time =''
    return mod_time

def flatten(x):
    result = []
    for el in x:
        if hasattr(el, "__iter__") and not isinstance(el, basestring):
            result.extend(flatten(el))
        else:
            result.append(el)
    return result

def file_age_in_seconds(pathname):
    return time.time() - os.stat(pathname)[stat.ST_MTIME]


def main():
    pass

if __name__ == '__main__':
    main()
