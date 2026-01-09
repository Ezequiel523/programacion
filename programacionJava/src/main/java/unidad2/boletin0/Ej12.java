package unidad2.boletin0;

import java.util.Scanner;

public class Ej12 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Dime una contraseña: ");
        int contrasena = scanner.nextInt();

        while (contrasena != 1234){
            System.out.print("Dime de nuevo la contraseña: ");
            contrasena = scanner.nextInt();
        }
        System.out.print("Bienvenido");
    }
}
