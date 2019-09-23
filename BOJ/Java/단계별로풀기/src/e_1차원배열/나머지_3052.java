//baekjoon source = "https://www.acmicpc.net/problem/3052"
package e_1차원배열;

import java.util.HashMap;
import java.util.Scanner;

public class 나머지_3052 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		HashMap<Integer, Integer> dic = new HashMap<>();

		for (int i = 0; i < 10; i++) {
			int number = sc.nextInt() % 42;
			dic.put(number, 1);
		}
		
		System.out.println(dic.size());
	}
}
