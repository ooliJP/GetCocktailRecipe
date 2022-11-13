import json
import requests
import sys
from fpdf import FPDF
from urllib.request import urlopen
from PIL import Image

class PDF(FPDF):
    def header(self):
        self.set_font("courier", "B", 35)
        width = self.get_string_width(self.title) + 6
        self.set_x((297 - width) / 2)
        self.set_text_color(0, 0, 0)
        self.cell(
            width,
            9,
            self.title,
            new_x="LMARGIN",
            new_y="NEXT",
            align="C",
        )
        self.ln(10)

def main():
        try:
            name = input("Type the name of the cocktail or just the first letter: ")
            if len(name) < 2:
                get_variants(name)
                info = get_cocktail(input("Choose one: "))
            else:
                info = get_cocktail(name)
            ingr, measures = get_ingredients(info)
            create_pdf(info, ingr, measures)
        except (TypeError):
            sys.exit("We don't have such a cocktail or you wrote the wrong name. Try again")

def get_variants(input):                #to get variants of the cocktails starting with the letter user entered
    with urlopen(f"https://www.thecocktaildb.com/api/json/v1/1/search.php?f={input}") as resp:
        source = resp.read()
        data = json.loads(source)
        print(f"Here are some cocktails starting with \"{input}\"")
        for variants in data["drinks"]:
            print(variants["strDrink"])

def get_cocktail(input_two):            #to get a JSON file of selected cocktail
    if ' ' in input_two:
        input_two = input_two.replace(' ', '%20')
    with urlopen(f"https://www.thecocktaildb.com/api/json/v1/1/search.php?s={input_two}") as resp:
        source = resp.read()
        data = json.loads(source)
        no_nulls = delete_nulls(data['drinks'][0])
        return no_nulls

def delete_nulls(info):        #to remove None values and make it easier to read
    for key, value in info.copy().items():
        if value is None:
            del info[key]
    return info

def get_ingredients(data):
    ingrs = list()
    measures = list()
    for key, value in data.items():
        if key.startswith('strIngredient'):
            ingrs.append(value)
        if key.startswith('strMeasure'):
            measures.append(value)
    return ingrs, measures

def create_pdf(info, ingr, measures):
    im = Image.open(requests.get(info['strDrinkThumb'], stream=True).raw)
    pdf = PDF('L')
    pdf.set_font("courier", size =20)
    pdf.set_title(info["strDrink"])
    pdf.add_page()
    pdf.image(im, x=10, y= 50, w=100, h=0)
    pdf.cell(0, 10, "What you will need: ", new_x="LMARGIN", new_y="NEXT", align = 'C')
    pdf.cell(0, 10, f"Glass type: {info['strGlass']}", new_x="LMARGIN", new_y="NEXT", align = 'R')
    for i in range(len(ingr)):
        if i < len(measures):
            pdf.cell(0, 10, f"{ingr[i]} - measure: {measures[i]}", new_x="LMARGIN", new_y="NEXT", align = 'R')
        else:
            pdf.cell(0, 10, f"{ingr[i]}", new_x="LMARGIN", new_y="NEXT", align = 'R')
    pdf.cell(0, 10, "Instruction: " , new_x="LMARGIN", new_y="NEXT", align = 'C')
    pdf.set_x(150)
    pdf.multi_cell(0, 10, info['strInstructions'], align = 'C')
    pdf.output("cocktail.pdf")

if __name__ == "__main__":
    main()