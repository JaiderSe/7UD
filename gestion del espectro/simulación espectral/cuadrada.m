clc; clear; close all;

% Parámetros
Fs = 1e5;             % Frecuencia de muestreo (Hz)
t = 0:1/Fs:0.01;      % Tiempo (10 ms)
fc = 1e4;             % Frecuencia portadora (Hz)
fm = 1e3;             % Frecuencia de modulación (Hz)
Am = 1;               % Amplitud de la señal moduladora
Ac = 1;               % Amplitud de la portadora
modIndex = 0.5;       % Índice de modulación AM

% Señales
portadora = Ac * cos(2*pi*fc*t);
moduladora = Am * cos(2*pi*fm*t);
senalAM = (1 + modIndex * moduladora) .* portadora;

% FFT
N = length(t);
f = (-N/2:N/2-1)*(Fs/N);
spectrumCW = abs(fftshift(fft(portadora)));
spectrumAM = abs(fftshift(fft(senalAM)));

% Gráficas
figure;

subplot(2,2,1);
plot(t*1e3, portadora);
title('Portadora (CW) - Dominio del Tiempo');
xlabel('Tiempo (ms)');
ylabel('Amplitud');

subplot(2,2,2);
plot(f/1e3, spectrumCW);
title('Portadora (CW) - Espectro');
xlabel('Frecuencia (kHz)');
ylabel('|FFT|');

subplot(2,2,3);
plot(t*1e3, senalAM);
title('Señal AM - Dominio del Tiempo');
xlabel('Tiempo (ms)');
ylabel('Amplitud');

subplot(2,2,4);
plot(f/1e3, spectrumAM);
title('Señal AM - Espectro');
xlabel('Frecuencia (kHz)');
ylabel('|FFT|');
