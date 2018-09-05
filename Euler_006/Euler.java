public class Euler{
	public static void main(String[] args) {

		int s_cuad = 0;
		int cuad_s = 0;
		
		//Suma de los cuadrados
		for (int i=1 ; i<101 ; i++) {
			s_cuad = s_cuad + i*i;
		}

		//Cuadrado de la suma
		for (int i=1 ; i<101 ; i++) {
			cuad_s = cuad_s + i;
		}
		cuad_s = cuad_s*cuad_s;
		
		System.out.println(cuad_s);
		System.out.println(s_cuad);
		System.out.println(cuad_s - s_cuad);

	}
}