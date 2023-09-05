import numpy as np
from scipy.io import wavfile

# Define the parameters
sample_rate = 44100  # Samples per second (Hz) need to be in 10k and above? 
duration = 0.3 # Duration of the sound in seconds
frequency = 220.0  # Frequency of the sine wave in Hz (A4 note)

# Generate the time points
t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)

# Generate the sine wave
waveform = np.sin(3 * np.pi * frequency * t)

# Scale the waveform to 16-bit signed integer values
scaled_waveform = np.int16(waveform * 32767)

# Save the audio data to a WAV file
wavfile.write('output.wav', sample_rate, scaled_waveform)
