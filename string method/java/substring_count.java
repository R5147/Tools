import java.util.Arrays;

public class Test {
	public static void main(String[] args) {
		String string = "Hello world!";
		String find = "l";
		
		System.out.println(substring_count(string, find).length);
		System.out.println(Arrays.toString(substring_count(string, find)));
		
		find = "ll";
		System.out.println(substring_count(string, find).length);
		System.out.println(Arrays.toString(substring_count(string, find)));
		
	}
	
	public static int[] substring_count(String old_string, String search_string) {
		int[] result = {};
		
		if(search_string.length() > old_string.length()) {
			return result;
		}
		
		for(int i = 0; i < old_string.length() - search_string.length() + 1; i++) {
			if(old_string.substring(i, i + search_string.length()).equals(search_string)) {
				if(result.length == 0) {
					result = Arrays.copyOf(result, result.length + 1);
					result[result.length - 1] = i;
				}
				else if(i > result[result.length - 1] + search_string.length() - 1) {
					result = Arrays.copyOf(result, result.length + 1);
					result[result.length - 1] = i;
				}
			}
		}
		
		return result;
	}
}
