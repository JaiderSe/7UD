% Tu función original con escalones
u = @(t) (t >= 0); 
t = 0:0.01:3; % en vez de -2:0.01:10
y =((2+sin(2*pi*t)).*(u(t)-u(t-1))+(-4*t+6).*(u(t-1)-u(t-2))+(-2+sin(2*pi*t)).*(u(t-2)-u(t-3)));

% Escalado para Arduino (de -5:5 a 0:255)
y_scaled = round((y + 5) * (255 / 10)); 

% Tomar 100 muestras
indices = round(linspace(1, length(y_scaled), 100));
y_arduino = y_scaled(indices);

% Mostrar en formato Arduino
fprintf('const byte signal[100] = {');
fprintf('%d, ', y_arduino(1:end-1));
fprintf('%d};\n', y_arduino(end));
