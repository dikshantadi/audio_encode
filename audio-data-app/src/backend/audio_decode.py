from scipy.io import wavfile
import numpy as np

def goertzel(chunk, target_freq, fs):
    """
    Compute Goertzel magnitude for a single frequency
    """
    N = len(chunk)
    k = int(0.5 + (N * target_freq) / fs)
    omega = (2.0 * np.pi * k) / N
    coeff = 2.0 * np.cos(omega)

    s_prev = 0.0
    s_prev2 = 0.0

    for sample in chunk:
        s = sample + coeff * s_prev - s_prev2
        s_prev2 = s_prev
        s_prev = s

    magnitude = np.sqrt(s_prev2**2 + s_prev**2 - coeff * s_prev * s_prev2)
    return magnitude

def fsk_demodulator(wav_file, f0, f1, Tb):
    fs, data = wavfile.read(wav_file)
    data = data.astype(float)

    print(f"Sampling rate: {fs} Hz, Length: {len(data)} samples")

    if data.ndim > 1:
        data = data[:,0]  # Use first channel if stereo

    N = int(Tb * fs)
    bitstream = ""

    for i in range(0, len(data), N):
        chunk = data[i:i+N]
        if len(chunk) < N:
            break

        mag0 = goertzel(chunk, f0, fs)
        mag1 = goertzel(chunk, f1, fs)

        bit = '0' if mag0 > mag1 else '1'
        bitstream += bit

    # Convert bitstream to ASCII message
    chars = []
    for i in range(0, len(bitstream), 8):
        byte = bitstream[i:i+8]
        if len(byte) == 8:
            chars.append(chr(int(byte, 2)))
    message = "".join(chars)

    return bitstream, message

if __name__ == "__main__":
    bits, msg = fsk_demodulator("fsk_message.wav", f0=8000, f1=9000, Tb=0.1)
    print("Recovered bits:", bits)
    print("Recovered message:", msg)



