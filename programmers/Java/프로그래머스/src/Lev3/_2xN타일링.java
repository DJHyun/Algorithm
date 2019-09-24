//www.programmers.co.kr
package Lev3;

class _2xN≈∏¿œ∏µ {
	public static int solution(int n) {
		int index = 2;
		int left = 1;
		int right = 2;
		int answer = 0;

		if (n == 1) {
			answer = 1;
		} else if (n == 2) {
			answer = 2;
		}

		while (index < n) {
			answer = (int) ((left + right) % 1000000007);
			left = right;
			right = answer;
			index++;
		}

		return answer;
	}

	public static void main(String[] args) {
		for (int i = 1; i <= 100; ++i) {
			solution(i);
		}
	}
}
