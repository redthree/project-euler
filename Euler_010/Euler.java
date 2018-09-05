public class Euler {

	public static void main(String[] args) {

		long suma = 0;

		for (int i = 2; i < 2000000; i++) {
			if(esPrimo(i)){
				suma = suma + i;
			}
		}
		
		System.out.println(suma);
	}

	public static boolean esPrimo(int n) {
		boolean esPrimo = true;

		for (int i=2; i<= Math.round(Math.sqrt(n)) && esPrimo; i++) {
			esPrimo = !(n % i == 0);
		}

		return esPrimo;
	}
}