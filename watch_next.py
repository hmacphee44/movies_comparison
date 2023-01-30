import spacy
nlp = spacy.load('en_core_web_md')

movies = open('movies.txt', 'r')

"""
Your task is to create a function to return which movies a user would watch
next if they have watched Planet Hulk with the description “Will he save
their world or destroy it? When the Hulk becomes too dangerous for the
Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
planet where the Hulk can live in peace. Unfortunately, Hulk land on the
planet Sakaar where he is sold into slavery and trained as a gladiator.”

The function should take in the description as a parameter and return the
title of the most similar movie.
"""

description = """Will he save their world or destroy it? When the Hulk becomes too 
dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch 
him into space to a planet where the Hulk can live in peace. Unfortunately, 
Hulk land on the planet Sakaar where he is sold into slavery and trained as 
a gladiator."""

movies_list = []
similarity_factors = []


def compare_movies(description):
    for movie in movies:
        title_desc = movie.split(':')
        sim_factor = (nlp(description).similarity(nlp(title_desc[1])))
        movie_sim = [title_desc, sim_factor]
        movies_list.append(movie_sim)
        similarity_factors.append(sim_factor)

    max_sim_factor = max(similarity_factors)

    for i in range(len(movies_list)):
        if max_sim_factor == movies_list[i][1]:
            print(movies_list[i][0][0])


compare_movies(description)
