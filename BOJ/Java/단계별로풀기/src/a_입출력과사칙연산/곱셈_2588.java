//baekjoon source = "https://www.acmicpc.net/problem/2588"
package a_ÀÔÃâ·Â°ú»çÄ¢¿¬»ê;

import java.util.Scanner;


public class °ö¼À_2588 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String a = sc.next();
		String b = sc.next();
		int result = 0;
		int realResult = 0;
		int idx = 0;
		int realIdx = 0;
		
		
		for (int i = b.length() - 1; i > -1; i--) {
			result = 0;
			idx = 0;
			for (int j = a.length() - 1; j > -1; j--) {
				result += ((a.charAt(j) - '0') * (b.charAt(i) - '0'))*Math.pow(10, idx);
				idx++;
			}
			System.out.println(result);
			realResult += result*Math.pow(10, realIdx);
			realIdx += 1;
			
		}
		System.out.println(realResult);
	}
}
