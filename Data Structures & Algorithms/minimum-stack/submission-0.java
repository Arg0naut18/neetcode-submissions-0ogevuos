class MinStack {
    Stack<Integer> minStack;
    Stack<Integer> st;
    
    public MinStack() {
        minStack = new Stack<>();
        st = new Stack<>();
    }
    
    public void push(int val) {
        st.push(val);
        if(minStack.isEmpty() || minStack.peek()>=val) {
            minStack.push(val);
        }
    }
    
    public void pop() {
        int val = st.pop();
        if(minStack.peek()==val) {
            minStack.pop();
        }
    }
    
    public int top() {
        return st.peek();
    }
    
    public int getMin() {
        return minStack.peek();
    }
}
