# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 11:53:28 2013

@author: ramaswamy.tiruchirap
"""


import fnmatch
import os

def seach_files(src,match) :
    matches = []
    for root, dirnames, filenames in os.walk(src):
        for filename in fnmatch.filter(filenames, match):
            matches.append(os.path.join(root, filename))

    return matches
    
    
