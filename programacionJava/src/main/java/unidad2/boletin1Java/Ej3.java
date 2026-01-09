package unidad2.boletin1Java;

import java.util.Scanner;

public class Ej3 {
    static void main(String[] args) {
        Ej3 referencia = new Ej3();
        Scanner b = new Scanner(System.in);
        System.out.print("Dime cuanto mide la base: ");
        int base = b.nextInt();
        Scanner h = new Scanner(System.in);
        System.out.print("Dime cuanto mide la altura: ");
        int altura = h.nextInt();
        System.out.print("El area es: ");
        System.out.print(referencia.area(base,altura));
    }
    int area (int b, int h) {
        int resArea = b * h;
        return resArea;
    }
}
