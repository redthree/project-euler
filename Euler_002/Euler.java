public class Euler{

	public static void main(String[] args) {
		
		int suma = 0;
		int a = 0;
		int b = 1;
		int temp = 0;

		for (int i=0; i < 4000000; i++ ) {
			temp = a;
			a = b;
			if(a<4000000){
				b = temp + b;
			}
			
			if(b%2==0){
				suma = suma + b;
			}
		}
		
		System.out.println(suma);
	
	}//fin main
}