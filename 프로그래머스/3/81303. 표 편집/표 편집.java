import java.util.*;
import java.io.*;

class Solution {
    
    public class Node {
        Node prev;
        Node next;
        int idx;
        boolean isDetached;
        
        public Node(Node prev, int idx) {
            this.prev = prev;
            this.idx = idx;
            this.isDetached = false;
        }
        
        public void detach() {
            this.isDetached = true;
            if (this.next != null && this.prev != null) {
                this.next.setPrev(this.prev);
                this.prev.setNext(this.next);
            } else if(this.next == null) {
                this.prev.setNext(null);
            } else if(this.prev == null) {
                this.next.setPrev(null);
            }
        }
        
        public void restore() {
            this.isDetached = false;
            if (this.next != null && this.prev != null) {
                this.next.setPrev(this);
                this.prev.setNext(this);
            } else if(this.next == null) {
                this.prev.setNext(this);
            } else if(this.prev == null) {
                this.next.setPrev(this);
            }
        }
        
        public void setPrev(Node prev) {
            this.prev = prev;
        }
        
        public void setNext(Node next) {
            this.next = next;
        }
        
        public Node move(int x, String type) {
            Node current = this;
            
            if (type.equals("U")) {
                for (int i = 0; i < x; i++) {
                    current = current.prev;
                }
                return current;
            }
            
            for (int i = 0; i < x; i++) {
                current = current.next;
            }   
            
            return current;
        }
    }
    
    
    public String solution(int n, int k, String[] cmd) {
        StringBuilder answer = new StringBuilder();
        List<Node> nodes = new ArrayList<>();
        
        Node current = new Node(null, 0);
        nodes.add(current);
        Node start = current;
        Node cursor = current;
        for (int i = 1; i < n; i++) {
            current.setNext(new Node(current, i));
            current = current.next;
            nodes.add(current);
            if (i == k) {
                cursor = current;
            }
        }
        
        Stack<Node> stack = new Stack<>();
        
        for (int i = 0; i < cmd.length; i++) {
            String[] command = cmd[i].split(" ");
            if (command[0].equals("U")) {
                cursor = cursor.move(Integer.parseInt(command[1]), "U");
            } else if (command[0].equals("D")) {
                cursor = cursor.move(Integer.parseInt(command[1]), "D");
            } else if (command[0].equals("C")) {
                cursor.detach();
                stack.push(cursor);
                if (cursor.idx == start.idx) {
                    start = cursor.next;
                }
                if (cursor.next == null) {
                    cursor = cursor.prev;
                    continue;
                } 
                cursor = cursor.next;
            } else if (command[0].equals("Z")) {
                Node node = stack.pop();
                if (node.idx == start.idx) {
                    start = node;
                }
                node.restore();
            }
        }
        
        for (Node node : nodes) {
            if (node.isDetached) {
                answer.append("X");
                continue;
            }
            answer.append("O");
        }
        
        return answer.toString();
    }
}