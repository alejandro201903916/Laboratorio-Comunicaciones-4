import numpy as np
import scipy.signal as signal
from scipy.io import wavfile
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt
from os.path import dirname, join as pjoin
import matplotlib.pyplot as plt
import scipy.io
import os

i = 0

while i < 1:
    print("1. Calcular transformada de Z")
    print("2. Aplicar la DCT")
    print("3. Reproducir Audio Original")
    print("4. Salir")
    opcion = int(input("Elija una opción: "))

    if opcion == 1: #Aplicar transformada Z
        # Leer archivo de audio WAV
        fs, x = wav.read('audio.wav')

        # Converitr a señal monoaural
        x = np.mean(x, axis=1)

        # Calcular Transformada Z
        z = signal.TransferFunction(x, [1.0, 0.0], dt=1 / fs)

        # Obtener coeficientes de la Transformada Z
        b, a = z.num, z.den

        # Aplicar Transformada Z al archivo de audio
        y = signal.lfilter(b, a, x)

        # Graficar señal original y señal con Transformada Z aplicada
        t = np.arange(len(x)) / float(fs)
        plt.subplot(2, 1, 1)
        plt.plot(t, x)
        plt.xlabel('Tiempo(s)')
        plt.ylabel('Amplitud')
        plt.title('Señal Original')

        plt.subplot(2, 1, 2)
        plt.plot(t, y)
        plt.xlabel('Tiempo(s)')
        plt.ylabel('Amplitud')
        plt.title('Señal con Transformada Z aplicada')

        plt.show()

        # Escribir archivo de audio WAV con Transformada Z aplicada
        wav.write('archivo_audio_con_Z.wav', fs, y.astype(np.int16))

    elif opcion == 2: #Aplicar DCT
        #data_dir = pjoin(dirname(scipy.io.__file__), 'tests', 'data')
        #wav_fname = pjoin(data_dir, 'audio.wav')

        # Cargar archivo de audio
        fs, audio = wavfile.read('audio.wav')

        # Convertir a float entre -1 y 1
        audio = audio.astype(float) / 32768.0

        # Aplicar la DCT.
        dct = np.fft.rfft(audio)

        # Realizar la compresión eliminando los coeficientes de menor magnitud
        threshold = 0.1 * np.max(np.abs(dct))
        dct_compressed = dct * (np.abs(dct) >= threshold)

        # Aplicar la IDCT
        audio_compressed = np.fft.irfft(dct_compressed)

        # Graficar archivo de audio inicial y final
        t = np.arange(len(audio)) / fs
        plt.subplot(2, 1, 1)
        plt.plot(t, audio)
        plt.title('Archivo de audio inicial')
        plt.xlabel('Tiempo(seg)')
        plt.ylabel('Amplitud')

        plt.subplot(2, 1, 2)
        plt.plot(t, audio_compressed)
        plt.title('Archivo de audio comprimido')
        plt.xlabel('Tiempo(seg)')
        plt.ylabel('Amplitud')
        plt.tight_layout()
        plt.show()

    elif opcion == 3: #Reproducir audio original
        file = "audio.wav"
        os.system("afplay " + file)

    elif opcion == 4: #finalizar el proceso
        break
"""
#########################################################
# Cargar archivo de audio
fs, audio = wavfile.read('audio.wav')

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
"""