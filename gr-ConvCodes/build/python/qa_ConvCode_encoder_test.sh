#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/aruulmozhivarman/Downloads/Convolution-Encoder-SDR-GNU-Radio/gr-ConvCodes/python
export GR_CONF_CONTROLPORT_ON=False
export PATH=/home/aruulmozhivarman/Downloads/Convolution-Encoder-SDR-GNU-Radio/gr-ConvCodes/build/python:$PATH
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH
export PYTHONPATH=/home/aruulmozhivarman/Downloads/Convolution-Encoder-SDR-GNU-Radio/gr-ConvCodes/build/swig:$PYTHONPATH
/usr/bin/python2 /home/aruulmozhivarman/Downloads/Convolution-Encoder-SDR-GNU-Radio/gr-ConvCodes/python/qa_ConvCode_encoder.py 
