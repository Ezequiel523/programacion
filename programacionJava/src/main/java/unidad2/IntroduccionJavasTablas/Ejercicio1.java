package unidad2.IntroduccionJavasTablas;

public class Ejercicio1 {
    public static void main(String[] args) {

        String[] tabla = new String[7];
        tabla[0] = "Lunes";
        tabla[1] = "Martes";
        tabla[2] = "Miércoles";
        tabla[3] = "Jueves";
        tabla[4] = "Viernes";
        tabla[5] = "Sábado";
        tabla[6] = "Domingo";

        System.out.println("DÍAS DE LA SEMANA");
        for(int i = 0;i< tabla.length;i++){
        System.out.println(tabla[i]);
        }
    }
}

