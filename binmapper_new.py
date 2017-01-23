import numpy as np
import sys
import os
import binary_io
io_funcs = binary_io.BinaryIOCollection()
#need to make this better.. read in a file with phonelist etc. This is only for testing.
STATELIST=["0",'aa_1', 'aa_2', 'aa_3', 'ae_1', 'ae_2', 'ae_3', 'ah_1', 'ah_2', 'ah_3', 'ao_1', 'ao_2', 'ao_3', 'aw_1', 'aw_2', 'aw_3', 'ax_1', 'ax_2', 'ax_3', 'ay_1', 'ay_2', 'ay_3', 'b_1', 'b_2', 'b_3', 'ch_1', 'ch_2', 'ch_3', 'd_1', 'd_2', 'd_3', 'dh_1', 'dh_2', 'dh_3', 'eh_1', 'eh_2', 'eh_3', 'er_1', 'er_2', 'er_3', 'ey_1', 'ey_2', 'ey_3', 'f_1', 'f_2', 'f_3', 'g_1', 'g_2', 'g_3', 'hh_1', 'hh_2', 'hh_3', 'ih_1', 'ih_2', 'ih_3', 'iy_1', 'iy_2', 'iy_3', 'jh_1', 'jh_2', 'jh_3', 'k_1', 'k_2','k_3', 'l_1', 'l_2', 'l_3', 'm_1', 'm_2', 'm_3', 'n_1', 'n_2', 'n_3', 'ng_1', 'ng_2', 'ng_3', 'ow_1', 'ow_2', 'ow_3', 'oy_1', 'oy_2', 'oy_3', 'p_1', 'p_2', 'p_3', 'pau_1', 'pau_2', 'pau_3', 'r_1', 'r_2', 'r_3', 's_1', 's_2', 's_3', 'sh_1', 'sh_2', 'sh_3', 'pau_5', 't_1', 't_2', 't_3', 'th_1', 'th_2', 'th_3', 'uh_1', 'uh_2', 'uh_3', 'uw_1', 'uw_2', 'uw_3', 'v_1', 'v_2', 'v_3', 'w_1', 'w_2', 'w_3', 'y_1', 'y_2', 'y_3', 'z_1', 'z_2', 'z_3', 'zh_1', 'zh_2', 'zh_3']
PHONELIST=["0",'aa', 'ae', 'ah', 'ao', 'aw', 'ax', 'ay', 'b', 'ch', 'd', 'dh', 'eh', 'er', 'ey', 'f', 'g', 'hh', 'ih', 'iy', 'jh', 'k', 'l', 'm', 'n', 'ng', 'ow', 'oy', 'p', 'pau', 'r', 's', 'sh', 'ssil', 't', 'th', 'uh', 'uw', 'v', 'w', 'y', 'z', 'zh']
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

def one_hot(number, max_size):
    """ Returns the one hot vector of a number, given the max"""
    b = np.zeros(max_size,dtype=float)
    b[number]=1.0
    return b

def make_binary(outdir, infile):
    """Makes binary vectors"""
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
    final_mat=[]
    filename=infile.strip().split('/')[-1]
    if not os.path.exists(outdir):
        os.makedirs(outdir)
    outfile= outdir + '/' + filename
    with open(infile, 'r') as f:
        for line in f:
            feat_list=line.strip().split()
            for feat, list_name in enumerate(features):
                #print "DEBUG: ", feat+2, list_name, feat_list[feat+2]
                final_list.extend(get_element(feat_list[feat + 2], list_name))
            final_mat.append(final_list)
            final_list=[]
        io_funcs.array_to_binary_file(final_mat, outfile)
    
    #print '\n'.join([ str(element) for element in final_list ])

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
    outdir=sys.argv[2]
    make_binary(outdir,infile)
    outfile=outdir +'/' + infile.strip().split('/')[-1]
#    binary_mat = read_binary_file(outfile,711)
#    print binary_mat


