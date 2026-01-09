package unidad2.boletin1Java;

import java.util.Random;
import java.util.Scanner;

public class Ej10 {
    static void main(String[] args) {
        Random random = new Random();
        int numAdivinar = random.nextInt(10);

        Ej10 ref = new Ej10();
        ref.adivinaNumero(numAdivinar);
    }
    void adivinaNumero (int numAdivinar){
        Scanner escaner = new Scanner(System.in);
        System.out.print("Introduce un numero: ");
        int num = escaner.nextInt();
        int numIntentos = 0;
        while (num != numAdivinar){
            System.out.print("Introduce otro numero: ");
            num = escaner.nextInt();
            numIntentos = numIntentos + 1;
        }
        System.out.print("Numero correcto. El numero era el " + numAdivinar);
        System.out.println(" has utilizado " + numIntentos + " intentos");
    }
}
