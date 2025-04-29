// Definición de pines
const int pwmPin = 9; // Puedes usar cualquier pin PWM

// Parámetros de la señal
const int numPoints = 2000;   // Número de muestras
const float t_max = 3.0;     // Tiempo máximo (3 segundos como en tu ecuación)
const float dt = t_max / numPoints; // Incremento de tiempo

// Arreglo para guardar la señal
byte signal[numPoints];

void setup() {
  // Inicialización
  pinMode(pwmPin, OUTPUT);

  // Generar los valores de la señal
  for (int i = 0; i < numPoints; i++) {
    float t = i * dt;
    float y = 0;

    // Evaluar la función por tramos
    if (t >= 0 && t < 1) {
      y = 2 + sin(2 * PI * t);
    }
    else if (t >= 1 && t < 2) {
      y = -4 * t + 6;
    }
    else if (t >= 2 && t < 3) {
      y = -2 + sin(2 * PI * t);
    }

    y = y + 4; // Corrimiento para hacerla toda positiva

    // Normalizar de 0-8 a 0-255 (porque máximo y = 8)
    int pwm_value = map(y * 100, 0, 800, 0, 255); 

    // Guardarlo en el array
    signal[i] = constrain(pwm_value, 0, 255);
  }
}

void loop() {
  // Reproducir la señal periódicamente
  for (int i = 0; i < numPoints; i++) {
    analogWrite(pwmPin, signal[i]);
    delayMicroseconds(500); // Ajusta el tiempo para controlar la frecuencia
  }
}
