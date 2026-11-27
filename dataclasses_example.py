"""Topic 30: dataclasses for simple data objects."""


from dataclasses import dataclass


@dataclass
class Student:
    # Dataclass thinking:
    # If a class mainly stores data, `@dataclass` can write common methods
    # like `__init__` and a readable `__repr__` for you.
    name: str
    score: int

    def is_passing(self) -> bool:
        # You can still add normal methods when the object needs behavior.
        return self.score >= 70


student = Student("Maya", 92)

print(student)
print(f"Passing? {student.is_passing()}")


@dataclass
class Course:
    title: str
    students: list[str]


course = Course("Python Basics", ["Maya", "Leo"])
print(course)

# Use a dataclass when:
# - the class mostly holds named pieces of data
# - you want cleaner setup code
# - you still want methods connected to that data

course.students.append("Ari")
print(f"Updated course: {course}")

print(f"Course student count: {len(course.students)}")

print(f"Maya is enrolled? {'Maya' in course.students}")

print(f"Course title: {course.title}")

new_student = Student("Leo", 78)
print(f"New student passing? {new_student.is_passing()}")

borderline_student = Student("Ari", 69)
print(f"Borderline student passing? {borderline_student.is_passing()}")

print(f"Ari passes? {Student('Ari', 69).is_passing()}")
