import media

import BestMovies



toy_story3 = media.Movie("Toy Story3","dumb pixar movie", 'https://upload.wikimedia.org/wikipedia/commons/0/06/Toy_Story_3_Logo_Black.svg', "https://www.youtube.com/watch?v=JcpWXaA2qeg")

toy_story2 = media.Movie("Toy Story2","dumb pixar movie",'https://upload.wikimedia.org/wikipedia/commons/e/e2/Toy_Story_2_logo.svg', "https://www.youtube.com/watch?v=Lu0sotERXhI")


movies = [toy_story3,toy_story2]

BestMovies.open_movies_page(movies)




