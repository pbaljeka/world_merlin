#!/bin/bash
# Note the features are in reverse order when read in, and are reversed and put in the right order when written out.
SPTK_BINDIR=$SPTKDIR/bin
SOURCE_DIR=festival/rev_world_coeffs
TARGET_DIR=ss_dnn/data
MGC_DIR=${TARGET_DIR}/mgc
BAP_DIR=${TARGET_DIR}/bap
LF0_DIR=${TARGET_DIR}/lf0
rm -rf ${SOURCE_DIR} 
rm -rf tmp*
mkdir -p ${SOURCE_DIR}
mkdir -p ${MGC_DIR}
mkdir -p ${BAP_DIR}
mkdir -p ${LF0_DIR}
for i in festival/coeffs/*.mcep;
    do
    echo $i
    f=`basename $i`
    tac $i > ${SOURCE_DIR}/$f
    done

 cat etc/txt.done.data|
    awk '{print $2}'|
    while read file
      do
        echo $file
    #Parse world features f0, mgc (60) , bap(5), vuv(not needed
        cat $SOURCE_DIR/${file}.mcep |awk '{print $2}' >tmp.f0
        cat $SOURCE_DIR/${file}.mcep |cut -d ' ' -f3-62 >tmp.mgc
        cat $SOURCE_DIR/${file}.mcep |cut -d ' ' -f63-67 >tmp.bap

    #Convert F0 to lf0
        $SPTK_BINDIR/x2x +af tmp.f0 >tmp.f0a
        $SPTK_BINDIR/sopr -magic 0.0 -LN -MAGIC -1.0E+10 tmp.f0a >${LF0_DIR}/${file}.lf0

    #Save the others as binary
        $SPTK_BINDIR/x2x +af tmp.mgc > ${MGC_DIR}/${file}.mgc
        $SPTK_BINDIR/x2x +af tmp.bap > ${BAP_DIR}/${file}.bap
     rm tmp*
     done


   mkdir ss_dnn/data/ref_data2
   cp ss_dnn/data/mgc/* ss_dnn/data/ref_data2
   cp ss_dnn/data/bap/* ss_dnn/data/ref_data2
   cp ss_dnn/data/lf0/* ss_dnn/data/ref_data2
