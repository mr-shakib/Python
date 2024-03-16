username = ["Nacht", "Shakib", "mrnacht"]
password = ("p@ssword", "nicepass", "strong")

users = zip(username,password)

for user in users:
    print(user)

users2 = dict(zip(username,password))
print(users2)
for key,value in users2.items():
    print(key +" : "+value)

users3 = list(zip(username,password))
print(users3)

"""We can zip more than two iterables"""

username = ["Nacht", "Shakib", "mrnacht"]
password = ("p@ssword", "nicepass", "strong")
last_login = ["11/2/24","15/2/24","9/3/24"]

users = zip(username,password,last_login)
for user in users:
    print(user)

users = list(zip(username,password,last_login))
print(users)

