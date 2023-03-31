# Pancakes A*

Este programa resuelve el problema de pancake sorting mediante el uso del algoritmo A*.

**Lenguaje utilizado**: Python

## Funciones

 ### **'Voltear(self, posicion, pancakes)'**
Esta funcion recibe como parametro la posición donde se van a voltear los pancakes y los pancakes que se van a voltear y devuelve los pancakes volteados desde esa posición.

### **'h(self, nodo)'**
Esta función se encarga de la heuristica del programa, recibe como parametro el nodo al que se le va a calcular la heuristica y devuelve un valor entero que indica la heuristica de ese nodo.

 ### **'busqAStar(self, nodo)'**
 Esta funcion recibe como parametro el nodo a partir del cual se realizará la busqueda en amplitud y va a retornar la serie de movimientos que se tiene que realizar para ordenar de menor a mayor los pancakes.
 
 ## Como utilizar el código
Para poder utilizar el código se tiene que crear una instancia de la clase "Pancakes" añadiendole como parametro una lista desordenada  
de letras minusculas y luego llamar a la funcion busqAStar() dandole como parametro la lista a ordenar. El resultado de la ejecución  
será una serie de numeros que indican los movimientos que se tienen que realizar para resolver ese problema.
 
A continuación se presenta un ejemplo de como utilizar el código:

![image](https://user-images.githubusercontent.com/125157604/229012805-1c729ca9-d48b-4da7-971f-47c99e621102.png)
