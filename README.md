# merlin_festvox
To build a new voice with the merlin toolkit and using the clustegen's question set:
###Simple Steps:
####0. Copy this folder into the FESTVOXDIR/src/world_merlin

####1. Setup environment variables:
```bash
export ESTDIR=/path/to/speech_tools
export FESTVOXDIR=/path/to/festvox
export SPTKDIR=/path/to/SPTK
```
####2. Make a new voice directory and set up the initial directory structure
```bash
mkdir <institute>_<lexicon>_<voicename>
example: mkdir cmu_us_pnb
cd cmu_us_pnb
$FESTVOXDIR/src/world_merlin/setup_world_merlin cmu us pnb
```
####3. Copy the transcript in the festival format:
```bash
cp <TRANSCRIPT_DIR>/txt.done.data etc/txt.done.data
```
It needs to be named txt.done.data and must be of the format:
( wavfile_name "Transcription of wavefile." )
eg:( arctic_a0001 "Author of the danger trail, Philip Steels, etc." )

####4. Copy wav files from your directory and power normalize:
```bash
./bin/get_wavs <WAVDIR>/*.wav
```

####5. Remove extra silences optionally.
Remove trailing and leading silences:
```bash
./bin/prune_silence wav/*.wav
```
Remove middle silences:
```bash
./bin/prune_middle_silence wav/*.wav
```

####6. Run the voice building script.
```bash
./bin/build_merlin_world_voice
```

#####Note the last step in the above script assumes the default location of trained neural network model and its name.  

### Steps in build_merlin_world_voice:-Continue after step 5 above.
####6. Dump aligned WORLD feats with CLUSTERGEN's features:
```bash
./bin/dump_world_feats
```

####7. Make train/test/val splits.
```bash
./bin/make_file_id_list.sh `pwd`  
```
####8. Setup the configuration file
```bash
./bin/setup_conf.sh ss_dnn/feed_forward_dnn_WORLD_template.conf
```
####9. Train DNN
```bash
python ss_dnn/merlin_scripts/src/run_dnn.py ss_dnn/feed_forward_dnn_WORLD.conf
```
####10. Resynthesize wavefiles
```bash
./bin/merlin_resynthesis.sh $model_directory
```
