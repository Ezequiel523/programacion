package unidad2.boletin1Java;

public class Ej1 {
    static void main(String[] args) {
        int x = 144;
        int y = 999;
        Ej1 referencia = new Ej1();

        System.out.print("la suma es: ");
        System.out.println(referencia.suma(x,y));
        System.out.print("La resta es: ");
        System.out.println(referencia.resta(x,y));
        System.out.print("La multiplicacion es: ");
        System.out.println(referencia.multiplicacion(x,y));
        System.out.print("La division es: ");
        System.out.println(referencia.division(x,y));
    }

        int suma(int x, int y){
            int resSuma = x + y;
            return resSuma;
        }
        int resta(int x, int y){
            int resResta = x - y;
            return resResta;
        }
        int multiplicacion(int x, int y){
            int resMultiplicacion = x * y;
            return resMultiplicacion;
        }
        int division(int x, int y){
            int resDivision = x % y;
            return resDivision;
        }
}
