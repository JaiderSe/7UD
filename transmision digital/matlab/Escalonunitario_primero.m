clear;
close all;
u = @ (t) (t>=0); % para tiempos mayores o iguales que cero la funcion vale 1 utilizando la funcion
t = (-10:0.01:10);
y = (3)*(u(t)-u(t-1))+(-2)*(u(t-1)-u(t-2))+(2)*(u(t-2)-u(t-3))+(-0.5)*(u(t-3)-u(t-4)+(3)*(u(t-4)-u(t-5)));

%****Triangulo
%y = t.*(u(t)-u(t-1))-t.*(u(t-1)-u(t-2));
%y = t.*(u(t)-u(t-1))+(-t+2).*(u(t-1)-u(t-2));
%y = (u(t)-u(t-1))+(t).*(u(t-1)-u(t-2))+(2).*(u(t-2)-u(t-3))+(-t+5).*(u(t-3)-u(t-5));
%y = (2/3*t).*(u(t)-u(t-3))+(3)*(u(t-3)-u(t-5))+(-5/3*t+28/3).*(u(t-5)-u(t-10));

header = {'X', 'CH1', 'Start', 'Increment,'};
metadata = {'Sequence', 'Volt', -2.950000e-03, 5.000000e-06};

% Crear el archivo CSV
fileID = fopen('./csv/ejercicio1.csv', 'w');
fprintf(fileID, '%s,%s,%s,%s\n', header{:}); % Escribir encabezado
fprintf(fileID, '%s,%s,%.6e,%.6e\n', metadata{:}); % Escribir metadatos

% Escribir los datos
for i = 1:length(t)
    fprintf(fileID, '%d,%.2e,\n', i-1, y(i));
end

fclose(fileID); 
disp('Datos guardados en ./csv/ejercicio1.csv'); % Mensaje de confirmación


plot (t,y,'r','LineWidth',2);
axis([-1 12   -8 4]);
%xlim([-1,8.5]);
%ylim([-2,2]);
grid on;