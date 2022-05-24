import sys

num_movies = int(input())
movie = ""
rate = 0
highest_rate = -sys.maxsize
lowest_rate = sys.maxsize
highest_rate_movie = ""
lowest_rate_movie = ""
total_rate = 0

for i in range(num_movies):
    movie = input()
    rate = float(input())
    total_rate += rate
    if rate > highest_rate:
        highest_rate = rate
        highest_rate_movie = movie
    elif rate < lowest_rate:
        lowest_rate = rate
        lowest_rate_movie = movie

average_rate = total_rate / num_movies

# outputs
print(f"{highest_rate_movie} is with highest rating: {highest_rate:.1f}")
print(f"{lowest_rate_movie} is with lowest rating: {lowest_rate:.1f}")
print(f"Average rating: {average_rate:.1f}")
