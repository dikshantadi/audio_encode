#This file is Encoding Data into Audio File and Using Frequency Shift Keying Modulation Technique

import scipy
from scipy.io.wavfile import write
import matplotlib.pyplot as plt 
import wave
import numpy as np 
from math import pi
from enkode import take_message

#defining
fs = 44100 # Sampling frequency
Tb = 0.1    # bit duration in seconds
f0 = 18500   # Frequency for bit 0 in Hz
f1 = 19500   # Frequency for bit 1 in Hz 

signal = np.array([])
bitstream = take_message()

for bit in bitstream :
    f = f1 if bit == '1' else f0
    t = np.linspace(0, Tb, int(fs*Tb), endpoint=False)
    sine_wave = np.sin(2 * pi * f * t)
    signal = np.concatenate((signal, sine_wave))

signal_int16 = np.int16(signal * 32767)

write("fsk_message.wav", fs, signal_int16)
print("WAV file saved")


plt.plot(signal[:1000])
plt.title("FSK waveform (first few samples)")
plt.xlabel("Sample")
plt.ylabel("Amplitude")
plt.savefig("fsk_waveform.png")




