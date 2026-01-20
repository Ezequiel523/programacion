package unidad2.toma_de_contacto;

public class pruebaLista2 {
    static void main(String[] args) {
        int [] tabla;
        int [] tabla2 = {1,2,3,4};

        tabla = tabla2;
        tabla2[3] = 8;
        tabla = tabla2;
    }
}
