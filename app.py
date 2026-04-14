"""
Hekima Junior School - Financial Sustainability & Academic Excellence System
A streamlined solution for managing school operations, finances, and student performance.
"""

class Student:
    def __init__(self, name, grade, fees):
        self.name = name
        self.grade = grade
        self.fees_balance = fees
        self.scores = {}
        self.attendance = 0
    
    def add_score(self, subject, score):
        self.scores[subject] = max(0, min(100, score))
    
    def average(self):
        return sum(self.scores.values()) / len(self.scores) if self.scores else 0
    
    def pay_fees(self, amount):
        self.fees_balance = max(0, self.fees_balance - amount)


class HekimaSchool:
    def __init__(self):
        self.students = {}
        self.income = {'fees': 0, 'donations': 0}
        self.expenses = {'salaries': 0, 'operations': 0}
    
    def register(self, sid, name, grade, fees=5000):
        self.students[sid] = Student(name, grade, fees)
        print(f"Registered: {name}")
    
    def record_fees(self, sid, amount):
        if sid in self.students:
            self.students[sid].pay_fees(amount)
            self.income['fees'] += amount
            print(f"Fees paid: ${amount}")
    
    def record_grade(self, sid, subject, score):
        if sid in self.students:
            self.students[sid].add_score(subject, score)
            print(f"Grade recorded: {subject} = {score}")
    
    def academic_report(self):
        print("\n" + "="*50)
        print("ACADEMIC PERFORMANCE REPORT")
        print("="*50)
        for sid, s in self.students.items():
            avg = s.average()
            status = "Excellent" if avg >= 80 else "Good" if avg >= 60 else "Needs Improvement"
            print(f"{s.name} (Grade {s.grade}): Avg={avg:.1f}% - {status}")
            print(f"  Fees Balance: ${s.fees_balance:.2f}")
    
    def financial_report(self):
        total_income = sum(self.income.values())
        total_expenses = sum(self.expenses.values())
        profit = total_income - total_expenses
        
        print("\n" + "="*50)
        print("FINANCIAL REPORT")
        print("="*50)
        print(f"Total Income: ${total_income:.2f}")
        print(f"Total Expenses: ${total_expenses:.2f}")
        print(f"Net Profit: ${profit:.2f}")
        
        if profit > 0:
            print("Status: SUSTAINABLE ✅")
        else:
            print("Status: DEFICIT - Review needed")
    
    def excellence_scholarships(self, threshold=85, fund=5000):
        """Reward top performers with fee discounts"""
        eligible = [(s.name, s.average()) for s in self.students.values() if s.average() >= threshold]
        eligible.sort(key=lambda x: x[1], reverse=True)
        
        print("\n" + "="*50)
        print("EXCELLENCE SCHOLARSHIPS")
        print("="*50)
        if eligible:
            award = fund / len(eligible)
            for name, avg in eligible:
                print(f"{name} (Avg={avg}%): ${award:.2f} scholarship")
        else:
            print("No students qualified this term")
    
    def run(self):
        """Execute the complete school management system"""
        print("\n🏫 HEKIMA JUNIOR SCHOOL MANAGEMENT SYSTEM")
        print("="*50)
        
        # Register students
        self.register("S01", "John Mwangi", 5, 5800)
        self.register("S02", "Mary Wanjiku", 5, 5800)
        self.register("S03", "Peter Omondi", 6, 6000)
        
        # Record fees
        self.record_fees("S01", 5800)
        self.record_fees("S02", 5000)
        self.record_fees("S03", 6000)
        
        # Record grades
        self.record_grade("S01", "Math", 92)
        self.record_grade("S01", "English", 88)
        self.record_grade("S02", "Math", 78)
        self.record_grade("S02", "English", 85)
        self.record_grade("S03", "Math", 65)
        self.record_grade("S03", "English", 70)
        
        # Set expenses
        self.expenses['salaries'] = 12000
        self.expenses['operations'] = 3000
        
        # Generate reports
        self.academic_report()
        self.financial_report()
        self.excellence_scholarships()
        
        # Final recommendation
        print("\n" + "="*50)
        print("RECOMMENDATIONS")
        print("="*50)
        print("✅ Maintain high-performer scholarships to boost excellence")
        print("✅ Monitor fee collection to ensure sustainability")
        print("✅ Provide remedial support for struggling students")


# Run the system
if __name__ == "__main__":
    school = HekimaSchool()
    school.run()
