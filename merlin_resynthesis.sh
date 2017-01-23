
# top merlin directory

# tools directory
#world="/home/pbaljeka/Merlin/merlin/tools/bin/WORLD"
world=$FESTVOXDIR/src/wrold_merlin/WORLD
sptk=$SPTKDIR/bin
# input audio directory
#out_dir=`pwd`/gen/DNN__mgc_lf0_vuv_bap_1_917_711_199_6_1024
MODEL_DIR=$1
out_dir=I`pwd`/ss_dnn/gen/$MODEL_DIR
# Output features directory
#out_dir=`pwd`/syn_world

resyn_dir="${out_dir}/resyn_dir"

mkdir -p ${resyn_dir}
# initializations
fs=16000

if [ "$fs" -eq 16000 ]
then
nFFTHalf=1024 
alpha=0.58
fi

if [ "$fs" -eq 48000 ]
then
nFFTHalf=2048
alpha=0.77
fi

mcsize=59
order=4

for file in $out_dir/*.cmp #.wav
do
    filename="${file##*/}"
    file_id="${filename%.*}"
   
    echo $file_id
   
    ### WORLD ANALYSIS -- extract vocoder parameters ###

    ## extract f0, sp, ap ### 
   ### convert lf0 to f0 ###
    $sptk/sopr -magic -1.0E+10 -EXP -MAGIC 0.0 ${out_dir}/$file_id.lf0 | $sptk/x2x +fa > ${resyn_dir}/$file_id.resyn.f0a
    $sptk/x2x +ad ${resyn_dir}/$file_id.resyn.f0a > ${resyn_dir}/$file_id.resyn.f0

    ### convert mgc to sp ###
    $sptk/mgc2sp -a $alpha -g 0 -m $mcsize -l $nFFTHalf -o 2 ${out_dir}/$file_id.mgc | $sptk/sopr -d 32768.0 -P | $sptk/x2x +fd > ${resyn_dir}/$file_id.resyn.sp
    
    ### convert bap to ap ###
    $sptk/mgc2sp -a $alpha -g 0 -m $order -l $nFFTHalf -o 2 ${out_dir}/$file_id.bap | $sptk/sopr -d 32768.0 -P | $sptk/x2x +fd > ${resyn_dir}/$file_id.resyn.ap
   

    $world/synth $nFFTHalf $fs ${resyn_dir}/$file_id.resyn.f0 ${resyn_dir}/$file_id.resyn.sp ${resyn_dir}/$file_id.resyn.ap ${out_dir}/$file_id.resyn.wav
done

