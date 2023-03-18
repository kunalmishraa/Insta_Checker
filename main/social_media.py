import instaloader

# create an instance of Instaloader class
L = instaloader.Instaloader()

# prompt the user to enter the Instagram username to analyze
username = input("Enter the Instagram username to analyze: ")

# get the profile of the user
profile = instaloader.Profile.from_username(L.context, username)

# print the number of followers and following
print(f"The number of followers of {username} is {profile.followers}")
print(f"The number of accounts {username} is following is {profile.followees}")
