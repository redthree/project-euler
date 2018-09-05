public class Euler{
	public static void main(String[] args) {

		int num = 1;

		while(division(num)!=true){
			num++;
		}

		System.out.println(num);

	}

	//
	public static boolean division(int x){
		boolean respuesta = true;

		for (int i=1; i<21; i++) {
			if(x%i!=0){
				respuesta = false;
				break;
			}
		}

		return respuesta;
	}
}