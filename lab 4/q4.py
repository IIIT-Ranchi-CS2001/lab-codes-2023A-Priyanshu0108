
singers = {"Alice", "Bob", "Charlie", "Diana"}
dancers = {"Charlie", "Diana", "Eve", "Frank"}

singers_set = {student for student in singers}
dancers_set = {student for student in dancers}

all_artists = singers_set | dancers_set
allrounders = singers_set & dancers_set
dancers_not_singers = dancers_set - singers_set
singers_not_dancers = singers_set - dancers_set
exclusive_artists = singers_set ^ dancers_set

print("All artists of the class:", all_artists)
print("All-rounders of the class:", allrounders)
print("Dancers but not singers:", dancers_not_singers)
print("Singers but not dancers:", singers_not_dancers)
print("Exclusive artists (Dancers but not singers or Singers but not dancers):", exclusive_artists)
