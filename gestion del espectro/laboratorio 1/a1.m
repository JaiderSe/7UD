clc; clear; close all;

fs = 100e6; % Frecuencia de muestreo (100 MHz)
f = 10e6;   % Frecuencia de la señal (10 MHz)
t = 0:1/fs:1e-6; % Vector de tiempo (1 microsegundo)

% Señal
signal = sin(2*pi*f*t);

% Transformada de Fourier
N = length(signal);
frequencies = (-N/2:N/2-1)*(fs/N); % Eje de frecuencias
spectrum = fftshift(abs(fft(signal))); % Magnitud del espectro

% Gráficas
figure;

% Señal en el dominio del tiempo
subplot(2,1,1);
plot(t*1e6, signal); % Escala de tiempo en microsegundos
title('Señal en el dominio del tiempo');
xlabel('Tiempo (\mus)');
ylabel('Amplitud');
grid on;

% Espectro en el dominio de la frecuencia
subplot(2,1,2);
plot(frequencies/1e6, spectrum); % Escala de frecuencia en MHz
title('Espectro de la señal');
xlabel('Frecuencia (MHz)');
ylabel('Magnitud');
grid on;