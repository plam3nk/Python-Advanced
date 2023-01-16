amount_of_usernames = int(input())
usernames = set()
for _ in range(amount_of_usernames):
    user = input()
    usernames.add(user)

for username in usernames:
    print(username)