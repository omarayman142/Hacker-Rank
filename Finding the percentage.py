if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for i in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
queried_scores = student_marks[query_name]
x = (queried_scores[0] + queried_scores[1] + queried_scores[2]) / 3.00
print("%.2f" % x)
