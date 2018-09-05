public class Euler{

	public static void main(String[] args) {
		
		int producto = 0;
		int max = 0;
		int resultado = 0;

		for (int i=100; i<=999 ; i++) {
			for (int j=100; j<=999 ; j++) {
				producto = i*j;
				if(reves(producto)==producto && producto>max){
					max = producto;
				}
			}
		}

		System.out.println(reves(producto));
		System.out.println(producto);
		System.out.println(max);

	}//fin main

	//Da vuelta el numero
	public static int reves(int numero){
		int copia_numero = numero;
		int numero_r = 0;

		while(copia_numero>0){
			numero_r = numero_r*10 + copia_numero%10;
			copia_numero = copia_numero/10;
		}

		return numero_r;
	}
}
