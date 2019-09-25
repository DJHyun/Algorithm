import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

class Main {
	static int n;
	static String[][] arr;
	static int m;

	public static void solution(boolean flag, int count, int num) {
		int index = 0;
		while (index < count) {
			if (flag) {

				String one = arr[num][num];
				for (int i = num; i < n - num - 1; ++i) {
					arr[num][i] = arr[num][i+1];
				}
				
				for(int i = num; i<n-num-1; ++i) {
					arr[i][n-num-1] = arr[i+1][n-num-1];
				}
				
				for(int i = n-num-1; i>num; --i) {
					arr[n-num-1][i] = arr[n-num-1][i-1];
				}
				
				for(int i = n-num-1; i>num; --i) {
					arr[i][num] = arr[i-1][num];
				}
				
				arr[num+1][num] = one;

			} else {
				String one = arr[num][n - num - 1];

				for (int i = n - num - 1; i > num; --i) {
					arr[num][i] = arr[num][i - 1];
				}

				for (int i = num; i < n - num - 1; ++i) {
					arr[i][num] = arr[i + 1][num];
				}

				for (int i = num; i < n - num - 1; ++i) {
					arr[n - num - 1][i] = arr[n - num - 1][i + 1];
				}

				for (int i = n - num - 1; i > num; --i) {
					arr[i][n - num - 1] = arr[i - 1][n - num - 1];
				}
				arr[num + 1][n - num - 1] = one;

			}
			index++;
		}
	}

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		arr = new String[n][n];
		for (int i = 0; i < n; ++i) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < n; ++j) {
				arr[i][j] = st.nextToken();
			}
		}

		int index = n;
		boolean flag = m > 0 ? false : true;
		int z = 0;
		while (index > 1) {
			int number = Math.abs(m % (4 * (index - 1)));
			solution(flag, number, z);
			flag = !flag;
			index -= 2;
			z += 1;
		}

		for (String[] ss : arr) {
			bw.write(Arrays.toString(ss).replace("[", "").replace("]", "").replace(",", "") + '\n');
		}
		bw.flush();
	}
}
