GPT = 0
CT = 0

for i in range(20):
    subject, credit, grade = input().split()

    if (grade != "P"):
        CT += float(credit)

    match grade:
        case "A+":
            grade = 4.5
        case "A0":
            grade = 4.0
        case "B+":
            grade = 3.5
        case "B0":
            grade = 3.0
        case "C+":
            grade = 2.5
        case "C0":
            grade = 2.0
        case "D+":
            grade = 1.5
        case "D0":
            grade = 1.0
        case "F":
            grade = 0
        case "P":
            grade = 0

    GPT += float(credit) * grade

print(GPT/CT)