package unidad2.toma_de_contacto;

import java.util.Scanner;

public class Dia2 {
    public static void main(String[] args) {

        float z = 3.0F;
        float y = 4.0F;
        float resultado = y / z - y * z;
        System.out.println(resultado);

        float x = 3.0F;
        double res = x - 3.0;
        res = res - 3.0;
        System.out.println(res);

        int entero;
        float numero = 1.12123F;
        double decimalGrande = 5.6789; //casting implicito porque NO pierdo información
        numero = (float) decimalGrande; //casting explicito porque pierdo información
        entero = (int) numero; //casting explicito porque pierdo información
        System.out.println(numero);
        System.out.println(entero);

        Scanner escaner = new Scanner(System.in);
        String cadena = escaner.next(); // Me lee hasta espacio en blanco y guarda en variable llamada cadena
        String linea = escaner.nextLine(); // Lee la frase entera con espacios
        int numeroEntero = escaner.nextInt();

        System.out.println(cadena);
        System.out.println(linea);
        System.out.println(numeroEntero);
    }
}