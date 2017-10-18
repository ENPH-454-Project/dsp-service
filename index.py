from controllers.dsp_controller import DspController
def handler(event, context):
    #1. receive wave packet and dsp suite
	#2. create dsp suite [figure out how]
	#3. apply dsp suite to wave packet
	#4. save wave packet to dynamoDB table
    dspSuite = event['dsp_suite']
    dspController = DspController()

    for dspMethod in dspSuite:
        print(dspMethod)
        print(dspController.addDspMethod)
        dspController.addDspMethod(dspMethod)

    result = dspController.executeDspSuite(0)
    print(result)
    return result

handler({
    'dsp_suite': ['testMethod', 'secondTestMethod']
},None)
