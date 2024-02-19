class StudentsInMLOps:
    def __init__(self):
        self.total_strength = 0
        self.class_name = "MLOps"

    def enrollStudents(self, num):
        if num > 0:
            self.total_strength += num
        else:
            print("Invalid number of students to enroll.")

    def dropStudents(self, num):
        if num > 0 and num <= self.total_strength:
            self.total_strength -= num
        else:
            print("Invalid number of students to drop.")

    def getTotalStrength(self):
        return self.total_strength

    def getClassName(self):
        return self.class_name

# Example usage
if __name__ == "__main__":
    ml_ops_class = StudentsInMLOps()
    print("Class name:", ml_ops_class.getClassName())
    ml_ops_class.enrollStudents(10)
    print("Total strength:", ml_ops_class.getTotalStrength())
    ml_ops_class.dropStudents(3)
    print("Total strength after dropping students:", ml_ops_class.getTotalStrength())
