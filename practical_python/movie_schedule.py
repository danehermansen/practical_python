current_movies = {
    'The Grinch' : '11:00am',
    'Rudolph' : '1:00pm',
    'Frosty the Snowman' : '3:00pm',
    'Christmas Vacation' : '5:00pm'
}
print(' we are currently showing these movies')
for key in current_movies:
    print(key)

movie = input('Which movie do you want to see\n')

showtime = current_movies.get(movie)
if showtime == None:
    print("No showtime found")
else:
    print(movie, 'is plating at', showtime)