class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # use a stack
        record_stack = []
        s = 0
        for operation in operations:
            if operation == 'D':
                record_stack.append(2*record_stack[-1])
            elif operation == 'C':
                record_stack.pop()
            elif operation == '+':
                record_stack.append(record_stack[-1] + record_stack[-2])
            else:
                record_stack.append(int(operation))
        for i in range(len(record_stack)):   
            s += record_stack.pop()
        return s

            