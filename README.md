# Module-10-Challenge Mission to Mars
# Overview of Project #
The purpose of this Project is to update Robin's web app to gather data from all the websites by web scraping. Robin's Web App scrapes the Mission to Mars News Website. The Web App needed to be updated to inlucde all the hemisphere images. In order to accomplish this, we will use BeautifulSoup and Splinter to scrape full-resolution images of Mars’s hemispheres and the titles of those images, store the scraped data on a Mongo database, use a web application to display the data, and alter the design of the web app to accommodate these images.

The web Scaping consisted of the following:
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
   <br><br>
   
# Results #
## Scrape Full-Resolution Mars Hemisphere Images and Titles and Update the Web App ##
The website url consists of four Mars Hemisphere news articals along with images and title for each Mars Hemispher. Using BeautifulSoup and Splinter, we were able to  retrieve a full-resolution image and title for each hemisphere. The Mongo database is updated to contain the full-resolution image URL and title for each hemisphere image.
The following depicts the scapped code:<br>
![code](/Image/code.png) <br>

##  Add Bootstrap 3 Components ##
We have added the following additional bootstrap components:
1. Changed the Button CSS Style
2. Changed the format of the Text and Layout
3. Changed the Layout and format of the Table
4. Added the hemisphere images as thumbnails <br>
![fig1](/Image/fig1.png) <br>
<br><br>
![fig2](/Image/fig2.png) <br>
<br><br>

![fig3](/Image/fig3.png) <br>
<br><br>

![fig4](/Image/fig4.png) <br>
<br><br>
