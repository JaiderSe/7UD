// Definición de pines
const int pwmPin = 9; // Puedes usar cualquier pin PWM

// Parámetros de la señal
const int numPoints = 1000;   // Número de muestras
const float t_max = 8;     // Tiempo máximo (3 segundos como en tu ecuación)
const float dt = t_max / numPoints; // Incremento de tiempo

// Arreglo para guardar la señal
byte signal[numPoints];

void setup() {
  // Inicialización
  pinMode(pwmPin, OUTPUT);

  // Generar los valores de la señal
  for (int i = 0; i < numPoints; i++) {
    float t = i * dt;
    float g = 0;

    if (t >= 0 && t < 4) {
      g = -cos(0.5 * PI * t) + 1;
    }
    else if (t >= 4 && t < 8) {
      g = cos(0.5 * PI * t) - 1;
    }
    else {
      g = 0;
    }

    // Escalar g(t) de -2 a 2 → a 0-255 para PWM
    int pwm_value = map(g * 1000, -2000, 2000, 0, 255);
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
