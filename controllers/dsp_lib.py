import numpy as np
from os import listdir, path
from os.path import isfile, join
coef_path = path.normpath("./filter_coefficients/")
class DspLib:
    def __init__(self):
        pass

    def convolve_filter_coefficients(self, params):
        files = [f for f in listdir(coef_path) if isfile(join(coef_path, f))]
        signal = params['signal']
        for file in files:
            my_path = path.normpath(coef_path + '/' + file)
            coefficients = np.array(open(my_path).read().splitlines()).astype(float)
            signal = np.convolve(signal,coefficients, "same")
        return signal



