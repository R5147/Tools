public class Test{
	public static void main(String[] args){
		System.out.println(repeat("0", 0));  //
		System.out.println(repeat("0", 1));  // 0
		System.out.println(repeat("0", 3));  // 000
		System.out.println(repeat("00", 3));  // 000000
	}
	
	public static String repeat(String s, int n) {
		if(n <= 0) {
			return "";
		}
		String result = s;
		for(int i = 0; i < n - 1; i++) {
			result += s;
		}
		return result;
	}
}
