
class Calculator:
    def __init__(self ,names ,weights ,totalStudentWeight ,totalStudentCount):
        self.n = names
        self.w = weights
        self.tsw = totalStudentWeight
        self.tsc = totalStudentCount
    def calculate_total_weight(self):
        return (sum(self.w))

with open("sample.txt", "r", encoding = "utf-8") as k:
    mylist = k.readlines()
    totalStudentWeight =0
    for line in mylist:
        StudentWeightList = line.split()
        print(StudentWeightList)
        names = str(StudentWeightList[0])
        weights = float(StudentWeightList[1])
        totalStudentCount = len(mylist)
        totalStudentWeight += (weights)
        print(totalStudentWeight)
        Student = Calculator(names, weights, totalStudentWeight, totalStudentCount)
        print("Students total weight is:", "kg for", totalStudentCount, "students")

        NewStudentName = input("Enter the new student's name:")
        NewStudentWeight = input("Enter the new student's weight (in kg):")
        numeric = float(NewStudentWeight)
        if numeric > 0:
            print("Student's weight entered is numeric")
        else:
            print("Student's weight entered is not numeric")

        NewTotal = totalStudentWeight + float(NewStudentWeight)
        print("New total weight is:", NewTotal, "in kg for,", (totalStudentCount + 1), "students")

