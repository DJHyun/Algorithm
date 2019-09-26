//source = www.programmers.co.kr
package Lev3;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

public class 단속카메라 {
	public static int solution(int[][] routes) {
		int answer = 1;
		
		
		for(int [] i :routes) {
			System.out.println(Arrays.toString(i));
		}
		System.out.println();
		Arrays.sort(routes, new Comparator<int []>() {
			@Override
			public int compare(int[] o1, int[] o2) {
				Integer one = o1[0];
				Integer two = o2[0];
				return one.compareTo(two);
			}
		});
		
		for(int [] i :routes) {
			System.out.println(Arrays.toString(i));
		}
		
		for(int i = 0; i<routes.length-1; ++i) {
			for(int j = i+1; j<routes.length; ++j) {
				if(routes[i][1] < routes[j][0]) {
					answer++;
					break;
				}
			}
		}
		System.out.println(answer);
		return answer;
	}

	public static void main(String[] args) {
		solution(new int[][] { { -20, 15 }, { -14, -5 }, { -18, -13 }, { -5, -3 } });
	}
}
