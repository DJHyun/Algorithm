//source = www.programmers.co.kr
package Lev3;

public class _4¥‹∞Ì¿Ω {
	static int answer = 0;

//	public static void solve(int n, int check, int three, int one, int count) {
//		System.out.printf("%d %d %d %d %d%n", n, check, three, one, count);
//
//		if (n == check) {
//			if (one == three * 2) {
//				answer++;
//				return;
//			}
//			return;
//		}
//
//		if (check * 3 <= n) {
//			solve(n, check * 3, three + 1, one, count+2);
//		}
//
//		if (count > 0 && check + 1 <= n) {
//			solve(n, check + 1, three, one + 1, count -1);
//		}
//
//	}
	public static void solve(int n, int count) {

		if(Math.pow(3, count/2)>n) return;
		
		if (n < 3)
			return;
		
		if (n == 3) {
			if (count == 2) {
				answer++;
				return;
			}
			return;
		}
		if (n % 3 == 0 && count >= 2) {
			solve(n / 3, count - 2);
		}
		solve(n - 1, count + 1);
		
		
	}

	public static int solution(int n) {
		answer = 0;
		solve(n, 0);
		System.out.println(n + " result " + answer);
		return answer;
	}

	public static void main(String[] args) {
		for (int i = 5; i <= 100000; ++i) {
			solution(i);
		}
	}
}
