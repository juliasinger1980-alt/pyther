from PIL import Image, ImageDraw, ImageFont
chars = []
dick = {}
fontsize = 4
if __name__ == "__main__":
    for y in range(32, 127):
        i = Image.new("RGB", [15, 15], "black")
        x = ImageDraw.Draw(i)
        x.text([1,1], chr(y), "white")
        c = i.get_flattened_data()
        dings = 0
        for s in c:
            if sum(s) > 0:
                dings += 1
        dick[chr(y)] = dings
    sortiert = sorted(dick.items(), key=lambda x: x[1])
    chars.append(sortiert)
    
    s = Image.new("RGB", [955, 14], "black")
    u = ImageDraw.Draw(s)
    counter = 1
    for zeichen, helligkeit in sortiert:
        u.text([counter,1], zeichen, "white")
        counter += 10
    s.show()
    s.save("font_atlas.png")