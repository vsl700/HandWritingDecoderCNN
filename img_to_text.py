from PIL import Image, ImageFont


def convert(text: str, font_filepath: str):
    font_size = 36
    # font_filepath = "fonts/sofiapro-light.otf"
    color = (255, 255, 255, 255)

    font = ImageFont.truetype(font_filepath, size=font_size)
    mask_image = font.getmask(text, "L")
    img = Image.new("RGBA", mask_image.size)
    img.im.paste(color, (0, 0) + mask_image.size, mask_image)  # need to use the inner `img.im.paste` due to `getmask` returning a core
    # img.save("yes.png")
    return img


convert("Hello world", "fonts/VeganStylePersonalUse-5Y58.ttf").save("imgs/yes.png")
