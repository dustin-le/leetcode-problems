import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.junit.Test;
import org.junit.Assert;

/** 
 * LeetCode #49: Group Anagrams
 * Given an array of strings strs, group the anagrams together. You can return the answer in any order.
 * An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
 */
public class groupAnagrams {
    public List<List<String>> groupAnagram(String[] strs) {
        List<List<String>> ans = new ArrayList<>();
        Map<String, Integer> values = new HashMap<String,Integer>();

        for (String s : strs) {
            int charValue = 0;
            for (char c : s.toCharArray()) {
                charValue += (int) c;
            }
            id
            
            values.put(s, charValue);
        }
        
    }

    @Test
    public void test1() {
        String[] strs = {"eat", "tea", "tan", "ate","nat","bat"};
        groupAnagram(strs);
    }

}
