
class Student:

    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = str(name)
        self.age = int(age)
        self.tracks = list(tracks)
        self.score = float(score)

    def change_name(self, change_name):
        self.name = change_name
        print(self.name)

    def change_age(self, change_age):
        self.age = change_age
        s = isinstance(change_age, int)
        if s == True:
            print(self.age)
        else:
            print('You did not enter a number')

    def add_track(self, add_tracks):
        self.tracks.append(add_tracks)
        print(self.tracks)

    def get_score(self):
        print(self.score)


Bob = Student("Bob", 26, ["FE", "BE"], 20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
