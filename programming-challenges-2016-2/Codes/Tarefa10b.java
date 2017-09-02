import java.util.*;
public class Tarefa10b{

	//public static int produtoEscalar(int[] v1, int[] v2){
	//	return (v1[0]*v2[0])+(v1[1]*v2[1]);
	//}

	public static String estaDentro(int[] p, int[][] poligono){

		int cruzamentos = 0;

		for(int i=0; i<poligono.length-1; i++){
			int[] a = poligono[i];
			int[] b = poligono[i+1];

			int r = ((a[0]-b[0])*(p[1]-b[1]))-((p[0]-b[0])-(a[1]-b[1]));

			//int[][] pa = {{p[0],p[1]},{a[0],a[1]}};
			//int[][] pb = {{p[0],p[1]},{b[0],b[1]}};

			//if(r=0 && produtoEscalar(pa, pb)<=0)
			if(a[1]>b[1]){
				int[] aux = a;
				a = b;
				b = aux;
			}
			if(r>0 && a[1]<p[1] && p[1]<=b[1]) cruzamentos += 1;
		}

		if(cruzamentos%2 == 0) return "nao";
		return "sim";

	}

	public static void main(String[] args){

		Scanner scanner = new Scanner(System.in);

		int qtdPts = scanner.nextInt();
		while(qtdPts != 0){
			int[][] poli = new int[qtdPts][2];

			for(int i=0; i<qtdPts; i++){
				scanner.nextLine();
				poli[i][0] = scanner.nextInt();
				poli[i][1] = scanner.nextInt();
			} 

			scanner.nextLine();
			int px = scanner.nextInt();
			int py = scanner. nextInt();

			int[] pt = {px, py};

			System.out.println(estaDentro(pt, poli));

			scanner.nextLine();
			qtdPts = scanner.nextInt();
		}

	}
} 