public class Euler {

	public static void main(String[] args) {

		double k = 0, suma = 0;

		for (int i = 3; i < 1000; i++) {
			for (int j = 2; j < 1000; j++) {
				k = (Math.pow(i, 2)) + (Math.pow(j, 2));
				
				if (i < j && j < k && Math.sqrt(k)%1==0) {
					suma = i + j + Math.sqrt(k);
					if(suma == 1000){
						System.out.println("\nA: " + i);
						System.out.println("B: " + j);
						System.out.println("C: " + Math.sqrt(k));
						System.out.println("Producto: " + i*j*(int)(Math.sqrt(k)));
					}
				}
			}
		}

	}// fin main

}
