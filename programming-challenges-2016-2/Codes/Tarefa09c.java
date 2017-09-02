
import java.util.Scanner;

public class Tarefa09c {

    static boolean achou;

    public static void main(String[] args) {
        Scanner tec = new Scanner(System.in);
        int t = tec.nextInt();
        for (int i = 0; i < t; i++) {
            int n = tec.nextInt();
            int m = tec.nextInt();
            int[][] holes = new int[n][n];
            for (int j = 0; j < n; j++) {
                for (int k = 0; k < n; k++) {
                    holes[j][k] = 1001;
                }
            }
            for (int j = 0; j < m; j++) {
                int orig = tec.nextInt();
                int dest = tec.nextInt();
                int custo = tec.nextInt();
                holes[orig][dest] = custo;
            }

            int[] caminho = temVolta(holes, n);
            achou = false;
            while (caminho[2] < 0 && !achou) {
                boolean[] passos = new boolean[n];
                achaCaminho(caminho[1], caminho[0], holes, 0, caminho[2], passos);
                caminho = temVolta(holes, n);
            }
            if (achou) {
                System.out.println("sim");
            } else {
                System.out.println("nao");
            }
        }System.out.println("");

    }

    private static int[] temVolta(int[][] holes, int n) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                int custo = holes[i][j];
                if (custo < 0) {
                    int k = custo;
                    holes[i][j] = 1001;
                    int[] resp = {i, j, k};
                    return resp;
                }
            }
        }
        int[] resp = {0, 0, 10};
        return resp;
    }

    private static void achaCaminho(int orig, int dest, int[][] holes, int custo, int custoMax, boolean[] passos) {
        passos[orig] = true;
        if (orig == dest) {
            
            if (-custo > custoMax) {
                achou = true;
            }
        } else {
            for (int i = 0; i < holes.length; i++) {
                if (!passos[i] && holes[orig][i] < 1001) {
                    int c = holes[orig][i];
                    
                    achaCaminho(i, dest, holes, custo + c, custoMax, passos);
                }
            }

        }
        passos[orig] = false;

    }

}

