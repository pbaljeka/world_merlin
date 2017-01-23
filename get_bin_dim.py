import numpy as np
import sys
import os
import binary_io
io_funcs = binary_io.BinaryIOCollection()
#need to make this better.. read in a file with phonelist etc. This is only for testing.

def get_items(infile):
    with open(infile, 'r') as f:
        itemlist=f.read().strip().split('___')
        itemlist.pop(-1)
        itemlist.insert(0,"0")
    return itemlist

def one_hot(number, max_size):
    """ Returns the one hot vector of a number, given the max"""
    b = np.zeros(max_size,dtype=float)
    b[number]=1.0
    return b


def get_binary_dim(infile, phonefile, statefile):
    """Makes binary vectors"""
    STATELIST=get_items(statefile)
    PHONELIST=get_items(phonefile)
    POSLIST=[0, 'aux','cc','content','det','in', 'md','pps','to','wp', 'punc']
    POS2LIST=['b','m','e']
    PRESENTLIST=[0, '+','-']
    PLACELIST=[0, 'a','b','d','g','l','p','v', '-']
    PLACE2LIST=[0,'a','d','l','s','-']
    PLACE3LIST=[0,'a','f','l','n','r','s','-']
    POSITIONLIST=[0, 'initial', 'single','final','mid']
    STRENGTHLIST=[0, 1, 2, 3, '-']
    STRENGTH2LIST=[0, '1', '3', '4']
    CODALIST =[0,'coda', 'onset']


    features=[STATELIST,
            STATELIST,
            STATELIST,
            PHONELIST,
            PRESENTLIST,
            PLACE3LIST,
            STRENGTHLIST,
            PLACE2LIST,
            STRENGTHLIST,
            PRESENTLIST,
            PLACELIST,
            PRESENTLIST,
            PHONELIST,
            PRESENTLIST,
            PLACE3LIST,
            STRENGTHLIST,
            PLACE2LIST,
            STRENGTHLIST,
            PRESENTLIST,
            PLACELIST,
            PRESENTLIST,
            'FLOAT',
            'FLOAT',
            'FLOAT',
            'FLOAT',
            POS2LIST,
            'FLOAT',
            'FLOAT',
            'FLOAT',
            'FLOAT',
            'FLOAT',
            'FLOAT',
            'FLOAT',
            'FLOAT',
            'FLOAT',
            'FLOAT',
            'FLOAT',
            'FLOAT',
            'FLOAT',
            CODALIST,
            CODALIST,
            CODALIST,
            'FLOAT',
            'FLOAT',
            'FLOAT',
            'FLOAT',
            STRENGTH2LIST,
            STRENGTH2LIST,
            POSITIONLIST,
            PHONELIST,
            PRESENTLIST,
            PLACE3LIST,
            STRENGTHLIST,
            PLACE2LIST,
            STRENGTHLIST,
            PRESENTLIST,
            PLACELIST,
            PRESENTLIST,
            'FLOAT',
            'FLOAT',
            POSLIST,
            POSLIST,
            POSLIST]
    
    final_list=[]
    with open(infile, 'r') as f:
        feat_list=f.readline().strip().split()
        for feat, list_name in enumerate(features):
                #print "DEBUG: ", feat+2, list_name, feat_list[feat+2]
            final_list.extend(get_element(feat_list[feat + 2], list_name))
            #print len(final_list)
    return len(final_list)
  

def get_element(item, find_list):
    """Returns the item index in a list"""
    if (find_list == 'FLOAT'):
        return [float(item)]
    else:
        return list(one_hot(np.where(np.asarray(find_list)==item)[0][0], len(find_list)))

def read_binary_file(filename, feature_dimension):
    load_mat=io_funcs.load_binary_file(filename, feature_dimension)
    return load_mat

if __name__=="__main__":
    infile=sys.argv[1]
    phonelist=sys.argv[2]
    statelist=sys.argv[3]
    print get_binary_dim(infile, phonelist, statelist)
    #print bin_dim
#    binary_mat = read_binary_file(outfile,711)
#    print binary_mat


