from scipy.io import wavfile
import matplotlib.pyplot as plt 
import numpy as np 

def fsk_demodulator(wav_file, f0=18500, f1=19500, Tb=0.1):
    fs, data = wavfile.read('fsk_message.wav')
    data = data.astype(float)
    print(f"Sampling rate: {fs} Hz, Length: {len(data)} samples")

    N = int(Tb * fs)

    if data.ndim > 1:
        data = data[:,0]

    bitstream = ""

    for i in range (0, len(data), N):
        chunk = data[i:i+N]
        if len(chunk) < N:
            break 
        
        fft_vals = np.fft.fft(chunk)
        freqs = np.fft.fftfreq(len(chunk), d = 1/fs)

        mag = np.abs(fft_vals[:len(chunk)//2])
        freqs = freqs[:len(chunk)//2]
        
        dominant_freq = freqs[np.argmax(mag)]

        if abs(dominant_freq - f0) < abs(dominant_freq - f1):
            bitstream += "0"
        else:
            bitstream += "1"
    
    chars = []
    for i in range(0, len(bitstream), 8):
        byte = bitstream[i:i+8]
        if len(byte) == 8:
            chars.append(chr(int(byte, 2)))
    message = "".join(chars)

    return bitstream, message

if __name__ == "__main__":
    bits, msg = fsk_demodulator("fsk_message.wav" , f0 = 18500, f1 = 19500, Tb = 0.1 )
    print("Recovered bits:", bits)
    print("Recovered message:", msg)






