
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
/**
 *
 * @author desafiosprog
 */
public class Tarefa09a {

    static int[][] pieces;
    static int[] visitados;
    static Queue<Integer> prox;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t, m, n, a, b, count;

        t = sc.nextInt();

        for (int i = 0; i < t; i++) {
            count = 0;
            n = sc.nextInt();
            m = sc.nextInt();
            visitados = new int[n];
            pieces = new int[n][n];
            for (int j = 0; j < m; j++) {
                a = sc.nextInt() - 1;
                b = sc.nextInt() - 1;
                pieces[a][b] = 1;
            }
            prox = new LinkedList<>();
            prox.add(0);

            while (hasNotVisited()) {
                count++;
                visitaLargura(prox);
            }

            System.out.println(count);
        }

    }

    static void visitaLargura(Queue<Integer> prox) {
        int atual;
        while (!prox.isEmpty()) {
            atual = prox.remove();
            visitados[atual] = 1;
            for (int j = 0; j < visitados.length; j++) {
                if (atual != j && pieces[atual][j] == 1) {
                    prox.add(j);
                }
            }
        }

    }

    private static boolean hasNotVisited() {

        for (int i = 0; i < visitados.length; i++) {
            if (visitados[i] == 0) {
                prox.add(i);
                return true;
            }
        }
        return false;

    }

}
