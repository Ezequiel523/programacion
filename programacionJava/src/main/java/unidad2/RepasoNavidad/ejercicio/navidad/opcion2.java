/*package unidad2.RepasoNavidad.ejercicio.navidad;

import java.util.Random;
import java.util.Scanner;

public class opcion2 {
    static void main(String[] args) {
        int hp = 100;
        int hpMonstruo = 80;
        int mp = 20;
        Random random = new Random();
     Scanner nombre = new Scanner(System.in);
        System.out.print("Dame el nombre de tu héroe: ");
        String heroe = nombre.next();
    public int pintaMenu(){
        System.out.println(heroe + ":" + hp + "puntos de vida (HP) y" + mp + "puntos de energía (MP).\n" +
                    "Monstruo:" + hpMonstruo + "puntos de vida (HP).");
            while (hp > 0 && hpMonstruo > 0) {
            System.out.println("1. Ataque Básico: No consume energía. El daño será un valor aleatorio entre 7 y 12.\n" +
                    "2. Ataque Especial: Consume 5 puntos de energía. El daño será un valor aleatorio entre 15 y 25. (Solo si tiene energía suficiente).\n" +
                    "3. Curar: Consume 8 de energía y recupera 20 de vida.\n");

            Scanner ataques = new Scanner(System.in);
            System.out.print("Dame el ataque que quieras hacer: ");
            int ataque = ataques.nextInt();
        }

                return opcion1
            }
        }

     */