class Course:
    def __init__(self, course: str, grade: int, creds: int):
        self.__name = course
        self.__grade = grade
        self.__creds = creds
    
    def course(self):
        return self.__name
    
    def grade(self):
        return self.__grade
    
    def credits(self):
        return self.__creds
    
    
class CourseTracker:
    def __init__(self):
         self.__course_list = {}

    def add_course(self, course, grade, creds):
        if course not in self.__course_list:
            self.__course_list[course] = Course(course, grade, creds)
        else:
            if self.__course_list[course].grade() < grade:
                self.__course_list[course] = Course(course, grade, creds)

    def get_data(self, course):
        if course in self.__course_list:
            return self.__course_list[course]
        else:
            return None
        
    def total_courses(self):
        return len(self.__course_list)
    
    def total_credits(self):
        total = 0
        for key, course in self.__course_list.items():
            total += course.credits()

        return total
    
    def median(self):
        total = 0
        for key, course in self.__course_list.items():
            total += course.grade()

        return round(total / self.total_courses(),1)
    
    def distribution(self):
        for i in range(5, 0, -1):
            count = 0
            for course in self.__course_list.values():
                if course.grade() == i:
                    count += 1
            print(f"{i}: {count * "x"}")

    

class Application:
    def __init__(self):
        self.__coursetracker = CourseTracker()

    def help(self):
        print("1 add course")
        print("2 get course data")
        print("3 statistics")
        print("0 exit")

    def add_course(self):
        course = input("course: ")
        grade = int(input("grade: "))
        creds = int(input("credits: "))

        self.__coursetracker.add_course(course, grade, creds)


    def get_course_data(self):
        course = input("course: ")
        data = self.__coursetracker.get_data(course)
        if data == None:
            print("no entry for this course")
        else:
            print(f"{data.course()} ({data.credits()} cr) grade {data.grade()}")
    
    def statistics(self):
        totalcredits = self.__coursetracker.total_credits()
        totalcourses = self.__coursetracker.total_courses()
        average = self.__coursetracker.median()

        print(f"{totalcourses} completed courses, a total of {totalcredits} credits")
        print(f"mean {average}")
        print("grade distribution")
        self.__coursetracker.distribution()


    def interface(self):
        self.help()

        while True:
            command = input("command: ")

            if command == "0":
                break
            elif command == "1":
                self.add_course()
            elif command == "2":
                self.get_course_data()
            elif command == "3":
                self.statistics()
            else:
                pass


#if __name__ == "__main__":
application = Application()
application.interface()
