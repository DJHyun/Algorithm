//baekjoon source = "https://www.acmicpc.net/problem/1085"
package i_수학_2;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class 직사각형에서탈출_1085 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		StringTokenizer st = new StringTokenizer(br.readLine());
		int x = Integer.parseInt(st.nextToken()), y = Integer.parseInt(st.nextToken()),
				w = Integer.parseInt(st.nextToken()), h = Integer.parseInt(st.nextToken());
		double result = Math.min(x, y);
		
		result = Math.min(result, Math.abs(x-w));
		result = Math.min(result, Math.abs(y-h));
		result = Math.min(result, Math.sqrt((Math.pow(Math.abs(x - w), 2) + Math.pow(Math.abs(y - h), 2))));
		result = Math.min(result, Math.sqrt((Math.pow(x, 2) + Math.pow(y, 2))));
		
		bw.write((int)result+"\n");
		bw.flush();
	}
}
