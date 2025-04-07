from fpdf import FPDF
import json

def generate_playing_cards(json_data, output_file="playing_cards.pdf"):
    data = json.loads(json_data)
    pdf = FPDF("P", "mm", "A4")
    pdf.set_auto_page_break(auto=False)
    
    card_width = 75
    card_height = 85
    margin_x = 10
    margin_y = 10
    space_x = 5
    space_y = 5
    page_width = 210
    page_height = 297
    
    pdf.set_font("Arial", size=12)

    for location in data["paikat"]:
        place = location["place"]
        roles = location["roles"]

        pdf.add_page()
        x_start = margin_x
        y_start = margin_y

        for role in roles:
            pdf.set_xy(x_start, y_start)
            pdf.set_fill_color(240, 240, 240)
            pdf.rect(x_start, y_start, card_width, card_height, style='DF')
            pdf.set_draw_color(0, 0, 0)
            pdf.rect(x_start, y_start, card_width, card_height, style='D')

            pdf.set_xy(x_start, y_start + 20)
            pdf.set_font("Arial", style='B', size=18)
            pdf.cell(card_width, 10, "Paikka:", ln=True, align="C")
            pdf.set_xy(x_start, y_start + 30)
            pdf.set_font("Arial", size=16)
            pdf.cell(card_width, 10, place, ln=True, align="C")

            pdf.set_xy(x_start, y_start + 50)
            pdf.set_font("Arial", style='B', size=18)
            pdf.cell(card_width, 10, "Rooli:", ln=True, align="C")
            pdf.set_xy(x_start, y_start + 60)
            pdf.set_font("Arial", size=16)
            pdf.cell(card_width, 10, role, ln=True, align="C")

            x_start += card_width + space_x
            if x_start + card_width > page_width:
                x_start = margin_x
                y_start += card_height + space_y
            if y_start + card_height > page_height - margin_y:
                x_start = margin_x
                y_start = margin_y
    
    pdf.output(output_file)

# Lue JSON-tiedosto
with open("data.json", "r", encoding="utf-8") as f:
    json_input = f.read()

generate_playing_cards(json_input)
