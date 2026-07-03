class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # use a stack
        record_stack = []
        s = 0
        for operation in operations:
            if operation == 'D':
                op = 2*record_stack[-1]
                s+=op
                record_stack.append(op)
            elif operation == 'C':
                s-=record_stack.pop()
            elif operation == '+':
                op=record_stack[-1] + record_stack[-2]
                s+=op
                record_stack.append(op)
            else:
                op=int(operation)
                s+=op
                record_stack.append(op)
        return s

            