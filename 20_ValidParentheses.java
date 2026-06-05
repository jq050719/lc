class Solution {
    public boolean isValid(String s) {
        List<Character> stack = new ArrayList<>();
        Map<Character, Character> openToClosed = new HashMap<>();
        openToClosed.put('(', ')');
        openToClosed.put('[', ']');
        openToClosed.put('{', '}');

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == '(' || c == '{' || c == '[') {
                stack.add(c);
            }
            else {
                // We have a closed bracket
                if (stack.size() == 0) {  // No corresponding open bracket
                    return false;
                }

                // Pop element from the stack
                char bracket = stack.remove(stack.size() - 1);  // This is an open bracket
                if (openToClosed.get(bracket) != c) {
                    return false;
                }
            }
        }

        // True iff stack is empty
        return stack.size() == 0;
    }
}
