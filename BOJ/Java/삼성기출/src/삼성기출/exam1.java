package »ï¼º±âÃâ;

import java.util.Arrays;
import java.util.Deque;
import java.util.LinkedList;
import java.util.Scanner;
import java.util.Stack;
import java.util.StringTokenizer;

class exam1 {

	static int n;
	static int[] number;
	static int[] asc;
	static int[] desc;
	static int result = 10;

	static boolean check(int[] arr) {
		if (Arrays.toString(arr).equals(Arrays.toString(asc))
				|| Arrays.toString(arr).equals(Arrays.toString(desc))) {
			return true;
		}
		return false;
	}

	static void sol(int[] arr, int cnt) {

		if (cnt >= 5) {
			return;
		}

		for (int i = 0; i < n; ++i) {
			Stack<Integer> a = new Stack<>();
			Stack<Integer> b = new Stack<>();

			for (int id = 0; id < n; ++id) {
				if (id < n / 2) {
					a.add(arr[id]);
				} else {
					b.add(arr[id]);
				}
			}
			
			int index = 0;
			for (int j = i; j > 0; --j) {
				if (a.size()-j > 0) {
					a.add(a.size()-j , b.remove(0));
				} else {
					a.add(index, b.remove(0));
					index++;
				}
				
				if(b.isEmpty()) break;
			}

			while (!b.isEmpty()) {
				a.addAll(b);
				b.clear();
			}
			
			int [] c = new int [n];
			for(int re = 0; re<n; ++re) {
				c[re] = a.get(re);
			}
			System.out.println(Arrays.toString(c));
			
			if(check(c)) {
				result = Math.min(result, cnt);
				return;
			}
			
			if (!Arrays.toString(c).equals(Arrays.toString(number))) {
				sol(c,cnt+1);
			}
		}
	}

	public static void main(String args[]) throws Exception {
		System.setIn(new java.io.FileInputStream("sample_input1.txt"));

		Scanner sc = new Scanner(System.in);

		int T = sc.nextInt();
		for (int test_case = 1; test_case <= T; test_case++) {
			n = sc.nextInt();
			number = new int[n];
			sc.nextLine();
			StringTokenizer st = new StringTokenizer(sc.nextLine());
			asc = new int[n];
			desc = new int[n];
			for (int i = 1; i <= n; ++i) {
				asc[i - 1] = i;
				desc[i - 1] = n - i + 1;
			}

			for (int i = 0; i < n; ++i) {
				number[i] = Integer.parseInt(st.nextToken());
			}
			System.out.println("asc" + Arrays.toString(asc));
			System.out.println("desc" + Arrays.toString(desc));
			System.out.println("number" + Arrays.toString(number));

			if (check(number)) {
				System.out.println("#" + test_case + " " + 0);
			} else {
				sol(number, 1);
				System.out.println("#" + test_case + " " + result);
			}

		}

		sc.close(); //
	}
}
