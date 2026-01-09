package unidad2.boletin0;

import java.util.Scanner;

public class Ej3 {
    static void main(String[] args) {
        Scanner numero1 = new Scanner(System.in);
        System.out.print("Dame el primer numero: ");
        int num1 = numero1.nextInt();
        Scanner numero2 = new Scanner(System.in);
        System.out.print("Dame otro numero: ");
        int num2 = numero2.nextInt();
        int multiplicacion = num1 * num2;
        System.out.print("la multiplicacion es: ");
        System.out.print(multiplicacion);

    }
}
