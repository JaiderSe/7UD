clear;
close all;
clc;

% Definir la función escalón unitario
u = @(t) (t >= 0); 

% Rango de tiempo
t = 0:0.01:8; 

% Definir la función por partes
y =(sin(2*pi*0.5*t)+2).*(u(t-4)-u(t-6)); % Oscilación senoidal entre t = 2 y t = 3

% Graficar la función
plot(t, y, 'r', 'LineWidth', 2);
axis([0 8 -2 4]); % Límites de los ejes
grid on;
xlabel('Tiempo (t)');
ylabel('y(t)');
title('Gráfica de la función definida por partes');