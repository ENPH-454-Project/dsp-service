#Challenges of the dsp-controller class:
#1. Need to be able to add function pointers to a list of function points
#2.
from .dsp_lib import DspLib # pylint: disable=E0401

class DspController:
    #dspLib = __import__('..dsp_libraries.DspLib')
    def __init__(self):
        self.dsp_lib = DspLib()
        self.dsp_suite = dict()
    def addDspMethod(self, name):
        self.dsp_suite[name] = getattr(self.dsp_lib, name)
    def executeDspSuite(self, params):
        for dspMethodName in self.dsp_suite:
            params['signal'] = self.dsp_suite[dspMethodName](params)
        return params
