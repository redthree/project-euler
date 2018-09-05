public class Euler{

	public static void main(String[] args) {

		//VARIABLES
		// long x = 50; //de prueba
		long x = 600851475143L;
		long cx;
		long max = 0;
		long resultado = 0;

		//Comienza proceso con el primer numero primero
		for (long i=2; i<x;) {
			if(x%i==0){
				while(x%i==0){
					x = x/i;
				}
			}
			do{
				i++;
			}while(!Primo(i));

			max = i;
		}
		System.out.println(max);
	}//fin main

	//Evalua si es primo
	public static boolean Primo(long x){
		boolean respuesta = true;
		
		for (long i=2; i<x ; i++) {
			if(x%i==0){
				respuesta = false;
				break;
			}
		}
		return respuesta;
	}//fin Primo
}