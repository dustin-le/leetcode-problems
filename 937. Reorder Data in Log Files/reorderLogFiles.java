import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;

import org.junit.Assert;
import org.junit.Test;

/** 
 * LeetCode #937: Reorder Data in Log Files (https://leetcode.com/problems/reorder-data-in-log-files/) 
 * There are two types of logs:
 * Letter-logs: All words (except the identifier) consist of lowercase English letters.
 * Digit-logs: All words (except the identifier) consist of digits.
 * 
 * The letter-logs come before all digit-logs.
 * The letter-logs are sorted lexicographically by their contents. If their contents are the same, then sort them lexicographically by their identifiers.
 * The digit-logs maintain their relative ordering.
 * 
 * After looking at solutions, you can just do all of it in one comparator function.
 */

public class reorderLogFiles {
    public String[] reorderLogs(String[] logs) {
        List<String> digits = new ArrayList<String>();
        List<String> withoutDigitLogs = new ArrayList<String>();

        for ( String s : logs ) { 
            String[] splitted = s.split(" ");
            if (Character.isDigit(splitted[1].toCharArray()[0])) {
                digits.add(s);
            }
            else {
                withoutDigitLogs.add(s);
            }
        }

        Comparator<String> comp = new Comparator<String>() {
            @Override
            public int compare(String s1, String s2) {
                String word1 = s1.substring(s1.indexOf(" ") + 1);
                String word2 = s2.substring(s2.indexOf(" ") + 1);

                if (word1.equals(word2)) {
                    return s1.substring(0, s1.indexOf(' ')).compareTo(s2.substring(0, s2.indexOf(' ')));
                }
                else {
                    return word1.compareTo(word2);
                }
            }
        };

        // Sort the letters using the comparator.
        String[] sortedLetters = new String[withoutDigitLogs.size()];
        sortedLetters = withoutDigitLogs.toArray(sortedLetters);
        Arrays.sort(sortedLetters, comp);

        // To save some space, clear withoutDigitLogs and populate with the sorted letter-logs. Once populated, add the digit-logs at the end.
        withoutDigitLogs.clear(); 
        for ( String s : sortedLetters ) {
            withoutDigitLogs.add(s);
        }
        withoutDigitLogs.addAll(digits);

        String[] answer = new String[withoutDigitLogs.size()];
        answer = withoutDigitLogs.toArray(answer);
        return answer;
    }

    @Test
    public void test1() {
        String[] test = { "dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero" };
        String[] expected = { "let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6" };
        Assert.assertArrayEquals(expected, reorderLogs(test));
    }

    @Test
    public void test2() {
        String[] test = { "a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo" };
        String[] expected = { "g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7" };
        Assert.assertArrayEquals(expected, reorderLogs(test));
    }

    @Test
    public void test3() {
        String[] test = { "a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo","a2 act car" };
        String[] expected = { "a2 act car","g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7" };
        Assert.assertArrayEquals(expected, reorderLogs(test));
    }
}
