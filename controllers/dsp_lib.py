from scipy.fftpack import fft, ifft
from scipy.signal import butter, lfilter, freqz
import numpy

class DspLib:
     #Removes all frequencies below 5 times the mean_value of the signal
     #frequencies. To remove noise? Somewhat useless method but oh well :)
    def removeNoise(self, params):
        fft_values = fft(params['signal'])
        mean_value = numpy.mean(abs(fft_values))
        threshold = mean_value*5
        print(threshold)
        for i in range(len(fft_values)):
            if abs(fft_values[i][0]) < threshold:
                fft_values[i] = [0, 0]
        return ifft(fft_values).real

    # function used in various internal functions to reduce redundant code
    def _get_norm_cutoff_and_nyq_freq(self, cutoff, sample_rate):
        nyq = 0.5 * cutoff
        normal_cutoff = sample_rate / nyq
        return normal_cutoff

    # Gets butterworth lower filter coefficients and then applies the filter to
    # the signal and returns the processed signal
    def butter_lowpass_filter(self, params):
        normal_cutoff = self._get_norm_cutoff_and_nyq_freq(params['cutoff'], params['sample_rate'])
        b, a = butter(params['order'], normal_cutoff, btype='lowpass', analog=False)
        return lfilter(b, a, params['signal'])

    def butter_highpass_filter(self, params):
        normal_cutoff = self._get_norm_cutoff_and_nyq_freq(params['cutoff'], params['sample_rate'])
        b, a = butter(params['order'], normal_cutoff, btype='highpass', analog=True)
        return lfilter(b, a, params['signal'])

    def butter_bandpass_filter(self, params):
        nyq = 0.5 * params['sample_rate']
        normal_low_cutoff = params['low_cutoff'] / nyq
        normal_high_cutoff = params['high_cutoff'] / nyq
        b, a = butter(params['order'], [normal_low_cutoff, normal_high_cutoff], btype='bandpass', analog=True)
        return lfilter(b, a, params['signal'])
