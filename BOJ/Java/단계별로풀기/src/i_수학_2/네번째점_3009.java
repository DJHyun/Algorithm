//baekjoon source = "https://www.acmicpc.net/problem/3009"
package i_수학_2;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class 네번째점_3009 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		Map<Integer, Integer> a = new HashMap<>();
		Map<Integer, Integer> b = new HashMap<>();

		for (int i = 0; i < 3; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int x = Integer.parseInt(st.nextToken()), y = Integer.parseInt(st.nextToken());

			if (!a.containsKey(x)) {
				a.put(x, 1);
			} else {
				a.remove(x);
			}

			if (!b.containsKey(y)) {
				b.put(y, 1);
			} else {
				b.remove(y);
			}
		}

		bw.write(a.keySet().toArray()[0] + " " + b.keySet().toArray()[0]);
		bw.flush();
	}
}
