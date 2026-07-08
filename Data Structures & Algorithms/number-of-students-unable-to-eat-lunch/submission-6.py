class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        st0 = 0
        st1 = 0
        for student in students:
            if student == 0:
                st0+=1
            else:
                st1+=1
        for sandwich in sandwiches:
            if sandwich == 0:
                if st0==0:
                    return st1
                st0-=1
            else:
                if st1==0:
                    return st0
                st1-=1
        return 0