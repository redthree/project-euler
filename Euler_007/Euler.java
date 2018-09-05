public class Euler{

	public static void main(String[] args) {

		int num = 0;
		int cont = 0;

		for (int i = 2; i>0 ; i++) {
			if(Primo(i)==true){
				num = i;
				cont++;
				if(cont==10001){
					break;
				}
			}
		}

		System.out.println(num);
	}

	//Es primo
	public static boolean Primo(int x){

		boolean respuesta = true;
		
		for (int i=2; i<x ; i++) {
			if(x%i==0){
				respuesta = false;
				break;
			}
		}

		return respuesta;
	}

}