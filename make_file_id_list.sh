#1/bin/bash

VOICE_FOLDER=$1

${VOICE_FOLDER}/bin/traintest $VOICE_FOLDER/etc/txt.done.data
${VOICE_FOLDER}/bin/traintest $VOICE_FOLDER/etc/txt.done.data.train

cat $VOICE_FOLDER/etc/txt.done.data.train.train |awk '{print $2}' >trainlist
cat $VOICE_FOLDER/etc/txt.done.data.train.test |awk '{print $2}' >vallist
cat $VOICE_FOLDER/etc/txt.done.data.test |awk '{print $2}' >testlist


cat trainlist vallist testlist >$VOICE_FOLDER/ss_dnn/data/file_id_list.scp
TRAIN_FILES=`cat trainlist |wc -l`
VAL_FILES=`cat vallist |wc -l`
TEST_FILES=`cat testlist |wc -l`

rm *list
echo  $TRAIN_FILES%$VAL_FILES%$TEST_FILES>etc/trainvaltest

