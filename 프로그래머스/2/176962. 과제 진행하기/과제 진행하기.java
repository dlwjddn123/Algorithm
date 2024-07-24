import java.util.*;

class Solution {
    
    public class Plan {
        String name;
        int time;
        int requestTime;
        
        public Plan(String name, int time, int requestTime) {
            this.name = name;
            this.time = time;
            this.requestTime = requestTime;
        }
    }
    
    public String[] solution(String[][] plans) {
        List<String> answer = new ArrayList<>();
        List<Plan> myPlans = new ArrayList<>();
        Stack<Plan> inProgressTasks = new Stack<>();
        
        for (String[] plan : plans) {
            myPlans.add(new Plan(plan[0], Integer.parseInt(plan[1].substring(0, 2)) * 60 + Integer.parseInt(plan[1].substring(3)), Integer.parseInt(plan[2])));    
        }
        
        Collections.sort(myPlans, (p1, p2) -> {
            return p1.time - p2.time;
        });
        
        int currentTime = 0;
        
        for (Plan plan : myPlans) {
            if (inProgressTasks.isEmpty()) {
                inProgressTasks.add(plan);
                currentTime = plan.time;
                continue;
            }
            
            while (!inProgressTasks.isEmpty()) {
                Plan inProgressTask = inProgressTasks.peek();
                if (currentTime + inProgressTask.requestTime <= plan.time) {
                    currentTime += inProgressTask.requestTime;
                    answer.add(inProgressTasks.pop().name);
                    continue;
                } 
                inProgressTask.requestTime -= plan.time - currentTime;
                currentTime += plan.time - currentTime; 
                break;
            }
            currentTime = (inProgressTasks.isEmpty()) ? plan.time : currentTime + plan.time - currentTime; 
            inProgressTasks.add(plan);
        }
        
        while (!inProgressTasks.isEmpty()) {
            answer.add(inProgressTasks.pop().name);
        }       

        return answer.toArray(new String[answer.size()]);
    }
}