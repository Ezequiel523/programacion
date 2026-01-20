package unidad2.examen.pokemon;

import java.util.Scanner;

public class Ejercicio_pokemon {
    public void  menu(){
        System.out.println("1. Capturar Pokémon");
        System.out.println("2. Realizar Batalla");
        System.out.println("3. Mostrar Pokédex");
        System.out.println("4. Finalizar");
    }

    static void main(String[] args) {
        Ejercicio_pokemon r = new Ejercicio_pokemon();
        r.menu();
        Scanner escaner = new Scanner(System.in);
        System.out.print("Elige una de estas opciones:  ");
        int opcion = escaner.nextInt();
        String [] nombres = new String[15];
        int [] niveles = new int[15];
        int numPokemons= 0;

        while(opcion != 4) {

            if (opcion == 1) {
                System.out.println("Capturar Pokémon");
                numPokemons= r.capturarPokem(nombres, niveles, numPokemons);

            }
            else if (opcion == 2) {
                System.out.println("Realizar Batalla");
            }
            else if (opcion == 3) {
                System.out.println("Mostrar Pokédex");
            }
            else{
                r.menu();
                System.out.print("Opcion invalida.  ");
            }
            r.menu();
            System.out.print("Elige una de estas opciones:  ");
            opcion = escaner.nextInt();
        }
    }
    int capturarPokem(String [] nombres, int [] niveles, int numPokemons)
    {
        Scanner esc = new Scanner(System.in);
        System.out.print("Escribe el nombre del pokémon:  ");
        String  capPoke = esc.next();
        System.out.print("Dime el nivel inicial del pokémon:  ");
        int capPokemon = esc.nextInt();
        nombres[numPokemons]= capPoke;
        niveles[numPokemons] = capPokemon;
        return numPokemons+1;

    }
}
