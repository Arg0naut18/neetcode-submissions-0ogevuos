class Solution {
    public boolean isValid(String s) {
        Stack<Character> st = new Stack<>();
        for (char c: s.toCharArray()) {
            if(st.isEmpty()) {
                st.push(c);
                continue;
            }
            char peek = st.peek();
            if((c==')' && peek=='(') || (c=='}' && peek=='{') || (c==']' && peek=='[')) {
                st.pop();
                continue;
            }
            st.push(c);
        }
        return st.isEmpty();
    }
}
