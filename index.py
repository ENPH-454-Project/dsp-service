from controllers.dsp_controller import DspController
#using this wavefile reader for now
import numpy


def handler(event, context):
    #1. receive wave packet and dsp suite
	#2. create dsp suite [figure out how]
	#3. apply dsp suite to wave packet
	#4. save wave packet to dynamoDB table

    dsp_suite = event['dsp_suite']
    signal = event['signal']
    params = event['params']
    print('received suite: ')
    print(dsp_suite)

    print('received params: ')
    print(params)

    dsp_controller = DspController()

    for dsp_method in dsp_suite:
        print(dsp_method)
        dsp_controller.addDspMethod(dsp_method)

    result = dsp_controller.executeDspSuite(signal)

    new_signal = numpy.array(result, dtype=numpy.int16)

    return new_signal
