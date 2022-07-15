# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
# set executable path
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)
# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)

# 1) Searching for elements with a specific combination of tag (div) and attribute (list_text).
# 2) Telling browser to wait one second before searching for components.
# set up the HTML parser
html = browser.html
news_soup = soup(html, 'html.parser')               # slide_elem  holds all of the other elements within it.
slide_elem = news_soup.select_one('div.list_text')  # . is used to select the classes div.list_text(or to pinpoint).

# when using select_one, the first matching element returned will be a <li /> element with 
# a class of slide and all nested elements within it.    
# Let's begin our scraping
slide_elem.find('div', class_='content_title') # The specific data is in a <div /> with a class of 'content_title'.

# slide_elem variable holds a ton of information, so to find this specific data in it.
# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
# get_text() return only the title of the news article and not any of the HTML tags or elements.
news_title
# We’ll need to change the class to “article_teaser_body.” we’re searching for the summary instead of the title, so we’ll need to use the unique class associated with the summary.
# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text() 
# Output is the summary of the article
news_p

# ### Featured Images
# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)
# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]    # The brower finds an element by its tag.
                                                      # full_image_elem is a new variable to hold the scaping result. 
full_image_elem.click()                               # Splinter will "click" the image to vew its full size.

# The automated browser should automatically "click" the button and change the view to a slideshow of images.
# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup

# The image tag and class (<img />and fancybox-img) to build the URL to the full-size image.
# An img tag is nested within this HTML, so we've included it.
# .get('src') pulls the link to the image.
# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src') 
img_url_rel

# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url

# create DataFrame
df = pd.read_html('https://galaxyfacts-mars.com')[0] # Creating a new DataFrame from the HTML table
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df
# .set_index() function turns the Description column into the DataFrame's index.
# inplace=True means that the updated index will remain in place, without having to reassign the DataFrame to a new variable.

# convert our DataFrame back into HTML-ready code
df.to_html()

df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()
browser.quit()


# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager

# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# ### Visit the NASA Mars News Site
# Visit the mars nasa news site
url = 'https://redplanetscience.com/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)
# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')
slide_elem.find('div', class_='content_title')
# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title
# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p
# ### JPL Space Images Featured Image
# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)

# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()
# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup
# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel
# Use the base url to create an absolute url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# ### Mars Facts
df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()
df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df

df.to_html()


#  D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ### Hemispheres
# 1. Use browser to visit the URL 
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)
# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
for j in range(4):
    # Browse through each article
    browser.links.find_by_partial_text('Hemisphere')[j].click()
    
    # Parse the HTML
    html = browser.html
    web_soup = soup(html,'html.parser')
    # title = soup.find('div', id="title").h2.text
    title = web_soup.find('h2', class_='title').text
    img_url = web_soup.find('li').a.get('href')
    
    # Store findings into a dictionary and append to list
    hemispheres = {}
    hemispheres['img_url'] = img_url
    hemispheres['title'] = title
    hemisphere_image_urls.append(hemispheres)
        
# Browse back to repeat
browser.back()
# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls

# 5. Quit the browser
browser.quit()







