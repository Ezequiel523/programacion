package unidad2.boletin0;

import java.util.Scanner;

public class Ej10 {
    static  void main(){
        Scanner scanner = new Scanner(System.in);
        System.out.print("Dime un número: ");
        int numero1 = scanner.nextInt();
        System.out.print("Dime un número: ");
        int numero2 = scanner.nextInt();

        float division = (float) numero1/numero2;

        if (numero2 != 0) {
            System.out.print("El resultado de la división es: ");
            System.out.print(+division);
        }
        else {
            System.out.println("El segundo número no puede ser 0");

        }
    }
}
