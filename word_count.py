#!/usr/local/bin/python3

import os
import sys
import pprint

def everyWordCount(filename):
    """
    This function takes filename as one of the arguments from 
    the command line and prints count of each word in that
    file.
    """
    # count of every word is stored in the dictionary
    word_dict = {}
    f = open(filename, "r")
    for line in f:
        word_list = line.split()
        for word in word_list:
            if word in word_dict.keys():
                word_dict[word] += 1
            else:
                word_dict[word] = 1
    return word_dict


# filename is given from command line as the first arugument
filename = sys.argv[1]
pprint.pprint(everyWordCount(filename))