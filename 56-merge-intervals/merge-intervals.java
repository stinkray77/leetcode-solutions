class Solution {
    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> a[0] - b[0]); // sort the arrays

        ArrayList<int[]> output = new ArrayList<>();
        int i = 0;
        while (i < intervals.length) {
            int start = intervals[i][0];
            int end = intervals[i][1];
            while (i + 1 < intervals.length && end >= intervals[i+1][0]) {
                i++;
                end = Math.max(end, intervals[i][1]);
            }
            output.add(new int[]{start, end});
            i++;
        }

        return output.toArray(new int[0][]);
    }
}