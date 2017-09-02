
import java.util.Scanner;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author linho
 */
public class Tarefa08c {
    public static void main(String[] args) {
        Scanner tec = new Scanner(System.in);
        int n = Integer.parseInt(tec.nextLine());
        for (int i = 0; i < n; i++) {
            String[] bin = tec.nextLine().split(" ");
            int n1 = Integer.parseInt(bin[0],2);
            int n2 = Integer.parseInt(bin[1],2);
            if(mdc(n1,n2)>1){
                System.out.println("V");
            }else{
                System.out.println("F");
            }
        }System.out.println("");
    }
    public static int mdc(int a, int b){
        if(b==0){
            return a;
        }else 
            return mdc(b,a%b);
        
    }
}
