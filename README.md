# Data Science Website Development and Deployment

Instructions on getting the environment set up and publishing your first site content.

## Getting Up and Running with Development

1.) Clone the repo if you're collaborating with Eddie on his DS website. Otherwise, within a local folder, create a virtual environment with (in this case named blog_env):

```console
foo@bar:~$ virtualenv blog_env
```

or if this command does not work:
```console
foo@bar:~$ python -m virtualenv blog_env
```

2.) Always activate the environment when beginning to develop:
```console
foo@bar:~$ source blog_env/Scripts/activate
```

Note: See https://docs.python-guide.org/dev/virtualenvs/ for more info on setting up virtual environments.

3.) Create a requirement.txt file if you're creating your own website (else switch to the dev branch where the requirements.txt file is located).
Within the file, write the following:

```
Markdown
pelican
jupyter>=1.0
ipython>=4.0
nbconvert<6
beautifulsoup4
ghp-import
matplotlib
```

4.) Make sure to install the requirements in this venv with:

```console
foo@bar:~$ pip install -r requirements.txt
```

5.) Create the data science blog dev lab if you're creating your own website with:

```console
foo@bar:~$ pelican-quickstart
```

Most important to fill out is the title of the site, the author, n for URL prefix and the timezone.

6.) If you're creating your own website, ```git init``` to initialize the current folder as a git repo

7.) Pip install pelican-jupyter

8.) If you're creating your own website, enable jupyter notebooks for Pelican by adding the following to the `pelicanconf.py` file:

```python
MARKUP = ("md", "ipynb")

from pelican_jupyter import markup as nb_markup
PLUGINS = [nb_markup]

IGNORE_FILES = [".ipynb_checkpoints"]
```

9.) To write your first post, create a jupyter notebook within the content folder. Create a file with the same name as the notebook with the extension: .nbdata
and with the following fields filled out (need that empty line at the end):

```
Title:
Slug:
Date:
Category:
Tags:
Author:
Summary:

```
Note: see https://github.com/danielfrg/pelican-jupyter for more info

10.) To then convert this to html, run ```pelican content``` and then ```pelican -l``` to open the html files in your browser.
Visit the site at the displayed url.

## Creating a Github Page (If you're creating your own website)

1.) Create a repo on github titled ```username.github.io``` where ```username``` is your Github username

2.) Within your local git repo folder, add the github repo as origin to your local repo by running:

```console
foo@bar:~$ git remote add origin git@github.com:username/username.github.io.git
```

Where ```username``` is your Github username

Essentially a Github page will display whatever HTML files are pushed up to the main branch at the URL ```username.github.io```

3.) Edit ```SITEURL``` in ```publishconf.py``` so that it is set to https://username.github.io where ```username``` is your Github username

Note: see https://docs.github.com/en/pages/quickstart

## Commiting and Deploying

1.) Always commit your changes to a development branch. If you're creating your own website, run:

```console
foo@bar:~$ git checkout -b dev
```

Then when you're ready to commit, run the usual ```git add -A```, ```git commit -m "message"```

2.) We need to add the content of the blog to the ```main``` branch for Github pages to work. Use the ```ghp-import``` for this:

```console
foo@bar:~$ ghp-import output -b main
```
to import everything in the output folder to main

3.) Finally, push your main branch to Github!

```console
foo@bar:~$ git push origin main
```

4.) Visit ```username.github.io``` to see the webpage!

Rinse and repeat when you make any changes with ```pelican content```, ```pelican -l``` to see changes in a local browser, ```ghp-import output -b main```, and ```git push origin main```

You are ready to start scaling your website with more content!!!

5.) Choosing a theme. Clone pelican-themes to your local machine with ```git clone --recursive https://github.com/getpelican/pelican-themes ~/pelican-themes```. Choose a theme from there and simplye include its location in the pelican settings file with one line:

```python
THEME = "/home/user/pelican-themes/theme-name"
```

Note: See https://github.com/getpelican/pelican-themes for more information

### Sources

https://www.dataquest.io/blog/how-to-setup-a-data-science-blog/

https://github.com/danielfrg/pelican-jupyter

https://docs.github.com/en/pages/quickstart

https://docs.getpelican.com/en/3.6.3/publish.html

https://github.com/getpelican/pelican-themes
