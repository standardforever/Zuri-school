class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, **kward):
        self.name = kward["name"]
        self.age = kward["age"]
        self.tracks = kward["tracks"]
        self.score = kward["score"]

    def change_name(self, new_name):
        self.name = new_name
    def change_age(self, new_age):
        self.age = new_age
    def add_track(self, new_track):
            self.name = new_track
    def get_score(self):
        return self.score


Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)
print(Bob)
# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
print(Bob.get_score())
