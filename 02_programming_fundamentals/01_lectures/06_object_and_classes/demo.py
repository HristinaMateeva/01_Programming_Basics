# class Person:
#     def __init__(self, name, age, kg):
#         self.name = name
#         self.age = age
#         self.kg = kg
#
#
# person = Person("Test", 12, 30)
# p2 = Person("Ines", 23, 60)

class SlidoComment:
    def __init__(self, author_name, content, date="now", author_picture="link", likes=0, dislikes=0):
        self.author_name = author_name
        self.content = content
        self.date = date
        self.likes = likes
        self.dislikes = dislikes
        self.author_picture = author_picture

    def present_comment(self):
        return f"{self.author_name}\n Likes:{self.likes} Dislikes: {self.dislikes} {self.author_picture}"


comment = SlidoComment("No name", content="Ne sum siguren")
comment2 = SlidoComment("Test", ".....")

for _ in range(100):
    comment.likes += 1
print(comment.present_comment())
print(comment2.present_comment())
