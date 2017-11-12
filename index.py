from controllers.dsp_controller import DspController
from scipy.io.wavfile import read, write
#using this wavefile reader for now
import wave
import numpy
import pyaudio

def handler(event, context):
    #1. receive wave packet and dsp suite
	#2. create dsp suite [figure out how]
	#3. apply dsp suite to wave packet
	#4. save wave packet to dynamoDB table

    dspSuite = event['dsp_suite']
    signal = event['signal']
    print('received suite: ')
    print(dspSuite)

    dspController = DspController()

    for dspMethod in dspSuite:
        print(dspMethod)
        dspController.addDspMethod(dspMethod)

    result = dspController.executeDspSuite(signal)
    newWav = numpy.array(result, dtype=numpy.int16)

    return newWav
