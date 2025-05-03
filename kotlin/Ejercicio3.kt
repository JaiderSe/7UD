package com.example.variables

fun pedirDatosEstudiantes(): Pair<String, Int> {
    println("Introduce el nombre del estudiante:")
    val nombre1 = readLine() ?: "Sin Nombre"
    println("Introduce la edad del primer estudiante:")
    val edad1 = readLine()?.toIntOrNull() ?: 0

    return Pair(nombre1, edad1)
}


fun imprimirMayor(nombre1: String, edad1: Int, nombre2: String, edad2: Int): String {

    var a: String = ""

    when {
        edad1 > edad2 -> a=("$nombre1 es mayor que $nombre2")
        edad2 > edad1 -> a=("$nombre2 es mayor que $nombre1")
        else -> a=("$nombre1 y $nombre2 tienen la misma edad")
    }
    return a
}

fun main() {
    // Pedimos los datos de los dos estudiantes
    val (nombre1, edad1) = pedirDatosEstudiantes()
    val (nombre2, edad2) = pedirDatosEstudiantes() // Llamamos de nuevo para el segundo estudiante

    // Imprimimos quién es mayor
    println(imprimirMayor(nombre1, edad1, nombre2, edad2))
}
// control/command + click
// video: https://udistritaleduco-my.sharepoint.com/:v:/g/personal/jsmorenoq_udistrital_edu_co/Ef14FapIibdAvtfmCqWipQwBYfDsGf_3yWWUlenzb_lwjQ?e=B0Isdk&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1MaW5rIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXcifX0%3D


