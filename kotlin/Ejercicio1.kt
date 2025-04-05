package com.example.variables

import kotlin.math.PI
import kotlin.math.sin
import kotlin.math.cos


fun main (){

    var booleano: Boolean = true
    var int8: Byte = 127
    var int16: Short = 32767
    var int32: Int = 1415926535
    var int64: Long = 1234567890123456789
    var string: String= "\n El número PI es: "
    var string2: String= "\n Y es similar a:  "
    var character: Char = '.'
    var flotante: Float = 0.14f
    var doble: Double = 0.001592653589793
    var hexFormat: Int = 0xFF

    doble +=  (int8-124) + flotante.toDouble()
    int16 = (2+(hexFormat.toShort())-(int8.toShort())*2).toShort()



    print(string+doble+"\n")
    print(string2+int16+character+int32+int64)

    print("\n la suma de los enteros de 8 y 16 es: "+(int8+int16).toString())
    print("\n la suma de los enteros de 32 y 64 es: "+(int32+int64).toString())
    print("\n la suma de los string y caracter es: "+string+character)
    print("\n la suma de los flotantes y double es: "+flotante.toString()+doble)
    print("\n la suma de los hexadecimales es: "+(hexFormat+0x2f).toInt())



}

// video:
/**
 * video:
 *
 * https://udistritaleduco-my.sharepoint.com/:v:/g/personal/jsmorenoq_udistrital_edu_co/ETpPZUU5ht1AgtHioflXa7UBUoEbe3jcEHSFx7Wss5nRkw?e=jMfF1r&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1MaW5rIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXcifX0%3D
 *
 * */



