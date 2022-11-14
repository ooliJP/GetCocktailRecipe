
# Cocktail recipe program

  
## Description:

This is the program that can find recipes for the most popular cocktails in the world and not only find them but also create a PDF file with all information on ingredients, instructions, and even an image of the cocktail you want to make!

 ### How to use:
 1. Just run the python file and that's it!

So, when you run it, the program is going to ask you to input the first letter of the cocktail or its full name. Let's start with the first case where your input is just the first letter, because who knows maybe you want to choose your future drink just by the random interesting name or you remember only the beginning of the word. After your input, the output of the program is going to look like this:

  

for example, you typed "n":

```bash

Type the name of the cocktail or just the first letter: n

Here are some cocktails starting with "n"

Negroni

New York Sour

Nutty Irishman

National Aquarium

New York Lemonade

Nuked Hot Chocolate

Choose any one:

```

The list of cocktails starting with "n" is going to appear and you have to choose one. After this moment the rest of the program is going to be the same as if you typed full name. If you entered the wrong name of the cocktail or no drinks are starting with your letter, it will exit with sys.exit, and a message will show up:

```bash
We do not have such a cocktail or you wrote the wrong name. Try again

```

  

If everything is okay, the program will search for the necessary information in the API of this site: www.thecocktaildb.com. After receiving the JSON file, the program sorts and removes unnecessary elements, and some even copies into a separate list to make it easier to work with them. Once information is sorted and easy to read, the last function creates a PDF file which is a lot more understandable than a raw JSON file :)

  
  
  

## Installation

Just download the file called 'project.py' and install the package that helps to work with PDF files and it's done!

  

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install FPDF.

  

```bash
pip install fpdf2
```

Other packages are also used, and if they are not installed on your PC, do it the same way as FPDF. Here they are:

  

```bash
requests

urllib

Pillow
```

some of them are already built-in, so you don't have to install them.
## How to install PIL?

> Installation instructions for your OS you can find here  [https://python-pillow.github.io/](https://python-pillow.github.io/)  and here  [http://pillow.readthedocs.org/en/3.0.x/installation.html](http://pillow.readthedocs.org/en/3.0.x/installation.html)

> If you using  **Linux**:

```
sudo pip install PIL --allow-external PIL --allow-unverified PIL

```

> If you using  **Windows**: Visit this page and download installation package for your Python version  [http://www.pythonware.com/products/pil/](http://www.pythonware.com/products/pil/)

> If you using  _**MAC**_:

```
pip install PIL --allow-external PIL --allow-unverified PIL
```
