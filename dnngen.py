import os
import numpy
from merlin_gen_scripts.mean_variance_norm import MeanVarianceNorm
from merlin_gen_scripts.parameter_generation import ParameterGeneration

def prepare_file_path_list(file_id_list, file_dir, file_extension='.cmp', new_dir_switch=True):
    if not os.path.exists(file_dir) and new_dir_switch:
        os.makedirs(file_dir)
    file_name_list = []
    with open(file_id_list, 'r') as fileid_list:
        for file_id in fileid_list:
            file_name = file_dir + '/' + file_id.strip() + file_extension
            file_name_list.append(file_name)
    return  file_name_list

def do_denormalization(norm_info_file, feature_dimension, filelist, in_dir='test', out_dir='gen'):
    fid = open(norm_info_file, 'rb')
    cmp_min_max = numpy.fromfile(fid, dtype=numpy.float32)
    fid.close()
    cmp_min_max = cmp_min_max.reshape((2, -1))
    cmp_min_vector = cmp_min_max[0, ]
    cmp_max_vector = cmp_min_max[1, ]
    
    norm_in_file_list = prepare_file_path_list(filelist, in_dir) 
    norm_out_file_list= prepare_file_path_list(filelist, out_dir)

    denormaliser = MeanVarianceNorm(feature_dimension = feature_dimension)
    denormaliser.feature_denormalisation(norm_in_file_list, norm_out_file_list, cmp_min_vector, cmp_max_vector)
    
def do_decomposition(var_dict, out_dimension_dict, filelist, feature_dimension, in_dir='gen'):
    gen_in_file_list = prepare_file_path_list(filelist, in_dir) 
    generator = ParameterGeneration(gen_wav_features = ['mgc', 'lf0', 'vuv', 'bap'])
    generator.acoustic_decomposition(gen_in_file_list, feature_dimension, out_dimension_dict, file_extension_dict, var_file_dict)

if __name__=="__main__":
    norm_info_file="/home2/pbaljeka/new_exps2/ss_dnn_festivalSLT/data/norm_info_mgc_lf0_vuv_bap_199_MVN.dat"
    file_id_list = "/home2/pbaljeka/new_exp4/data_festival/test_file"
    in_dir="/home2/pbaljeka/new_exp4/data_festival/predicted_features/true_test_feats"
    out_dir="/home2/pbaljeka/new_exp4/data_festival/gen_features/true_test_feats/"
    acoustic_feature_dimension = int(199)
    out_dimension_dict = { 'mgc' : 180,
                           'lf0' : 3,
                           'vuv' : 1,
                           'bap' : 15}
        
    file_extension_dict = {'mgc' : '.mgc',
                           'lf0' : '.lf0',
                           'vuv' : '.vuv',
                           'bap' : '.bap'}

    var_file_dict  = { 'mgc' : '/home2/pbaljeka/new_exps2/ss_dnn_festivalSLT/data/var/mgc_180',
                       'lf0' : '/home2/pbaljeka/new_exps2/ss_dnn_festivalSLT/data/var/lf0_3',
                       'bap' : '/home2/pbaljeka/new_exps2/ss_dnn_festivalSLT/data/var/bap_15',
                       'vuv' : '/home2/pbaljeka/new_exps2/ss_dnn_festivalSLT/data/var/vuv_1'}
    do_denormalization(norm_info_file=norm_info_file, feature_dimension=acoustic_feature_dimension, filelist=file_id_list, in_dir=in_dir, out_dir=out_dir)
    do_decomposition(var_dict=var_file_dict, out_dimension_dict=out_dimension_dict, filelist=file_id_list, feature_dimension=acoustic_feature_dimension, in_dir=out_dir)
    #generator = ParameterGeneration()

    #generator.acoustic_decomposition(in_file_list, 199, out_dimension_dict, file_extension_dict, var_file_dict)

