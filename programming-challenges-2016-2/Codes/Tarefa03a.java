
import java.util.*;

public class Tarefa03a {

    public static void main(String args[]) {
        Scanner input = new Scanner(System.in);
        int x = input.nextInt();
        for (int i = 0; i < x; i++) {
            String entrada = input.next();
            
            if(entrada.equals("")){
                System.out.println("sim");
            }
            if (verifica(entrada) == true) {
                System.out.println("sim");
            }

            if (verifica(entrada) == false) {
                System.out.println("nao");
            }

        }
    }

    public static boolean verifica(String str) {
        Stack<Character> pilha = new Stack<Character>();

        char p1 = '(';
        char p2 = ')';
        char br1 = '{';
        char br2 = '}';
        char bk1 = '[';
        char bk2 = ']';

        for (int i = 0; i < str.length(); i++) {
            if (str.charAt(i) == p1) {
                pilha.push(p1);
            } else if (str.charAt(i) == br1) {
                pilha.push(br1);
            } else if (str.charAt(i) == bk1) {
                pilha.push(bk1);
            } else if (str.charAt(i) == p2) {
                if (pilha.isEmpty()) {
                    return false;
                }
                if (pilha.pop() != p1) {
                    return false;
                }
            } else if (str.charAt(i) == br2) {
                if (pilha.isEmpty()) {
                    return false;
                }
                if (pilha.pop() != br1) {
                    return false;
                }
            } else if (str.charAt(i) == bk2) {
                if (pilha.isEmpty()) {
                    return false;
                }
                if (pilha.pop() != bk1) {
                    return false;
                }
            }
        }
        return pilha.isEmpty();
    }

}
