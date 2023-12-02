import sys
import argparse
from PIL import Image, ImageDraw, ImageFont


def text_to_png(text, grid_size, image_size, font_path):
    # Load the font
    font_size = grid_size * 2 // 3
    n_rows = image_size[0] // grid_size
    n_cols = image_size[1] // grid_size
    assert len(text) <= n_rows * n_cols, "Text is too long for image size"
    font = ImageFont.truetype(font_path, font_size)

    # Create image with transparent background

    image = Image.new("RGBA", image_size, (0, 0, 0, 0))

    # Initialize drawing context
    draw = ImageDraw.Draw(image)
    draw.fontmode = "1"  # Turn off antialiasing

    # Get text size
    for i, glyph in enumerate(text):
        row = i // n_cols
        col = i % n_cols
        x = col * grid_size
        y = row * grid_size
        _, _, w, h = draw.textbbox((0, 0), glyph, font=font)
        draw.text((x + (grid_size - w) / 2, y + (grid_size - h) / 2), glyph, font=font, fill="black")

    # Apply text to image

    # Save image
    image.save("glyphs.png")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Font2PNG.')

    parser.add_argument('glyphs', help='Input glyphs which should be included')
    parser.add_argument('path', help='Input ttf file path')

    parser.add_argument('--grid-size', '-g', default=16, help='Grid size of glyph')
    parser.add_argument('--image-size', '-s', default=256, help='Size of output image')

    args = parser.parse_args()

    text_to_png(args.glyphs, args.grid_size, (args.image_size, args.image_size), args.path)
