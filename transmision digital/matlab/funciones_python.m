% Leer el archivo CSV
file_path = './csv/ejercicio3.csv';

% Saltar las primeras filas innecesarias y cargar los datos correctamente
data = readtable(file_path, 'HeaderLines', 1, 'Delimiter', ',', 'ReadVariableNames', true, 'VariableNamingRule', 'preserve');

% Asegurarse de que las columnas necesarias existan
if all(ismember({'Sequence', 'Volt'}, data.Properties.VariableNames))   
    x = data.Sequence;
    y = data.Volt;
else
    disp("Las columnas 'Sequence' y 'Volt' no se encontraron en el archivo CSV.");
    disp("Por favor, verifica el archivo CSV.");
    return;
end

% Graficar la onda seno
figure;
plot(x, y, 'b', 'DisplayName', 'Funcion');
title('Gráfica de Onda');
xlabel('X');
ylabel('Y');
legend;
grid on;
