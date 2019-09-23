//baekjoon source = "https://www.acmicpc.net/problem/1110"
package d_while문;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class 더하기사이클_1110 {
	static String sum(String[] numbers) {
		int sum_ = 0;
		for (String i : numbers) {
			sum_ += Integer.parseInt(i);
		}
		if (Integer.toString(sum_).length() == 2) {
			sum_ = Integer.toString(sum_).charAt(1) - '0';
		}
		return Integer.toString(sum_);
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String n = br.readLine();
		String[] number = new String[2];
		int cnt = 0;
		
		if (n.length() == 1) {
			number[0] = "0";
			number[1] = Character.toString(n.charAt(0));
		} else {
			number[0] = Character.toString(n.charAt(0));
			number[1] = Character.toString(n.charAt(1));
		}
		
		while (true) {
			String check = sum(number);
			number[0] = number[1];
			number[1] = check;
			cnt += 1;
			check = "";
			for(String i : number) {
				check += i;
			}
			if (Integer.parseInt(check) == Integer.parseInt(n)) {
				break;
			}
		}
		System.out.println(cnt);
	}
}
