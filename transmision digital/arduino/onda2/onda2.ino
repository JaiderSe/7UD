// Definición de pines
const int pwmPin = 9; 

// Parámetros de la señal
const int numPoints = 2000;
const float t_max = 12;     
const float dt = t_max / numPoints; 

// Arreglo para guardar la señal
byte signal[numPoints];

void setup() {
  // Inicialización
  pinMode(pwmPin, OUTPUT);

  // Generar los valores de la señal
  for (int i = 0; i < numPoints; i++) {
    float t = i * dt;
    float y = 0;

    if (t >= 0 && t < 3) {
      y = (2.0/3.0) * t;
    }
    else if (t >= 3 && t <= 6) {
      y = 3.0;
    }
    else if (t > 6 && t < 10) {
      y = -(3.0/4.0)*t + 11.0/2.0;
    }
    else {
      y = 0;
    }

    y=y+3;
    
    // Normalizar (rango máximo aproximado entre 0 y 3 o 4)
    int pwm_value = map(y * 100, 0, 400, 0, 255);
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
