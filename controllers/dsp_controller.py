#Challenges of the dsp-controller class:
#1. Need to be able to add function pointers to a list of function points
#2.
from .dsp_lib import DspLib # pylint: disable=E0401

class DspController:
    #dspLib = __import__('..dsp_libraries.DspLib')
    def __init__(self):
        self.dsp_suite = dict()
    def addDspMethod(self, name):
        self.dsp_suite[name] = getattr(DspLib, name)
    def executeDspSuite(self, params):
        for dspMethodName in self.dsp_suite:
            signal = self.dsp_suite[dspMethodName](params)
        return signal
