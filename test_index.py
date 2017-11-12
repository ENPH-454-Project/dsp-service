from controllers.dsp_controller import DspController # pylint: disable=E0401
import wave
from scipy.io.wavfile import read, write
#using this wavefile reader for now
import numpy
import pyaudio

def handler(event, context):
    #1. receive wave packet and dsp suite
	#2. create dsp suite [figure out how]
	#3. apply dsp suite to wave packet
	#4. save wave packet to dynamoDB table

    dsp_suite = event['dsp_suite']
    params = event['params']
    print(params['signal'])

    dsp_controller = DspController()

    for dsp_method in dsp_suite:
        print(dsp_method)
        dsp_controller.addDspMethod(dsp_method)

    result = dsp_controller.executeDspSuite(params)
    new_wav = numpy.array(result, dtype=numpy.int16)
    print(new_wav)
    print(params['sample_rate'])
    write('you-really-need-to-grow-up.wav', params['sample_rate'], new_wav)
    return result

def wav_player(filepath):
    chunk = 1024
    #open a wav format music
    signal = wave.open(filepath)
    print(signal)
    #instantiate PyAudio
    _pyaudio = pyaudio.PyAudio()
    #open stream
    stream = _pyaudio.open(format=_pyaudio.get_format_from_width(signal.getsampwidth()),
                           channels=signal.getnchannels(),
                           rate=signal.getframerate(),
                           output=True)
    #read data
    data = signal.readframes(chunk)

    #play stream
    while data:
        stream.write(data)
        data = signal.readframes(chunk)

    #stop stream
    stream.stop_stream()
    stream.close()

    #close PyAudio
    _pyaudio.terminate()


wav_player('you-need-to-grow-up.wav')
AUDIO = read("you-need-to-grow-up.wav")

AUDIO_ARRAY = numpy.array(AUDIO[1], dtype=numpy.int16)
SAMPLE_RATE = AUDIO[0]
CUTOFF = 1000 # Hz
ORDER = 5
handler({
    'dsp_suite': ['butter_lowpass'],
    'params': {'sample_rate': SAMPLE_RATE, 'cutoff': CUTOFF, 'signal': AUDIO_ARRAY,
               'order': ORDER}
}, None)

wav_player('you-really-need-to-grow-up.wav')
