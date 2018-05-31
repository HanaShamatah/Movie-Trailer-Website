# Checked by PEP8
import media
import fresh_tomatoes

# My favourite movies
# Call Movie class to generate media.Movie instance for each movie
# each movie object with title, storyline, poster url, and youtube trailer url
Movie_1 = media.Movie("Me Before You", "Young and quirky Louisa Lou Clark (Emilia Clarke) moves from one job to the next to help her family make ends meet. Her cheerful attitude is put to the test when she becomes a caregiver for Will Traynor (Sam Claflin), a wealthy young banker left paralyzed from an accident two years earlier. Will's cynical outlook starts to change when Louisa shows him that life is worth living. As their bond deepens, their lives and hearts change in ways neither one could have imagined.", "https://i.pinimg.com/564x/d6/7f/48/d67f48e5f79575df961e4f3c99d289df.jpg", "https://www.youtube.com/watch?v=T0MmkG_nG1U")
Movie_2 = media.Movie("The Godfather", "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.", "https://i.pinimg.com/236x/7f/bf/39/7fbf396b1234209ed0c887b8b932476f.jpg", "https://www.youtube.com/watch?v=sY1S34973zA")
Movie_3 = media.Movie("3 idiots", "In college, Farhan and Raju form a great bond with Rancho due to his positive and refreshing outlook to life. Years later, a bet gives them a chance to look for their long-lost friend whose existence seems rather elusive.", "https://i.pinimg.com/564x/21/a2/4b/21a24b99327be8cde9135c1b3e5c2b01.jpg", "https://www.youtube.com/watch?v=xvszmNXdM4w")
Movie_4 = media.Movie("Braveheart", "William Wallace is the medieval Scottish patriot who is spurred into revolt against the English when the love of his life is slaughtered. Leading his army into battles that become a war, his advance into England threatens King Edward I's throne before he is captured and executed, but not before becoming a symbol for a free Scotland.", "https://i.pinimg.com/564x/8a/a3/54/8aa3543b31fbef0583e1afa3445de880.jpg", "https://www.youtube.com/watch?v=qDGjf3OZhKc")
Movie_5 = media.Movie("Harry Potter and the Half-Blood Prince", "As Death Eaters wreak havoc in both Muggle and Wizard worlds, Hogwarts is no longer a safe haven for students. Though Harry (Daniel Radcliffe) suspects there are new dangers lurking within the castle walls, Dumbledore is more intent than ever on preparing the young wizard for the final battle with Voldemort. Meanwhile, teenage hormones run rampant through Hogwarts, presenting a different sort of danger. Love may be in the air, but tragedy looms, and Hogwarts may never be the same again.", "https://i.pinimg.com/236x/70/a5/bc/70a5bcfdcb2ddbb981167a1693342176.jpg", "https://www.youtube.com/watch?v=JYLdTuL9Wjw")
Movie_6 = media.Movie("Face off", "Obsessed with bringing terrorist Castor Troy (Nicolas Cage) to justice, FBI agent Sean Archer (John Travolta) tracks down Troy, who has boarded a plane in Los Angeles. After the plane crashes and Troy is severely injured, possibly dead, Archer undergoes surgery to remove his face and replace it with Troy's. As Archer tries to use his disguise to elicit information about a bomb from Troy's brother, Troy awakes from a coma and forces the doctor who performed the surgery to give him Archer's face.", "https://i.pinimg.com/564x/86/55/bc/8655bcdbf6fdd7da79408edcbf6099f7.jpg", "https://www.youtube.com/watch?v=95VvTW1FvS8")


movies_list = [Movie_1, Movie_2, Movie_3, Movie_4, Movie_5, Movie_6]  # list of n movies

# use open_movies_page function in repository code with "movie list" input
fresh_tomatoes.open_movies_page(movies_list)

###
# print(Me_before_you.title)
# print(Me_before_you.storyline)
# Me_before_you.show_poster()
# Me_before_you.show_trailer()
