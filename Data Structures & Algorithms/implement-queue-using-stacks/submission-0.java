/*
s1 = source of truth real stack
s2 = front of queue (make sure not empty) 

s1 = []

s2 = [8, 7, 6]
*/

class MyQueue {

    private Deque<Integer> s1;
    private Deque<Integer> s2;

    public MyQueue() {
        this.s1 = new ArrayDeque<>();
        this.s2 = new ArrayDeque<>();
    }
    
    public void push(int x) {
        s1.push(x);
    }

    private void flush(){
        while (!s1.isEmpty()){
            s2.push(s1.pop());
        }
    }
    
    public int pop() {
        //flush logic
        if (s2.isEmpty()) {
            flush();
        }

        return s2.pop();

    }
    
    public int peek() {
        //flush logic
        if (s2.isEmpty()) {
            flush();
        }
        return s2.peek();
    }
    
    public boolean empty() {
        return s1.isEmpty() && s2.isEmpty();
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */