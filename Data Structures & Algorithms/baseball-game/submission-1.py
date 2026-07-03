class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # use a stack
        record_stack = []
        s = 0
        for operation in operations:
            if operation == 'D':
                s+=2*record_stack[-1]
                record_stack.append(2*record_stack[-1])
            elif operation == 'C':
                s-=record_stack.pop()
            elif operation == '+':
                s+=record_stack[-1] + record_stack[-2]
                record_stack.append(record_stack[-1] + record_stack[-2])
            else:
                s+=int(operation)
                record_stack.append(int(operation))
        return s

            