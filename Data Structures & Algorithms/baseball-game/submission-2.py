class Solution:
    def calPoints(self, operations: List[str]) -> int:
        points = []

        def is_number(s):
            try:
                float(s)
                return True
            except ValueError:
                return False

        for x in operations:
            if is_number(x):
                points.append(int(x))
            elif x == "+":
                points.append(points[-2] + points[-1])
            elif x == "C":
                points.pop()
            elif x == "D":
                print(points)
                points.append(points[-1] * 2)
        return sum(points)        