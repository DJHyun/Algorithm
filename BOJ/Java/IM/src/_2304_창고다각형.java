
//baekjoon source = "https://www.acmicpc.net/problem/2304"

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;

public class _2304_창고다각형 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int n = Integer.parseInt(br.readLine());
		int[] arr = new int[1001];
		StringTokenizer st;

		int max = 0, index = 0, result = 0, end = 0;
		for (int i = 0; i < n; ++i) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken()), b = Integer.parseInt(st.nextToken());
			arr[a] = b;
			if (max < b) {
				max = b;
				index = a;
			}
			end = Math.max(a, end);
		}
		int check = 0, check_index = 0;
		for (int i = 0; i <= index; ++i) {
			if (check <= arr[i]) {
				result += (i - check_index) * check;
				check = arr[i];
				check_index = i;

			}
		}
		check = 0;
		check_index = end;
		for (int i = end; i >= index; --i) {
			if (check <= arr[i]) {
				result += (check_index - i) * check;
				check = arr[i];
				check_index = i;
			}
		}
		
		bw.write(result+max+"");
		bw.flush();
	}
}
