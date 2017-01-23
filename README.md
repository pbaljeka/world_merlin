# merlin_festvox
To build a new voice with the merlin toolkit and using the clustegen's question set:
###Steps:
####1. Setup environment variables:
```bash
export ESTDIR=/path/to/speech_tools
export FESTVOXDIR=/path/to/festvox
export SPTKDIR=/path/to/SPTK
export WORLD=/path/to/WORLD_vocoder
```
####2. Make a new voice directory and set up the initial directory structure
```bash
mkdir <institute>_<lexicon>_<voicename>
example: mkdir cmu_us_pnb
cd cmu_us_pnb
$FESTVOXDIR/src/merlin_festvox/setup_merlin_world_voice cmu us pnb
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

6. Dump aligned WORLD feats with CLUSTERGEN's features:
```bash
./bin/dump_aligned_world_feats
```

7. Convert festival's dumped features to binary format required by Merlin.
```bash
```

8. Train the model
9. Resynthesize
10. Caluclate MCD
