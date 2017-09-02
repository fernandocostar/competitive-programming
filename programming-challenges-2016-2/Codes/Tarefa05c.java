/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */


import java.util.Scanner;
import java.util.*;

/**
 *
 * @author Fernando
 */
public class Tarefa05c {

    public static void main(String[] args) {
        Scanner tec = new Scanner(System.in);
        int n = tec.nextInt();

        for (int i = 0; i < n; i++) {
            String s = tec.next();
            String[] palavra;
            palavra = s.split("");
           
            anagramas(palavra);

        }
    }

    private static void anagramas(String[] palavra) {
        boolean[] visitas = new boolean[palavra.length];
        String[] resp = new String[palavra.length];
        Arrays.sort(palavra, String.CASE_INSENSITIVE_ORDER);
        List<String> dicionario = new ArrayList<>();
        for (int i = 0; i < resp.length; i++) {
            anagramas(palavra, visitas, resp, i, 0, dicionario);
        }
        
        for (int i = 0; i < dicionario.size(); i++) {
            System.out.println(dicionario.get(i));
            
        }

    }

    private static void anagramas(String[] palavra, boolean[] visitas, String[] resp, int letra, int contador, List<String> dicionario) {
        resp[contador] = palavra[letra];
        visitas[letra] = true;

        if (contador == resp.length - 1) {
            String s = junta(resp);

            if (!dicionario.contains(s)) {
                dicionario.add(s);
           
            }

        } else {
            for (int i = 0; i < palavra.length; i++) {
                if (!visitas[i]) {
                    anagramas(palavra, visitas, resp, i, contador + 1, dicionario);
                }
            }
        }
        visitas[letra] = false;
    }

    private static String junta(String[] palavra) {
        String retorno = "";
        for (int i = 0; i < palavra.length; i++) {
            retorno+=palavra[i];
            
        }
        return retorno;
    }
}
