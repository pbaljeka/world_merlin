#!/bin/bash

if [ ! "$FESTVOXDIR" ]
then
   echo "environment variable FESTVOXDIR is unset"
   echo "set it to your local festvox directory e.g."
   echo '   bash$ export FESTVOXDIR=/home/awb/projects/festvox/'
   exit 1
fi

if [ ! "$SPTKDIR" ]
then
   echo "environment variable SPTKDIR is unset"
   echo "set it to your local SPTK directory e.g."
   echo '   bash$ export SPTKDIR=/home/awb/projects/SPTK'
   exit 1
fi

conf_file=$1

CURRENT_DIR=`pwd`
TRAIN_FILES=`cat etc/trainvaltest|cut -d '%' -f1`
VAL_FILES=`cat etc/trainvaltest|cut -d '%' -f2`
TEST_FILES=`cat etc/trainvaltest|cut -d '%' -f3`

PHONELIST=festival/clunits/phonenames
STATELIST=festival/clunits/statenames

featfile=`cat etc/txt.done.data|awk '{print $2}'|head -1`
LAB_DIM=`python bin/get_bin_dim.py festival/coeffs/${featfile}.feats $PHONELIST $STATELIST`

echo $LAB_DIM
echo $TRAIN_FILES, $VAL_FILES, $TEST_FILES

cat ${conf_file}|
sed 's+$SPTKDIR+'"${SPTKDIR}"'+g'|
sed 's+$FESTVOXDIR+'"${FESTVOXDIR}"'+g'|
sed 's+$LAB_DIM+'"$LAB_DIM"'+g'|
sed 's+$TRAIN_FILES+'"$TRAIN_FILES"'+g'|
sed 's+$VAL_FILES+'"$VAL_FILES"'+g'|
sed 's+$TEST_FILES+'"$TEST_FILES"'+g'|
sed 's+$FESTIVAL_VOICE_DIR+'"${CURRENT_DIR}"'+g'>ss_dnn/feed_forward_dnn_WORLD.conf

THEANO_FLAGS="floatX=float32"
export THEANO_FLAGS
PYTHONPATH=:/usr/lib/python2.7/dist-packages
export PYTHONPATH
