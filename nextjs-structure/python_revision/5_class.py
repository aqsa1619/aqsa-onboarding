# @dataclass automatically generates some useful methods, including an initializer (__init__) for storing the attributes.
# self refers to the current object
# mark_done() changes the task status from Pending to Done.


from dataclasses import dataclass


@dataclass
class Task:
    title: str
    assignee: str
    status: str = "Pending"

    def mark_done(self):
        self.status = "Done"

task1 = Task("Complete Python revision", "Ali")

print(task1)

task1.mark_done()

print(task1)
