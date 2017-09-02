import java.util.Scanner;

/**
 *
 * @author fernando
 */
public class tarefa01a {
    public static void main(String[]args){
        Scanner s = new Scanner(System.in);
        int t = s.nextInt();
        for(int i = 0; i<t; i++){
            int n = s.nextInt();
            n = ((((((( (n*567)/9))+7492)*235)/47) - 498)/10)%10;
            
            if(n<0){n = n*(-1);}
            
            System.out.println(n);
        }
        s.close();
    }
    
}

    
}
