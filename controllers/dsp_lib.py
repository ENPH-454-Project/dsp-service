import numpy as np
from os import listdir, path
from os.path import isfile, join
coef_path = path.normpath("C:/Users/Paul/PycharmProjects/dsp-service/filter_coefficients/")
class DspLib:
     #Removes all frequencies below 5 times the mean_value of the signal
     #frequencies. To remove noise? Somewhat useless method but oh well :)
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

    def transfer_cheating(self, params):
        clean_signal = params['clean_signal']
        distorted_signal = params['signal']
        merp = clean_signal[:,0]
        inverseTransferFunction = np.divide(clean_signal[:,0], distorted_signal)
        sol = np.multiply(distorted_signal, inverseTransferFunction)
        return np.multiply(distorted_signal, inverseTransferFunction)

    def impulse_response(self, params):
        impulse = params['impulse']
        signal = params['signal']
        paddedImpulse = np.zeros(signal.shape)
        paddedImpulse[:len(impulse)] = impulse
        fft_signal = np.fft.fft(signal)
        fft_impulse = np.fft.fft(paddedImpulse)
        return np.fft.ifft(np.divide(np.fft.fft(signal),np.fft.fft(paddedImpulse))).real

    def remove_noise(self, params):
        fft_values = np.fft.fft(params['signal'])
        mean_value = np.mean(abs(fft_values))
        threshold = mean_value*2
        print(threshold)
        for i in range(len(fft_values)):
            if abs(fft_values[i]) < threshold:
                fft_values[i] = 0

        return np.fft.ifft(fft_values).real

    def remove_interference_peak(selfs, params):
        fft_values = np.fft.fft(params['signal'])
        lower_freq = 300000
        higher_freq = 400000
        for i in range(len(fft_values)):
            if (abs(fft_values[i]) < higher_freq) and (abs(fft_values[i]) > lower_freq):
                fft_values[i] = 0
        return np.fft.ifft(fft_values).real

    def keep_frequency_band(selfs, params):
        fft_values = np.fft.fft(params['signal'])
        lower_freq = 0
        higher_freq = 100000
        for i in range(len(fft_values)):
            if (abs(fft_values[i]) > higher_freq) or (abs(fft_values[i]) < lower_freq):
                fft_values[i] = 0
        return np.fft.ifft(fft_values).real

     # function used in various internal functions to reduce redundant code
    def _get_norm_cutoff_and_nyq_freq(self, cutoff, sample_rate):
        nyq = 0.5 * cutoff
        normal_cutoff = sample_rate / nyq
        return normal_cutoff


