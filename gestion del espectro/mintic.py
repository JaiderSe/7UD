import csv

# Datos de preguntas y respuestas en formato Anki (Pregunta, Respuesta)
flashcards = [
    ["¿Qué es la longitud de onda de una señal?", "Es la distancia entre dos crestas consecutivas de una onda y está inversamente relacionada con la frecuencia."],
    ["¿Cuáles son las cualidades de la longitud de onda?", "Se relaciona con la frecuencia, influye en la propagación, afecta la difracción y dispersión, impacta el diseño de antenas y la absorción/reflexión en distintos medios."],
    ["¿Por qué usamos una señal senoidal en telecomunicaciones y no una cuadrada u otra?", "Porque las señales senoidales tienen una sola frecuencia, minimizan interferencias, son más eficientes en modulación y transmisión, y evitan la generación de armónicos no deseados."],
    ["¿Qué son los armónicos?", "Son componentes de frecuencia múltiplos de la frecuencia fundamental, que aparecen en señales periódicas no senoidales y pueden generar interferencias."],
    ["Diferencia entre ancho de banda y velocidad de transmisión", "El ancho de banda mide la capacidad del canal en Hz o bps, mientras que la velocidad de transmisión es la cantidad real de datos enviados en bps, dependiendo de factores como interferencias y congestión."],
    ["¿Cuál es la diferencia entre el MinTIC y la ANE en Colombia?", "El MinTIC define políticas de TIC y telecomunicaciones, mientras que la ANE gestiona y vigila el uso eficiente del espectro radioeléctrico."]
]

# Nombre del archivo CSV
csv_filename = "./flashcards1/flashcards1.csv"

# Crear y guardar el archivo CSV
with open(csv_filename, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Pregunta", "Respuesta"])  # Encabezados
    writer.writerows(flashcards)

csv_filename
