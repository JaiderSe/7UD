% Parámetros de la señal
fs = 10000; % Frecuencia de muestreo (Hz)
t = 0:1/fs:0.1; % Vector de tiempo (0.1 segundos)
fc = 100; % Frecuencia de la portadora (Hz)
fm = 10; % Frecuencia de la señal moduladora (Hz)
Am = 1; % Amplitud de la señal moduladora
Ac = 1; % Amplitud de la portadora
beta = 2; % Índice de modulación para FM

% Señal moduladora
m = Am * cos(2 * pi * fm * t);

% Modulación AM
s_am = (1 + m) .* (Ac * cos(2 * pi * fc * t));

% Modulación FM
s_fm = Ac * cos(2 * pi * fc * t + beta * sin(2 * pi * fm * t));

% Transformada de Fourier para análisis en frecuencia
nfft = 2^nextpow2(length(t)); % Tamaño de la FFT
f = fs * (0:(nfft/2)-1) / nfft; % Vector de frecuencias

% FFT de la señal AM
S_AM = fft(s_am, nfft) / length(t);
S_AM = abs(S_AM(1:nfft/2));

% FFT de la señal FM
S_FM = fft(s_fm, nfft) / length(t);
S_FM = abs(S_FM(1:nfft/2));

% Gráficas
figure;

% Señal AM en el dominio del tiempo
subplot(3, 2, 1);
plot(t, s_am);
title('Señal AM en el tiempo');
xlabel('Tiempo (s)');
ylabel('Amplitud');

% Señal AM en el dominio de la frecuencia
subplot(3, 2, 2);
plot(f, S_AM);
title('Espectro de la señal AM');
xlabel('Frecuencia (Hz)');
ylabel('Magnitud');

% Señal FM en el dominio del tiempo
subplot(3, 2, 3);
plot(t, s_fm);
title('Señal FM en el tiempo');
xlabel('Tiempo (s)');
ylabel('Amplitud');

% Señal FM en el dominio de la frecuencia
subplot(3, 2, 4);
plot(f, S_FM);
title('Espectro de la señal FM');
xlabel('Frecuencia (Hz)');
ylabel('Magnitud');

% Señal moduladora
subplot(3, 2, 5);
plot(t, m);
title('Señal moduladora');
xlabel('Tiempo (s)');
ylabel('Amplitud');

% Portadora
subplot(3, 2, 6);
plot(t, Ac * cos(2 * pi * fc * t));
title('Portadora');
xlabel('Tiempo (s)');
ylabel('Amplitud');