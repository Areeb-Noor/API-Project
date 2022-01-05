#importing requests to allow for use of request function
import requests

#prompting user for a movie name as a string 
movie_name = str(input("Enter a movie please: "))

#declaring API key which will be used for authentication
api_key = 'b4779db09cabdb2c3b96f778ac5bbe3c'

#decalring path that program will use to reach the endpoint/server
end_point_path = 'https://api.themoviedb.org/3/search/movie'

#declaring variable to hold the response recieved from endpoint/server. Also joining together the path, authenticaiton key, and movie inputed from user as the request/get function
response = requests.get(end_point_path+"?api_key="+api_key+"&"+"query="+movie_name)

#converting recieved response into json file so it can be viewed as text
movie_info = response.json()

#setting boolean expression for later use in movie found or not found scenarios
movie_found = None 

#declaring variable to hold array of movie elements recieved 
list_of_movies = movie_info["results"]

#iterating over array of movies and more specefically the "title" key to search for a title exactly matching inputed movie name
for movie in list_of_movies:

#printing movie info if movie is found
    if movie['title'] == movie_name:
        movie_found = True
        print("Movie found!")
        print("Movie:",movie_name)
        print()
        print("Movie overview:",movie['overview'])
        print("Release date:",movie['release_date'])
        print("Reviews:",movie['vote_count'])
        print("Rating:",movie['vote_average'])

#returning code for when the movie is found and program runs with no issues
if movie_found == True:
    print("200: Movie found")

#returning code for if movie was not found 
else:
    print("Error 404: Movie not found :(") 
