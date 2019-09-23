//baekjoon source = "https://www.acmicpc.net/problem/15596"
package f_함수;

public class 정수N개의합_15596 {
	long sum(int[] a) {
		long result = 0;
		for (int i = 0; i < a.length; i++) {
			result += a[i];
		}
		return result;
	}
}
