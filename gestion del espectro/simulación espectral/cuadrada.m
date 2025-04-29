% Parámetros de la simulación
fs = 1e4; % Frecuencia de muestreo (Hz) 
t = 0:1/fs:0.1; % Vector de tiempo (0.1 segundos)
f_carrier = 1000; % Frecuencia de la portadora (Hz)
f_square = 50; % Frecuencia de la señal cuadrada (Hz)
A_carrier = 1; % Amplitud de la portadora
mod_index_AM = 0.5; % Índice de modulación AM
mod_index_FM = 50; % Índice de modulación FM

% Generar la señal cuadrada
square_signal = square(2*pi*f_square*t); 

% Modulación AM
am_signal = (1 + mod_index_AM * square_signal) .* A_carrier .* cos(2*pi*f_carrier*t);

% Modulación FM
fm_signal = A_carrier * cos(2*pi*f_carrier*t + mod_index_FM * square_signal);

% Transformada de Fourier para análisis en frecuencia
n = length(t);
f = (-n/2:n/2-1)*(fs/n); % Vector de frecuencias

% FFT de las señales
am_spectrum = fftshift(abs(fft(am_signal))/n);
fm_spectrum = fftshift(abs(fft(fm_signal))/n);

% Gráficas
figure;

% Señal AM en tiempo
subplot(3,2,1);
plot(t, am_signal);
title('Señal AM en el tiempo');
xlabel('Tiempo (s)');
ylabel('Amplitud');

% Espectro de la señal AM
subplot(3,2,2);
plot(f, am_spectrum);
title('Espectro de la señal AM');
xlabel('Frecuencia (Hz)');
ylabel('Magnitud');

% Señal FM en tiempo
subplot(3,2,3);
plot(t, fm_signal);
title('Señal FM en el tiempo');
xlabel('Tiempo (s)');
ylabel('Amplitud');

% Espectro de la señal FM
subplot(3,2,4);
plot(f, fm_spectrum);
title('Espectro de la señal FM');
xlabel('Frecuencia (Hz)');
ylabel('Magnitud');

% Señal cuadrada original
subplot(3,2,5);
plot(t, square_signal);
title('Señal cuadrada original');
xlabel('Tiempo (s)');
ylabel('Amplitud');

% Espectro de la señal cuadrada
square_spectrum = fftshift(abs(fft(square_signal))/n);
subplot(3,2,6);
plot(f, square_spectrum);
title('Espectro de la señal cuadrada');
xlabel('Frecuencia (Hz)');
ylabel('Magnitud');