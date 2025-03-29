% escalon_unitario.m
% Este programa grafica el escalón unitario.

% Definir el rango de tiempo
t = -10:0.01:10;

% Definir el escalón unitario
u = t >= 0;

% Graficar el escalón unitario
figure;
plot(t, u, 'LineWidth', 2);
grid on;
xlabel('Tiempo (t)');
ylabel('u(t)');
title('Escalón Unitario');
xlim([-10 10]);
ylim([-0.5 1.5]);