#!/bin/bash

config_file=$1
linguistic_feature_dimension=`cat ${config_file}|grep "lab_binary_dim"|cut -d ":" -f2|sed 's+^ ++g'` 
acoustic_feature_dimension=
train_files=
output_features="mgc_lf0_vuv_bap"
model="DNN_"
