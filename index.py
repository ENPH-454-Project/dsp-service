from controllers.dsp_controller import DspController


import numpy


def handler(event, context):

    dspSuite = event['dsp_suite']
    params = event['params']
    print('received suite: ')
    print(dspSuite)

    dspController = DspController()

    for dspMethod in dspSuite:
        print(dspMethod)
        dspController.addDspMethod(dspMethod)

    result = dspController.executeDspSuite(params)
    newWav = numpy.array(result, dtype=numpy.int16)

    return newWav
