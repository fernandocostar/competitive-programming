
import java.util.Arrays;
import java.util.Scanner;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author fernando
 */
public class Tarefa08b {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Scanner tec = new Scanner(System.in);
        long[] lisos = lisos(5842);
        int n = tec.nextInt();
        while(n != 0){
            System.out.println(lisos[n-1]);
            n = tec.nextInt();
        }
        System.out.println("");
        
    }

    private static long[] lisos(int i) {
        long[] lisos = new long[i];
        lisos[0] = 1;
        int k = 1;
        long n = 0;
        for (int j = 0; k < i; j++) {
            n = lisos[j]*2;
            if(!jaTem(n,lisos)&&n<=2000000000){
                lisos[k]=n;
                k++;
            }
            n = lisos[j]*3;
            if(!jaTem(n,lisos)&&n<=2000000000){
                lisos[k]=n;
                k++;
            }
            n = lisos[j]*5;
            if(!jaTem(n,lisos)&&n<=2000000000){
                lisos[k]=n;
                k++;
            }
            n = lisos[j]*7;
            if(!jaTem(n,lisos)&&n<=2000000000){
                lisos[k]=n;
                k++;
            }
        }
        Arrays.sort(lisos);
        return lisos;
    }

    private static boolean jaTem(long n, long[] lisos) {
        for (int i = 0; i < lisos.length; i++) {
            if(lisos[i]==n)return true;
        }
        return false;
    }
    
}
