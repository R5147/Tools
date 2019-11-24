import java.util.Arrays;

public class Test {
	public static void main(String[] args) {
		String string = "Helllo worlllllld";
		String find = "l";
		String replace_text = "p";
		int sequence = 1;
		
		System.out.println(string_replace(string, find, replace_text, sequence));  // Hepllo worlllllld
		
		sequence = 4;
		System.out.println(string_replace(string, find, replace_text, sequence));  // Hepppo worpllllld
		
		sequence = -1;
		find = "lll";
		replace_text = "a";
		System.out.println(string_replace(string, find, replace_text, sequence));  // Heao woraad
	}
	
	public static String string_replace(String old_string, String search_string, String replace_string, int replacement) {
		if(search_string.length() > old_string.length()) {
			return old_string;
		}
		
		String result_string = old_string;
		int[] replace_points = substring_count(old_string, search_string);
		
		if(replacement < 0 || replacement >= replace_points.length) {
			for(int i = 0; i < replace_points.length; i++) {
				result_string = result_string.substring(0, replace_points[i] + (replace_string.length() - search_string.length()) * i) + replace_string + result_string.substring(replace_points[i] + (replace_string.length() - search_string.length()) * i + search_string.length(), result_string.length());
			}
		}
		else if(replacement > 0) {
			for(int i = 0; i < replacement; i++) {
				result_string = result_string.substring(0, replace_points[i] + (replace_string.length() - search_string.length()) * i) + replace_string + result_string.substring(replace_points[i] + (replace_string.length() - search_string.length()) * i + search_string.length(), result_string.length());
			}
		}
		
		return result_string;
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
