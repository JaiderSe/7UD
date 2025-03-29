% Analizar el espectro de una onda seno con slider
function seno_espectro()
    % Crear la figura y el slider
    f = figure('Name', 'Espectro de Onda Seno', 'NumberTitle', 'off');
    slider = uicontrol('Style', 'slider', 'Min', 1, 'Max', 1000, 'Value', 100, ...
                       'Position', [100, 20, 300, 20], 'Callback', @updatePlot);
    uicontrol('Style', 'text', 'Position', [50, 20, 50, 20], 'String', 'Freq');
    freqLabel = uicontrol('Style', 'text', 'Position', [410, 20, 50, 20], 'String', '100 Hz');
    
    % Parámetros iniciales
    fs = 1000; % Frecuencia de muestreo
    t = 0:1/fs:1-1/fs; % Vector de tiempo
    freq = 100; % Frecuencia inicial de la onda seno
    
    % Crear el gráfico inicial
    ax1 = subplot(2, 1, 1);
    ax2 = subplot(2, 1, 2);
    plotSineAndSpectrum(freq);
    
    % Función para actualizar el gráfico
    function updatePlot(~, ~)
        freq = round(slider.Value);
        freqLabel.String = [num2str(freq) ' Hz'];
        plotSineAndSpectrum(freq);
    end

    % Función para graficar la onda seno y su espectro
    function plotSineAndSpectrum(freq)
        % Onda seno
        y = sin(2 * pi * freq * t);
        axes(ax1);
        plot(t, y);
        title('Onda Seno');
        xlabel('Tiempo (s)');
        ylabel('Amplitud');
        grid on;
        
        % Espectro
        Y = fft(y);
        f = (0:length(Y)-1) * fs / length(Y);
        axes(ax2);
        plot(f(1:floor(end/2)), abs(Y(1:floor(end/2))));
        title('Espectro de Frecuencia');
        xlabel('Frecuencia (Hz)');
        ylabel('Magnitud');
        grid on;
    end
end