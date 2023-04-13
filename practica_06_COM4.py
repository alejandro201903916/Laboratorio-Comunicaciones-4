import numpy as np
from os.path import dirname, join as pjoin
from scipy.io import wavfile
import scipy.io
import matplotlib.pyplot as plt

data_dir = pjoin(dirname(scipy.io.__file__), 'tests', 'data')
wav_fname = pjoin(data_dir, 'audio.wav')

# Cargar archivo de audio
fs, audio = wavfile.read(wav_fname)

# Convertir a float entre -1 y 1
audio = audio.astype(float)/32768.0

# Aplicar la DCT.
dct = np.fft.rfft(audio)

# Realizar la compresión eliminando los coeficientes de menor magnitud
threshold = 0.1*np.max(np.abs(dct))
dct_compressed = dct*(np.abs(dct)>=threshold)

# Aplicar la IDCT
audio_compressed = np.fft.irfft(dct_compressed)

# Graficar archivo de audio inicial y final
t = np.arange(len(audio))/fs
plt.subplot(2,1,1)
plt.plot(t, audio)
plt.title('Archivo de audio inicial')
plt.xlabel('Tiempo(seg)')
plt.ylabel('Amplitud')

plt.subplot(2,1,2)
plt.plot(t, audio_compressed)
plt.title('Archivo de audio comprimido')
plt.xlabel('Tiempo(seg)')
plt.ylabel('Amplitud')
plt.tight_layout()
plt.show()