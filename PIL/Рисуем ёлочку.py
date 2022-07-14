from PIL import Image, ImageDraw


def picture(file_name, width, height, sky_color='#75BBFD', snow_color='#FFFAFA', trunk_color='#A45A52',
            needls_color='#01796F', sun_color='#FFDB00'):
    im = Image.new('RGB', (width, height), sky_color)
    draw = ImageDraw.Draw(im)
    draw.ellipse((0.8 * width, -0.2 * height, 1.2 * width, 0.2 * height), sun_color)
    draw.rectangle((0, 0.8 * height, width, height), snow_color)
    draw.rectangle((0.45 * width, 0.9 * height, 0.55 * width, 0.7 * height), trunk_color)
    draw.polygon((width * 0.3, height * 0.7, width * 0.7, height * 0.7, width * 0.6, height * 0.5, width * 0.65,
                  height * 0.5,
                  width * 0.55, height * 0.3, width * 0.6, height * 0.3, width * 0.5, height * 0.1, width * 0.4,
                  height * 0.3,
                  width * 0.45, height * 0.3, width * 0.35, height * 0.5, width * 0.4, height * 0.5, width * 0.3,
                  height * 0.7), needls_color)

    im.save(file_name)


picture('Н1.png', 1000, 800)
