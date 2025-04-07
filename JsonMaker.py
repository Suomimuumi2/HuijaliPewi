import json

def convert_to_json(input_file, output_file):
    result = []

    with open(input_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    for line in lines:
        if ":" in line:
            place_part, roles_part = line.strip().split(":", 1)
            place = place_part.strip()
            roles = [role.strip() for role in roles_part.split(",") if role.strip()]
            result.append({
                "place": place,
                "roles": roles
            })

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False)

    print(f"Converted {input_file} to {output_file}")

# Käyttöesimerkki:
convert_to_json("input.txt", "output.json")
