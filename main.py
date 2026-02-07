#Talking Data Starter Code
import pandas as pd
import matplotlib.pyplot as plt

#Part 2 Setting up the program
pd.set_option('display.max_columns', None)
pd.set_option('max_colwidth', None)

movieData = pd.read_csv('./rotten_tomatoes_movies.csv')
favMovie = "Your Name. (Kimi No Na Wa.)"
print("My favorite movie is "+favMovie )



#Part 3 Investigate the data
#print(movieData.head())
#print(movieData["movie_title"])

#Part 4 Filter data
print("\nThe data for my favorite movie is:\n")
#Create a new variable to store your favorite movie information
favMovieBooleanList= movieData["movie_title"]==favMovie
favMovieData=movieData.loc[favMovieBooleanList]
print(favMovieData)

print("\n\n")

#Create a new variable to store a new data set with a certain genre

animationMovieBooleanList=movieData["genres"].str.contains("Animation")

animationMovieData=movieData.loc[animationMovieBooleanList]

numOfMovies=animationMovieData.shape[0]


print("We will be comparing " + favMovie +
      " to other movies under the genre Animation in the data set.\n")
print("There are " + str(numOfMovies) + " movies under the category Animation.")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
input("Press enter to see more information about how " + favMovie +
      " compares to other movies in this genre.\n")

#Part 5 Describe data
#min
minr = animationMovieData["audience_rating"].min()
difmin=favMovieData["audience_rating"]-minr
print("The min audience rating of the data set is: " + str(minr))
print(favMovie + " is rated"+ str(float(difmin))+ "points higher than the lowest rated movie.")
print()

#find max
maxr = animationMovieData["audience_rating"].max()
difmax = maxr - favMovieData["audience_rating"]
print("The max audience rating of the data set is: " + str(maxr))
print(favMovie + " is rated " + str(float(difmax)) + " points lower than the highest rated movie.")
print()

#find mean
mean = animationMovieData["audience_rating"].mean()
print("The mean audience rating of the data set is: " + str(mean))
print(favMovie + " is higher than the mean movie rating.")

#find median
median = animationMovieData["audience_rating"].median()
print("The median audience rating of the data set is: " + str(median))
print(favMovie + " is higher than the median movie rating.")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
input("Press enter to see data visualizations.\n")

#Part 6 Create graphs
#Create histogram
plt.hist( animationMovieData["audience_rating"],range=(0,100),bins=20)

#Adds labels and adjusts histogram
plt.grid(True)
plt.title("Audience Ratings of Animation Movies Histogram")
plt.xlabel("Audience Rating")
plt.ylabel("Number of Animation Movies")

#Prints interpretation of histogram
print("According to the histogram, most animation movies have audience ratings between 60 and 90, peaking around 80, indicating generally positive reception. Very few movies fall below a 40 rating, suggesting low-rated animations are rare.")
print("Close the graph by pressing the 'X' in the top right corner.")
print()

#Show histogram
plt.show()

#Create scatterplot
plt.scatter(data=animationMovieData, x= "audience_rating", y="critic_rating")

#Adds labels and adjusts scatterplot
plt.grid(True)
plt.title("Audience Ratings Versus Critic Rating")
plt.xlabel("Audience Ratings")
plt.ylabel("Critic Rating")
plt.xlim(0, 100)
plt.ylim(0, 100)

#Prints interpretation of scatterplot
print("The scatter plot shows a positive correlation between audience ratings and critic ratings—movies rated highly by audiences tend to be rated highly by critics too. However, there's significant spread, especially in mid-range ratings, showing that critics and audiences don’t always agree")
print()

print("Close the graph by pressing the 'X' in the top right corner.")

#Show scatterplot
plt.show()

print("\nThank you for reading through my data analysis!")
