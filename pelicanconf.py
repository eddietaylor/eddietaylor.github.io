AUTHOR = 'Ed Taylor, Ph.D.'
SITENAME = "The Data Scientist's Odyssey"
#SITEURL = 'https://eddietaylor.github.io'

PATH = 'content'
STATIC_PATHS = ['images', 'pages']

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

DISPLAY_PAGES_ON_MENU = True

# backdrop options
SITESUBTITLE = "The organized chaos of all things data science, machine learning, and social science"
BACKDROP_IMAGE = '/images/aurora.jpg'
PAGINATED_DIRECT_TEMPLATES = ('categories', 'archives')
PROFILE_IMAGE = '/images/ET.jpg'
FAVICON = '/images/ET.jpg'
SITE_DESCRIPTION = 'Hello! Names Eddie. I finished my PhD in experimental fusion physics in 2019 and have been working as an operations research scientist for a few years. I enjoy all things science and hope to understand my world better by reading the best sources and summarizing the information to the best of my ability for all to enjoy. I hope you enjoy my blog!'
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/edward-taylor-ph-d-330396159/'),('github', 'https://www.github.com/eddietaylor'), ('twitter', 'https://www.twitter.com/eddiedatadoc'))
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

#DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MARKUP = ("md", "ipynb")

from pelican_jupyter import markup as nb_markup
PLUGIN_PATHS=['./plugins']
PLUGINS = [nb_markup, 'render_math']

IGNORE_FILES = [".ipynb_checkpoints"]

THEME = 'C://Users/208766/pelican-themes/backdrop'