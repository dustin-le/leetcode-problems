import java.util.Arrays;
import java.util.Random;

import org.junit.Assert;
import org.junit.Test;

public class insertionSort {
    public static int[] doTheThing(int[] arr) {
        for ( int i = 1; i < arr.length; i++ ) {
            int valueToInsert = arr[i];
            int insertIndex = i;

            while ( insertIndex > 0 && arr[insertIndex - 1] > valueToInsert ) {
                arr[insertIndex] = arr[insertIndex - 1];
                insertIndex -= 1;
            }

            arr[insertIndex] = valueToInsert;
        }

        return arr;
    }

    public static void main(String[] args) {
        int[] arg = new Random().ints(100, 0, 100).toArray();
        System.out.println(Arrays.toString(arg));
        System.out.println(Arrays.toString(doTheThing(arg)));
    }

    @Test
    public void test1() {
        int[] arg = {2, 0, 1, 3, 2, 1, 1, 0, 4};
        Assert.assertEquals("[0, 0, 1, 1, 1, 2, 2, 3, 4]", Arrays.toString(doTheThing(arg)));
    }

    @Test
    public void test2() {
        int[] arg = {12, 4, 3, 13, 3, 8, 15, 14, 11, 1, 0, 1, 15, 15, 2};
        Assert.assertEquals("[0, 1, 1, 2, 3, 3, 4, 8, 11, 12, 13, 14, 15, 15, 15]", Arrays.toString(doTheThing(arg)));
    }

    @Test
    public void test3() {
        int[] arg = {76, 41, 14, 83, 9, 91, 99, 56, 25, 74, 24, 85, 35, 69, 76, 62, 48, 21, 46, 56, 11, 91, 18, 23, 55, 29, 49, 67, 75, 57, 22, 1, 87, 3, 24, 49, 45, 46, 33, 74, 35, 19, 73, 88, 37, 99, 67, 82, 20, 71, 53, 88, 64, 25, 84, 77, 14, 32, 23, 23, 14, 84, 32, 43, 65, 13, 49, 85, 12, 48, 30, 60, 37, 61, 17, 18, 38, 92, 26, 71, 24, 18, 72, 85, 86, 51, 53, 45, 83, 94, 70, 92, 51, 72, 0, 73, 53, 3, 56, 51};
        Assert.assertEquals("[0, 1, 3, 3, 9, 11, 12, 13, 14, 14, 14, 17, 18, 18, 18, 19, 20, 21, 22, 23, 23, 23, 24, 24, 24, 25, 25, 26, 29, 30, 32, 32, 33, 35, 35, 37, 37, 38, 41, 43, 45, 45, 46, 46, 48, 48, 49, 49, 49, 51, 51, 51, 53, 53, 53, 55, 56, 56, 56, 57, 60, 61, 62, 64, 65, 67, 67, 69, 70, 71, 71, 72, 72, 73, 73, 74, 74, 75, 76, 76, 77, 82, 83, 83, 84, 84, 85, 85, 85, 86, 87, 88, 88, 91, 91, 92, 92, 94, 99, 99]", Arrays.toString(doTheThing(arg)));
    }
}