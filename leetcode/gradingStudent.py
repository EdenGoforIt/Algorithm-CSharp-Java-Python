def gradingStudents(grades):
    failing_score = 38
    for i in range(len(grades)):
        grade = grades[i]
        if grade < failing_score:
            continue
        # 84 , 59
        if 5 - (grade % 5) < 3:
            new = grade + 5 - (grade % 5)
            grades[i] = new
    return grades


if __name__ == '__main__':
    print(gradingStudents([38]))
