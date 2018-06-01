# Checked by PEP8
import media
import fresh_tomatoes

# My favourite movies
# Call Movie class to generate media.Movie instance for each movie
# each movie object with title, storyline, poster url, and youtube trailer url
Movie_1 = media.Movie("Me Before You",
                      "YA girl in a small town forms an unlikely bond with a recently-paralyzed man she's taking care of. ",  # noqa
                      "https://i.pinimg.com/564x/d6/7f/48/d67f48e5f79575df961e4f3c99d289df.jpg",  # noqa
                      "https://www.youtube.com/watch?v=T0MmkG_nG1U")
Movie_2 = media.Movie("The Godfather",
                      "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.",  # noqa
                      "https://i.pinimg.com/236x/7f/bf/39/7fbf396b1234209ed0c887b8b932476f.jpg",  # noqa
                      "https://www.youtube.com/watch?v=sY1S34973zA")
Movie_3 = media.Movie("3 idiots",
                      "In college, Farhan and Raju form a great bond with Rancho due to his positive and refreshing outlook to life. Years later, a bet gives them a chance to look for their long-lost friend whose existence seems rather elusive.",  # noqa
                      "https://i.pinimg.com/564x/21/a2/4b/21a24b99327be8cde9135c1b3e5c2b01.jpg",  # noqa
                      "https://www.youtube.com/watch?v=xvszmNXdM4w")
Movie_4 = media.Movie("Braveheart",
                      "William Wallace is the medieval Scottish patriot who is spurred into revolt against the English when the love of his life is slaughtered. Leading his army into battles that become a war, his advance into England threatens King Edward I's throne before he is captured and executed, but not before becoming a symbol for a free Scotland.",  # noqa
                      "https://i.pinimg.com/564x/8a/a3/54/8aa3543b31fbef0583e1afa3445de880.jpg",  # noqa
                      "https://www.youtube.com/watch?v=qDGjf3OZhKc")
Movie_5 = media.Movie("Harry Potter and the Half-Blood Prince",
                      "As Death Eaters wreak havoc in both Muggle and Wizard worlds, Hogwarts is no longer a safe haven for students. Though Harry (Daniel Radcliffe) suspects there are new dangers lurking within the castle walls, Dumbledore is more intent than ever on preparing the young wizard for the final battle with Voldemort. Meanwhile, teenage hormones run rampant through Hogwarts, presenting a different sort of danger. Love may be in the air, but tragedy looms, and Hogwarts may never be the same again.",  # noqa
                      "https://i.pinimg.com/236x/70/a5/bc/70a5bcfdcb2ddbb981167a1693342176.jpg",  # noqa
                      "https://www.youtube.com/watch?v=JYLdTuL9Wjw")
Movie_6 = media.Movie("Face off",
                      "Obsessed with bringing terrorist Castor Troy (Nicolas Cage) to justice, FBI agent Sean Archer (John Travolta) tracks down Troy, who has boarded a plane in Los Angeles. After the plane crashes and Troy is severely injured, possibly dead, Archer undergoes surgery to remove his face and replace it with Troy's. As Archer tries to use his disguise to elicit information about a bomb from Troy's brother, Troy awakes from a coma and forces the doctor who performed the surgery to give him Archer's face.",  # noqa
                      "https://i.pinimg.com/564x/86/55/bc/8655bcdbf6fdd7da79408edcbf6099f7.jpg",  # noqa
                      "https://www.youtube.com/watch?v=95VvTW1FvS8")

# list of n movies
movies_list = [Movie_1, Movie_2, Movie_3, Movie_4, Movie_5, Movie_6]

# use open_movies_page function in fresh_tomatoes module with "movielist" input
fresh_tomatoes.open_movies_page(movies_list)

# Following commands shows title, storyline, poster image and youtube trailer
# print(Movie_1.title)
# print(Movie_1.storyline)
# Movie_1.show_poster()
# Movie_1.show_trailer()
