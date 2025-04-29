clear;
close all;
clc;

% Definir la función escalón unitario
u = @(t) (t >= 0); 

% Rango de tiempo
x = -1:0.01:10; 
t = x*4;
% Definir la función por partes
%y = (-cos(0.5*pi*t)+1).*(u(t)-u(t-4))+(cos(0.5*pi*t)-1).*(u(t-4)-u(t-8));
y = 0.5*(-cos(0.5*pi*t)+1).*(u(t)-u(t-4))+0.5*(cos(0.5*pi*t)-1).*(u(t-4)-u(t-8));
g = y*2;
% Graficar la función
plot(t, g, 'r', 'LineWidth', 2);
hold on;
%plot(t, g, 'b', 'LineWidth', 2);
axis([0 8 -3 3]); % Límites de los ejes
hold off;
grid on;


xlabel('Tiempo (t)');
ylabel('y(t)');
title('Gráfica de la función definida por partes');