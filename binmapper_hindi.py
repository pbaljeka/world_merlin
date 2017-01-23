import numpy as np
import sys
import os
import binary_io
io_funcs = binary_io.BinaryIOCollection()
#need to make this better.. read in a file with phonelist etc. This is only for testing.
STATELIST=["0", '9r_1', '9r_2', '9r_3', '9r=_1', '9r=_2', '9r=_3', 'A_1', 'A_2', 'A_3', 'A:_1', 'A:_2', 'A:_3', 'A:nas_1', 'A:nas_2', 'A:nas_3', 'E_1', 'E_2', 'E_3', 'G_1', 'G_2', 'G_3', 'J_1', 'J_2', 'J_3', 'Jh_1', 'Jh_2', 'Jh_3', 'N_1', 'N_2', 'N_3', 'aI_1', 'aI_2', 'aI_3', 'aInas_1', 'aInas_2', 'aInas_3', 'aU_1', 'aU_2', 'aU_3', 'ay_1', 'ay_2', 'ay_3', 'aynas_1', 'aynas_2', 'aynas_3', 'b_1', 'b_2', 'b_3', 'bh_1', 'bh_2', 'bh_3', 'c_1', 'c_2', 'c_3', 'ch_1', 'ch_2', 'ch_3', 'c}_1', 'c}_2', 'c}_3', 'dB_1', 'dB_2', 'dB_3', 'dBh_1', 'dBh_2', 'dBh_3', 'dR_1', 'dR_2', 'dR_3', 'dr_1', 'dr_2', 'dr_3', 'e_1', 'e_2', 'e_3', 'enas_1', 'enas_2', 'enas_3', 'f_1', 'f_2', 'f_3', 'g_1', 'g_2', 'g_3', 'gh_1', 'gh_2', 'gh_3', 'h_1', 'h_2', 'h_3', 'hv_1', 'hv_2', 'hv_3', 'i_1', 'i_2', 'i_3', 'i:_1', 'i:_2', 'i:_3', 'i:nas_1', 'i:nas_2', 'i:nas_3', 'j_1', 'j_2', 'j_3', 'k_1', 'k_2', 'k_3', 'kh_1', 'kh_2', 'kh_3', 'l_1', 'l_2', 'l_3', 'm_1', 'm_2', 'm_3', 'nB_1', 'nB_2', 'nB_3', 'nX_1', 'nX_2', 'nX_3', 'nr_1', 'nr_2', 'nr_3', 'n~_1', 'n~_2', 'n~_3', 'o_1', 'o_2', 'o_3', 'onas_1', 'onas_2', 'onas_3', 'ow_1', 'ow_2', 'ow_3', 'ownas_1', 'ownas_2', 'ownas_3', 'p_1', 'p_2', 'p_3', 'pau_1', 'pau_2', 'pau_3', 'ph_1', 'ph_2', 'ph_3', 'q_1', 'q_2', 'q_3', 'rr_1', 'rr_2', 'rr_3', 'rrh_1', 'rrh_2', 'rrh_3', 's_1', 's_2', 's_3', 'sr_1', 'sr_2', 'sr_3', 'pau_5', 'tB_1', 'tB_2', 'tB_3', 'tBh_1', 'tBh_2', 'tBh_3', 'tR_1', 'tR_2', 'tR_3', 'tr_1', 'tr_2', 'tr_3', 'u_1', 'u_2', 'u_3', 'u:_1', 'u:_2', 'u:_3', 'u:nas_1', 'u:nas_2', 'u:nas_3', 'unas_1', 'unas_2', 'unas_3', 'v_1', 'v_2', 'v_3', 'x_1', 'x_2', 'x_3', 'z_1', 'z_2', 'z_3']


PHONELIST=["0", '9r', '9r=', 'A', 'A:', 'A:nas', 'E', 'G', 'J', 'Jh', 'N', 'aI', 'aInas', 'aU', 'ay', 'aynas', 'b', 'bh', 'c', 'ch', 'c}', 'dB', 'dBh', 'dR', 'dr', 'e', 'enas', 'f', 'g', 'gh', 'h', 'hv', 'i', 'i:', 'i:nas', 'j', 'k', 'kh', 'l', 'm', 'nB', 'nX', 'nr', 'n~', 'o', 'onas', 'ow', 'ownas', 'p', 'pau', 'ph', 'q', 'rr', 'rrh', 's', 'sr', 'ssil', 'tB', 'tBh', 'tR', 'tr', 'u', 'u:', 'u:nas', 'unas', 'v', 'x', 'z']
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
            #print ' '.join([ str(element) for element in final_list ])     
            final_mat.append(final_list)
            final_list=[]
        io_funcs.array_to_binary_file(final_mat, outfile)
    
   

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


