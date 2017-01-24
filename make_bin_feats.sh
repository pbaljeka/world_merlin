#!/bin/bash
# Note the features are in reverse order when read in, and are reversed and put in the right order when written out.
SOURCE_DIR=festival/rev_coeffs
PHONELIST=festival/clunits/phonenames
STATELIST=festival/clunits/statenames

rm -rf ${SOURCE_DIR}

mkdir -p ${SOURCE_DIR}

for i in festival/coeffs/*.feats;
    do
    echo $i
    f=`basename $i|cut -d '.' -f1`
    tac $i > ${SOURCE_DIR}/${f}.lab
    done

featfile=`cat etc/txt.done.data|awk '{print $2}'|head -1`
feat_dim=`python bin/get_bin_dim.py $SOURCE_DIR/${featfile}.lab $PHONELIST $STATELIST`
echo $feat_dim
TARGET_DIR=ss_dnn/data/binary_label_${feat_dim}
rm -rf ${TARGET_DIR}
    cat etc/txt.done.data|
    awk '{print $2}'|
    while read file
      do
        echo $file
        python bin/binmapper.py $SOURCE_DIR/${file}.lab ${TARGET_DIR} ${PHONELIST} ${STATELIST}
      done
