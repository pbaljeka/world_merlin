import os
import numpy
from io_funcs.binary_io import BinaryIOCollection

def load_covariance(var_file_dict, out_dimension_dict):
    var = {}
    io_funcs = BinaryIOCollection()
    for feature_name in var_file_dict.keys():
        var_values, dimension = io_funcs.load_binary_file_frame(var_file_dict[feature_name], 1)
        var_values = numpy.reshape(var_values, (out_dimension_dict[feature_name], 1))
        var[feature_name] = var_values
    return  var


def load_stats():
    fid = open('/home2/pbaljeka/ss_dnn/data/norm_info_mgc_lf0_vuv_bap_199_MVN.dat', 'rb')
    cmp_min_max = numpy.fromfile(fid, dtype=numpy.float32)
    fid.close()
    cmp_min_max = cmp_min_max.reshape((2, -1))
    cmp_min_vector = cmp_min_max[0, ]
    cmp_max_vector = cmp_min_max[1, ]
   # denormaliser = MeanVarianceNorm(feature_dimension = cmp_dim)
    #denormaliser.feature_denormalisation(gen_file_list, gen_file_list, cmp_min_vector, cmp_max_vector)
    print cmp_min_vector
    return cmp_max_vector
if __name__=="__main__":
    var_file_dict = {}
    out_dimension_dict={'mgc' : 180, 'lf0' : 3, 'vuv' :1, 'bap' : 15}

    for feature_name in out_dimension_dict.keys():
        var_file_dict[feature_name] = os.path.join('/home2/pbaljeka/ss_dnn/data/var', feature_name + '_' + str(out_dimension_dict[feature_name]))

    var_dict = load_covariance(var_file_dict, out_dimension_dict)
    print var_dict
    print load_stats()
