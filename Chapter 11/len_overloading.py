class student:
    def __init__(self, subject):
        self.subject = subject

    def __len__(self):
        return len(self.subject)

s = student(["java","python","c","MySQL"])
print(len(s))