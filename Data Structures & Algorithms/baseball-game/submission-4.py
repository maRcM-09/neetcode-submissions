class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # use a stack
        record_stack = []
        s = 0
        for i, operation in enumerate(operations):
            if operation == '+':
                record_stack.append(
                    record_stack[-1] + record_stack[-2])
            elif operation == 'D':
                record_stack.append(2*record_stack[-1])
            elif operation == 'C':
                record_stack.pop()
            
            else:
                record_stack.append(int(operation))
        for record in record_stack:
            s+=record
        return s

            