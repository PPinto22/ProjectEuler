import java.util.*;

public class Problem3 {

	//private static long TARGET = 600851475143;

	private static boolean isPrime(int num){
		int i;
		for( i = num-1 ; i >= 2; i--){
			if( num % i == 0 ) return false;
		}
		return true;
	}

	public static void main(String[] args){
		for(int i = 1; i < 1000; i++){
			if(isPrime(i)){
				System.out.println(i + " e primo");
			}
		}
	}
}