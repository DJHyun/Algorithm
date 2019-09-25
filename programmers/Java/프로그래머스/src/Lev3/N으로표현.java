//source = www.programmers.co.kr
package Lev3;

public class N으로표현 {
	static int answer;
	
	public static void dfs(int n, int number, int depth, int result) {
		if (depth > 8) {
			return;
		}
		
		if (answer != -1 && answer < depth) {
			return;
		}
		
		if (number == result) {
			answer = depth;
			return;
		}
		
		int new_n = n;
		
		for(int i = 0; i<8-depth; ++i) {
			dfs(n,number,depth+i+1,result+new_n);
			dfs(n,number,depth+i+1,result-new_n);
			dfs(n,number,depth+i+1,result*new_n);
			dfs(n,number,depth+i+1,result/new_n);
			
			new_n = new_n*10+new_n;
		}
	}
	
	
	public static int solution(int N, int number) {
		answer = -1;
		dfs(N,number,0,0);
		System.out.println(answer);
		return answer;
	}
	
	public static void main(String[] args) {
		solution(2,11);
	}
}
