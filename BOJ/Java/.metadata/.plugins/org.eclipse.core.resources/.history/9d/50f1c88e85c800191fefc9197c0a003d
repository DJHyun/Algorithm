
//baekjoon source = "https://www.acmicpc.net/problem/2578"

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class _2578_ºù°í {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int[][] arr = new int[5][5];
		int[][] check = new int[5][5];
		StringTokenizer st;
		int result = 0;

		for (int i = 0; i < 5; ++i) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < 5; ++j) {
				arr[i][j] = Integer.parseInt(st.nextToken());
			}
		}

		for (int i = 0; i < 5; ++i) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < 5; ++j) {
				int a = Integer.parseInt(st.nextToken());
				System.out.println(a+" ");
				boolean flag = true;
				for (int p = 0; p < 5; ++p) {
					if (flag) {
						for (int q = 0; q < 5; ++q) {
							if (arr[p][q] == a) {
								arr[p][q] = -1;
								result++;
								flag = false;
							}
						}
					} else {
						break;
					}
				}

				if (i >= 2) {
					int sum = 0;
					boolean ch = true;
					for (int x = 0; x < 5; ++x) {
						if (ch) {
							for (int y = 0; y < 5; ++y) {
								if (arr[x][y] != -1) {
									break;
								}
								if (y == 4)
									sum++;
							}
							
							if (sum >= 3) {
								ch = false;
								break;
							}
							
							for (int y = 0; y < 5; ++y) {
								if (arr[y][x] != -1) {
									break;
								}
								if (y == 4)
									sum++;
							}
							
							if (sum >= 3) {
								ch = false;
								break;
							}
						}else {
							break;
						}
					}
					
					if (sum <= 2) {
						ch = true;
						for(int x = 0; x <5; ++x) {
							if (arr[x][x] != -1) {
								break;
							}
							if (x == 4) sum++;
							
							if (sum >= 3)
								break;
						}
						
						for(int x = 0; x<5; ++x) {
							if (arr[x][4-x] != -1)break;
							if (x == 4) sum++;
							if (sum >= 3) break;
						}
					}
					System.out.println("asdfsadf"+sum);
					if (sum >= 3) break;
				}
			}
		}
		bw.write(result+"");
		bw.flush();
	}
}
