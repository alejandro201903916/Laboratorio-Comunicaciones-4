import numpy as np
import scipy.signal as signal
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt

# Leer archivo de audio WAV
fs, x= wav.read('audio.wav')

# Converitr a señal monoaural
x = np.mean(x, axis=1)

# Calcular Transformada Z
z = signal.TransferFunction(x,[1.0,0.0], dt=1/fs)

# Obtener coeficientes de la Transformada Z
b, a = z.num, z.den

# Aplicar Transformada Z al archivo de audio
y = signal.lfilter(b, a, x)

# Graficar señal original y señal con Transformada Z aplicada
t = np.arange(len(x))/float(fs)
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