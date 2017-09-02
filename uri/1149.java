import java.io.IOException;
import java.util.Scanner;
 
/**
 * IMPORTANT: 
 *      O nome da classe deve ser "Main" para que a sua solução execute
 *      Class name must be "Main" for your solution to execute
 *      El nombre de la clase debe ser "Main" para que su solución ejecutar
 */
public class 1149 {
 
    public static void main(String[] args) throws IOException {
 		Scanner s = new Scanner(System.in);
        int a = s.nextInt();
        int n;
        do{
        	n = s.nextInt();
        }while(n <= 0);
        int sum = 0;
        for(int i = a; i < a+n; i++){
        	sum += i;
        }
        System.out.println(sum);
    }
 
}