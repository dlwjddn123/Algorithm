class Solution {
    public int[] solution(String[] wallpaper) {
        int[] answer = {};
        int u = 0;
        boolean flag = false;
        
        for (int i = 0; i < wallpaper.length; i++) {
            for (int j = 0; j < wallpaper[i].length(); j++) {
                if (wallpaper[i].charAt(j) == '#') {
                    u = i;
                    System.out.println(i + " " + j);
                    flag = true;
                    break;
                }
            }
            if (flag) {
                flag = false;
                break;
            }
        }
        int d = 0;
        for (int i = wallpaper.length - 1; i > 0; i--) {
            for (int j = 0; j < wallpaper[i].length(); j++) {
                if (wallpaper[i].charAt(j) == '#') {
                    d = i;
                    flag = true;
                    break;
                }
            }
            if (flag) {
                flag = false;
                break;
            }
        }
        int l = 0;
        for (int i = 0; i < wallpaper[0].length(); i++) {
            for (int j = 0; j < wallpaper.length; j++) {
                if (wallpaper[j].charAt(i) == '#') {
                    l = i;
                    flag = true;
                    break;
                }
            }
            if (flag) {
                flag = false;
                break;
            }
        }

        int r = 0;
        for (int i = wallpaper[0].length() - 1; i > 0; i--) {
            for (int j = 0; j < wallpaper.length; j++) {
                if (wallpaper[j].charAt(i) == '#') {
                    r = i;
                    flag = true;
                    break;
                }
            }
            if (flag) {
                flag = false;
                break;
            }
        }
        answer = new int[]{u, l, d+1, r+1};
        return answer;
    }
}