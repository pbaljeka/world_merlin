import numpy as np
import sys
import os
import binary_io
io_funcs = binary_io.BinaryIOCollection()
        
        
def write_binary_file(final_mat, outfile):
    io_funcs.array_to_binary_file(final_mat, outfile)
    
    #print '\n'.join([ str(element) for element in final_list ])

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


