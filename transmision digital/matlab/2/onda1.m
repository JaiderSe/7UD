clear;
close all;
clc;

% Definir la función escalón unitario
u = @(t) (t >= 0); 

% Rango de tiempo
t = -2:0.01:10; 

% Definir la función por partes
y =((2+sin(2*pi*t)).*(u(t)-u(t-1))+(-4*t+6).*(u(t-1)-u(t-2))+(-2+sin(2*pi*t)).*(u(t-2)-u(t-3)))+4;
% Graficar la función
plot(t, y, 'r', 'LineWidth', 2);
axis([-1 8 -5 5]); % Límites de los ejes
grid on;
xlabel('Tiempo (t)');
ylabel('y(t)');
title('Gráfica de la función definida por partes');