package unidad2.boletin1Java;

import java.util.Scanner;

public class Ej2 {
    static void main(String[] args) {
        Ej2 referencia = new Ej2();
        Scanner num1 = new Scanner(System.in);
        System.out.print("Dime el primer numero: ");
        int numero1 = num1.nextInt();
        Scanner num2 = new Scanner(System.in);
        System.out.print("Dime el segundo numero: ");
        int numero2 = num2.nextInt();
        System.out.print("La multiplicacion es: ");
        System.out.print(referencia.multiplicacion(numero1,numero2));
    }
    int multiplicacion (int num1, int num2){
        int resMultiplicacion = num1 * num2;
        return resMultiplicacion;
    }
}

