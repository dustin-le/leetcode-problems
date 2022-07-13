import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import org.junit.Assert;
import org.junit.Test;

/** 
 * LeetCode #56: Merge Intervals (https://leetcode.com/problems/merge-intervals/)
 * Given an array of intervals where intervals[i] = [starti, endi], 
 * merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
 */

public class mergeIntervals {
    public static int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, (i1, i2) -> Integer.compare(i1[0], i2[0]));
        List<int[]> ans = new ArrayList<>();

        if ( intervals.length == 1 ) {
            return intervals;
        }
        
        for ( int i = 0; i < intervals.length - 1; i++ ) {
            if ( intervals[i][1] >= intervals[i+1][0] ) {
                intervals[i+1][0] = Math.min(intervals[i][0], intervals[i+1][0]);
                intervals[i+1][1] = Math.max(intervals[i][1], intervals[i+1][1]);
            }
            else {
                ans.add(intervals[i]);
            }
            if ( i == intervals.length - 2 ) {
                ans.add(intervals[i+1]);
            }
        }
        return ans.toArray(new int[ans.size()][]);
    }

    public static void main(String[] args) {

    }

    @Test
    public void test1() {
        int[][] arg = { {1,3}, {2,6}, {8,10}, {15,18} };
        Assert.assertEquals("[[1, 6], [8, 10], [15, 18]]", Arrays.deepToString(merge(arg)));
    }

    @Test
    public void test2() {
        int[][] arg = { {1,4}, {0,4} };
        Assert.assertEquals("[[0, 4]]", Arrays.deepToString(merge(arg)));
    }
    
    @Test
    public void test3() {
        int[][] arg = { {1,4}, {0,1} };
        Assert.assertEquals("[[0, 4]]", Arrays.deepToString(merge(arg)));
    }

    @Test
    public void test4() {
        int[][] arg = { {1,4}, {0,0} };
        Assert.assertEquals("[[0, 0], [1, 4]]", Arrays.deepToString(merge(arg)));
    }

    @Test
    public void test5() {
        int[][] arg = { {2,3}, {4,5}, {6,7}, {8,9}, {1, 10} };
        Assert.assertEquals("[[1, 10]]", Arrays.deepToString(merge(arg)));
    }   
    
    @Test
    public void test6() {
        int[][] arg = { {2,3}, {2,2}, {3,3}, {1,3}, {5,7}, {2,2}, {4,6} };
        Assert.assertEquals("[[1, 3], [4, 7]]", Arrays.deepToString(merge(arg)));
    }

    @Test
    public void test7() {
        int[][] arg = { {1,3} };
        Assert.assertEquals("[[1, 3]]", Arrays.deepToString(merge(arg)));
    }
}
