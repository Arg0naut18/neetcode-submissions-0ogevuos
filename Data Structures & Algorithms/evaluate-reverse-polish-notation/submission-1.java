class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> elements = new Stack<>();
        String operators = "+-*/";
        for(String token: tokens) {
            if(operators.contains(token)) {
                int operand2 = elements.pop();
                int operand1 = elements.pop();
                if(token.equals("+")) {
                    elements.push(operand1+operand2);
                }
                else if(token.equals("-")) {
                    elements.push(operand1-operand2);
                }
                else if(token.equals("*")) {
                    elements.push(operand1*operand2);
                }
                else if(token.equals("/")) {
                    elements.push(operand1/operand2);
                }
            } else {
                elements.push(Integer.parseInt(token));
            }
        }
        return elements.pop();
    }
}
