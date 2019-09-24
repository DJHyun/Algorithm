//www.programmers.co.kr
package Lev3;

public class 타일장식물 {
	public static long solution(int N) {
		long answer = 4;
		long left = 1;
		long right = 1;
		int index = 2;
		
		
		while (index < N) {
			long number = left + right;
			left = right;
			right = number;
			index++;
		}
		if (N != 1) {
			answer = 2*(left+right)+2*right;			
		}
		System.out.println(N+" "+answer);
		return answer;
	}

	public static void main(String[] args) {
		for (int i = 1; i <= 80; ++i) {
			solution(i);
		}
	}
}
