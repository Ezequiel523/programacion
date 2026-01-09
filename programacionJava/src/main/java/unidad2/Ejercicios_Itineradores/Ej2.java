package unidad2.Ejercicios_Itineradores;

import java.util.Scanner;

public class Ej2 {
    static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Dime un numero de filas: ");
        int num =  scanner.nextInt();
        String cadena = "";
        for (int i=0; i<num;i++){
            System.out.println(cadena += "*");
        }
    }
}
