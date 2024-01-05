import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav

fs = 44100  # Sample rate
duration = 5  # seconds
print("ok")
myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=2)
sd.wait()  # Wait until recording is finished
wav.write('output.wav', fs, myrecording)  # Save as WAV file
#koto