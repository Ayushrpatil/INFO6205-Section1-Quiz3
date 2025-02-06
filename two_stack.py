"""
Dijkstra’s Two-Stack Algorithm for Expression Evaluation

This algorithm evaluates arithmetic expressions written in infix notation using two stacks:
1. **Operand Stack:** Stores numbers (operands).
2. **Operator Stack:** Stores operators (+, -, *, /).

eg: "((3 + 2) * 5)" evaluates to 25

### How It Works:
- **When encountering a number:** Push it onto the operand stack.
- **When encountering an operator:** Push it onto the operator stack.
- **When encountering a left parenthesis (`(`):** Do nothing (it just signifies precedence).
- **When encountering a right parenthesis (`)`)**:
  - Pop an operator from the operator stack.
  - Pop two operands from the operand stack.
  - Apply the operator to these two operands.
  - Push the result back onto the operand stack.
- **When expression is fully parsed:** The operand stack contains the final result.

This ensures correct evaluation based on operator precedence and parentheses.
"""

def evaluate_expression(expression: str) -> int:
    """
    Evaluate an arithmetic expression using Dijkstra’s Two-Stack Algorithm.

    :param expression: str - The arithmetic expression in infix notation.
    :return: int - The result of evaluating the expression.
    """
    operators = []
    operands = []

    def apply_operator():
        """Applies the top operator on the top two operands and pushes the result back."""
        if len(operands) < 2 or not operators:
            return
        val2 = operands.pop()
        val1 = operands.pop()
        op = operators.pop()
        
        if op == '+':
            operands.append(val1 + val2)
        elif op == '-':
            operands.append(val1 - val2)
        elif op == '*':
            operands.append(val1 * val2)
        elif op == '/':
            operands.append(val1 // val2)  

    i=0
    while i < len(expression):
        char = expression[i]

        if char == ' ':
            i += 1
            continue

        if char.isdigit():  
            num = 0
            while i < len(expression) and expression[i].isdigit():
                num = num * 10 + int(expression[i])
                i += 1
            operands.append(num)
            continue

        elif char in "+-*/":
            while (operators and operators[-1] in "+-*/" and char in "+-*/"):
                apply_operator()
            operators.append(char)

        elif char == '(':
            operators.append(char)

        elif char == ')':
            while operators and operators[-1] != '(':
                apply_operator()
            operators.pop()  

        i += 1

    while operators:
        apply_operator()

    return operands.pop() if operands else 0


expression = "((3 + 2) * 5)"
result = evaluate_expression(expression)
print(f"Result: {result}")  
