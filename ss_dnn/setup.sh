SSROOTDIR=/Volumes/Network/courses/ss/
FROOTDIR=/Volumes/Network/courses/ss/festival/festival_mac

ESTDIR=$FROOTDIR/speech_tools
MBDIR=$FROOTDIR/multisyn_build
LDLIBS=$ESTDIR/lib

FESTIVALDIR=$FROOTDIR/festival
FESTVOXDIR=$FROOTDIR/festvox

FESTIVAL=$FESTIVALDIR/bin/festival
PATH=$MBDIR/bin:$FESTVOXDIR/src/general:$SSROOTDIR:$ESTDIR/bin:$FESTIVALDIR/bin:$PATH

export ESTDIR FESTIVAL FESTVOXDIR LD_LIBRARY_PATH PATH FROOTDIR SSROOTDIR MBDIR


THEANO_FLAGS="floatX=float32"
export THEANO_FLAGS

PYTHONPATH=:/Volumes/Network/courses/ss/dnn/lib/python2.7/site-packages/
export PYTHONPATH
