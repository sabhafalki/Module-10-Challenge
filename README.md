# Module-10-Challenge Mission to Mars
# Overview of Project #
The purpose of this Project is to create a Robin's web app to gather data from all the websites by web scraping.She wants to create portfolio, so that she can share it with Astroport, Nasa one day. She vistes many sites with news about space exploration especially Mission to Mars.She had been admiring images of Mars’s hemispheres online and realized that the site is scraping-friendly. She would like to adjust the current web app to include all four of the hemisphere images. To do this, you’ll use BeautifulSoup and Splinter to scrape full-resolution images of Mars’s hemispheres and the titles of those images, store the scraped data on a Mongo database, use a web application to display the data, and alter the design of the web app to accommodate these images.

The analysis consisted of the following:
1. Scrape Full-Resolution Mars Hemisphere Images and Titles
2. Update the Web App with Mars Hemisphere Images and Titles
3. Add Bootstrap 3 Components

# Resources #

- Web pages scraped:<br>
  - https://data-class-mars.s3.amazonaws.com/Mars/index.html
  - https://spaceimages-mars.com
  - https://galaxyfacts-mars.com
  - https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars/<br>
- Software:<br>
  Python<br>
  Jupyter Notebook<br>
  Pandas, BeautifulSoup, Splinter, ChromeDriverManager, Flask, PyMongo<br>
  MongoDB<br>
  HTML5<br>
  Bootstrap 3<br>
# Results #
## an ETL Function to Read Three Data Files ##
To Extract the three data files (wiki, kaggle, movielens). MovieLens is a website run by the GroupLens research group at the University of Minnesota. The Kaggle dataset pulls from the MovieLens dataset of over 20 million reviews and contains a metadata file with details about the movies from The Movie Database.<br>

The following depicts the wiki_movies_df DataFrame:<br>
![Movie_DataFrame](/Image/Wiki_Movies.png) <br>

The following depicts the kaggle_metadata DataFrame: <br>
![MataData](/Image/kaggle_metadata.png) <br>

The following depicts the ratings DataFrame: <br>
![Ratings](/Image/Rating.png) <br>

##  Extract and Transform the Wikipedia Data ##
Filtering out bad data is important, in order to get good clean data and a cleaned Wikipedia data is converted to a Pandas DataFrame for clear view.<br>
The following depicts the columns from wiki_movies_df DataFrame to a list:<br>
![wiki_movie](/Image/to_list.png) <br>
<br><br>

## Extract and Transform the Kaggle data ##
The extraction and transformation of the Kaggle metadata using the ETL function and performe the merging of Wikipedia and Kaggle DataFrames. <br>
![wiki_movie](/Image/Wiki_Movies.png)<br>
<br><br>

## The Movie Database ##
The Movie DataFrame consist of the movies table and ratings table in the SQL database, by adding elapsed time to the database.
The following depicts the movies table in SQL database.<br>
![movies_query](/resources/movies_query.png)<br>
The following depicts the ratings table in SQL database.<br>
![ratings_query](/resources/ratings_query.png)<br>
<br><br>
