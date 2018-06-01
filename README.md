# Movie-Trailer-Website
Generate a website shows your favourite movies with their poster image and youtube tariler.
## Project Steps
- Create **Movie class** in [media.py](https://github.com/HanaShamatah/Movie-Trailer-Website/blob/master/media.py) file that: 
  - Save multiple instances that identifying: the title, storyline, poster image, and youtube trailer of the movie.
  - Identify instances methods to open the poster image and trailer URL.
- Call the constructor media.Movie() to instantiate movie objects in [entertainment_center.py](https://github.com/HanaShamatah/Movie-Trailer-Website/blob/master/entertainment_center.py).
- Use [fresh_tomatoes.py](https://github.com/udacity/ud036_StarterCode) python module that creates an _HTML_ file to generate a website that displays these movies by calling the _open_movies_page_ function with movies list as an input.

## Get started
Fork this repository to create your own copy in GitHub. Then clone your repository to work on this project locally on your computer.

## How to Run
- Open [entertainment_center.py](https://github.com/HanaShamatah/Movie-Trailer-Website/blob/master/entertainment_center.py) code
- Add your _n_ favourite movies starting from movie 1 in line 8 with the following inputs in order:
  - Title
  - Storyline
  - poster image url
  - Youtube trailer url
- Edit the movies list in line 34 to the number of movies you have inserted _"n"_.
- Then, run the code according to the text editor you are using. I used ctrl+B in Sublime Text3 to run.
- The website will open with your favourite movies list.
- If you run the code without editing, you will open a website of my favourite movies.

 ## Notes
- The codes are organized according to [PEP8 Style Guide](https://www.python.org/dev/peps/pep-0008/#tabs-or-spaces)
- _E501 error_ "line too long" appears from testing _entertainment_center.py_ code in PEP8 online code check because some movies have a long storyline that cannot be split into many lines.

## License
The content of this repository is licensed under an [MIT](https://choosealicense.com/licenses/mit/)
