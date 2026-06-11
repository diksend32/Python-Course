PASSING_GRADE = 8


class Trainee:
    
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.visited_lectures = 0
        self.done_home_tasks = 0
        self.missed_home_task = 0
        self.missed_lectures = 0
        self.mark = 0

    def visit_lecture(self):   
        self.visited_lectures += 1

    def do_homework(self):
        self.visited_lectures += 2

    def miss_lecture(self):
        self.missed_lectures -= 2

    def miss_homework(self):
        self.missed_home_task -= 2

    def _add_points(self, points):
        if self.mark > 10:
            self.mark = 10
        else:
            self.mark += points

    def _subtract_points(self, points):
            if self.mark > 0:
                self.mark = 0
            else:
                self.mark -= points


    def is_passed(self):
        if self.mark >= 8:
            print('Good job!')
        else:
            print(f"You need to get {8 - self.mark} more points. Try to do your best!")


    def __str__(self):
        status = (
            f"Trainee {self.name.title()} {self.surname.title()}:\n"
            f"done homework {self.done_home_tasks} points;\n"
            f"missed homework {self.missed_home_tasks} points;\n"
            f"visited lectures {self.visited_lectures} points;\n"
            f"missed lectures {self.missed_lectures} points;\n"
            f"current mark {self.mark};\n"
        )
        return status
