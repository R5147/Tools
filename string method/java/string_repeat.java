public class Test{
	public static void main(String[] args){
		System.out.println(repeat("0", 0));  //
		System.out.println(repeat("0", 1));  // 0
		System.out.println(repeat("0", 3));  // 000
	}
	
	public static String repeat(String s, int n) {
		String result = s;
		for(int i = 0; i < n - 1; i++) {
			result += s;
		}
		if(n <= 0) {
			return "";
		}
		return result;
	}
}
