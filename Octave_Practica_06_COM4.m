% Comprueba si estamos ejecutando en MatLab o en Octave
if (exist('OCTAVE_VERSION', 'builtin') ~= 0)
  % Estamos en Octave
  pkg load signal;
end 
% Menú principal
opcion = 0;
while opcion ~= 5
  %opcion = input('Seleccione una opción:\n 1. Grbar audio\n 2. Reproducir audio\n ');
  %Menú de opciones
  
  disp('Seleccione una opción:')
  disp('1. Grabar')
  disp('2. Reproducir') 
  disp('3. Graficar')
  disp('4. Graficar densidad')
  disp('5. Transformada Z')
  disp('6. Realizar DCT')
  disp('7. Salir')
  opcion = input('Ingrese su elección: ');
  
  switch opcion
    case 1
      %Grabación de audio
      try
        duracion = input('Ingrese la duración de la grabación en segundos: ');
        disp('Comenzando la grabación...');
        recObj = audiorecorder;
        recordblocking(recObj,duracion);
        disp('Grabacion Finalizada');
        data = getaudiodata(recObj);
        audiowrite('grabacion.wav', data, recObj.SampleRate);
        disp('Archivo de Audio grabado correctamente');
      catch
        disp('Error al grabar el audio');
      end_try_catch
      
    case 2
      % Reproducción de audio
      try
        [data, fs] = audioread('audio.wav');
        sound(data, fs);
      catch
        disp('Error al reproducir el audio');
      end_try_catch
      
    case 3
      % Gráfica de audio
      try
        [data, fs] = audioread('audio.wav');
        tiempo = linspace(0, length(data)/fs, length(data));
        plot(tiempo, data);
        xlabel('Tiempo (s)');
        ylabel('Amplitud');
        title('Audio');
      catch
        disp('Error al graficar el audio.');
      end_try_catch
    case 4
      % Graficando espectro de frecuencia
      try
        disp('Graficando espectro de frecuencia...');
        [audio, Fs] = audioread('audio.wav'); %Lee la señal desde el archivo .wav
        N = length(audio); %Número de muestras de la señal
        f = linspace(0, Fs/2, N/2+1); %Vector de frecuencias
        ventana = hann(N); % Ventana de Hann para reducir el efecto de las discontinuidades al calcular la FFT
        Sxx = pwelch(audio, ventana, O, N, Fs); % Densidad espectral de potencia
        plot(f, 10*log10(Sxx(1:N/2+1))); % Grafica el espectro de frecuencia en dB
        xlabel('Frecuencia (Hz)');
        ylabel('Densidad espectral de potencia (dB/Hz)');
        title('Espectro de frecuencia de la señal grabada');
    catch
      disp('Error al graficar el audio.');
    end_try_catch
  case 5
    % Leer archivo de audio WAV
    [x, fs] = audioread('audio.wav');
    
    % Convertir la señal monoaural
    x = mean(x, 2);
    
    %Calcula Transdormada Z
    z = tf(x, 1); 
    
    %Obtener coeficientes de la Transformada Z
    [b, a] = tfdata(z, "vector");
    
    %Aplicar Transformada Z al archivo de audio
    y = filter(b, a, x);
    
    % Graficar señal original y señal con Transformada Z aplicada
    t = 0:1/fs:(length(x)-1)/fs;
    subplot(2, 1, 1);
    plot(t, x);
    xlabel("Tiempo(s)");
    ylabel("Amplitud");
    title("Señal Original");
    
    subplot(2, 1, 2);
    plot(t, y);
    xlabel("Tiempo(s)");
    ylabel("Amplitud");
    title("Señal con Transformada Z aplicada");
    
    %Escribir archivo de audio WAV con Transformada Z aplicada
    audiowrite("archivo_audio_con_Z.wav", y, fs);
    
  case 6
    # Leer archivo de audio
    [y, fs] = audioread('audio.wav');
    
    # Realizar DCT
    dct_y = dct(y);
    
    # Establecer el umbral para la compresión
    umbral = 0.1;
    
    # Comprimir DCT
    dct_y_comprimido = dct_y.*(abs(dct_y)>umbral);
    
    #Realizar la inversa de la DCT para obtener el archivo de audio comprimido
    y_comprimido = idct(dct_y_comprimido);
    
    # Graficar el archivo inicial y final
    t = (0:length(y)-1)/fs;
    t_comp = (0:length(y_comprimido)-1)/fs;
    
    subplot(2,1,1);
    plot(t,y)
    title('Archivo de audio inicial')
    xlabel('Tiempo(s)');
    ylabel('Amplitud');
    
    subplot(2,1,2);
    plot(t_comp, y_comprimido);
    title('Archivo de audio comprimido');
    xlabel('Tiempo(s)');
    ylabel('Amplitud');
   
  case 7
    %Salir
    disp('Saliendo del programa...');
    break
  otherwise
    disp('Opción no válida.');
  end   
  end
