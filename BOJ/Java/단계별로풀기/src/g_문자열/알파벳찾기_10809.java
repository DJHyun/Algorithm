//baekjoon source = "https://www.acmicpc.net/problem/10809"
package g_문자열;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;

public class 알파벳찾기_10809 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		String s = br.readLine();
		int[] arr = new int[26];
		Arrays.fill(arr, -1);
		for(int i = 0; i<s.length(); i++) {
			char check = s.charAt(i);
			int c = (int)check-97;
			
			if(arr[c] == -1) arr[c] = i;
		}
		
		for(int i : arr) {
			bw.write(Integer.toString(i)+" ");
		}
		bw.flush();
	}
}
