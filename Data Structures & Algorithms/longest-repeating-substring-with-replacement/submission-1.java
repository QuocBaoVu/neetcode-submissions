class Solution {
    public int characterReplacement(String s, int k) {
        HashMap<Character, Integer> windowMap = new HashMap<>();
        int out = 1;
        int left = 0;
        windowMap.put(s.charAt(0), 1);
        for (int i = 1; i < s.length(); i++) {
            windowMap.put(s.charAt(i), windowMap.getOrDefault(s.charAt(i), 0)+1);
            int windowSize = i - left + 1;
            int most_freq = Collections.max(windowMap.values());
            if (windowSize - most_freq <= k) {
                out = Math.max(out, windowSize);
            } else {
                windowMap.put(s.charAt(left), windowMap.get(s.charAt(left))-1 );
                if (windowMap.get(s.charAt(left)) == 0) {
                    windowMap.remove(s.charAt(left));
                }
                left ++;
            }
        }
        return out;
    }
}
/*
AAABABB
AAAAA
*/