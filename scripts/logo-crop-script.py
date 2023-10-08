import os
import argparse
from PIL import Image


def crop_transparent(img):
    # Calculate the bounding box of the non-zero regions in the image
    bbox = img.getbbox()
    return img.crop(bbox)


def resize_and_pad(img, size):
    # Determine the aspect ratio
    aspect = img.width / img.height
    new_width = size
    new_height = size

    # Maintain the aspect ratio
    if aspect > 1:  # Width > height
        new_height = round(size / aspect)
    elif aspect < 1:  # Height > width
        new_width = round(size * aspect)

    img = img.resize((new_width, new_height), Image.LANCZOS)

    new_img = Image.new(
        "RGBA", (size, size), (0, 0, 0, 0)
    )  # create a transparent image
    new_img.paste(img, ((size - new_width) // 2, (size - new_height) // 2))

    return new_img


def main(folder_path, output_folder, new_size):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(folder_path):
        if filename.endswith(".png"):
            img_path = os.path.join(folder_path, filename)
            img = Image.open(img_path).convert("RGBA")  # retain transparency

            # Crop the image to non-transparent area
            img = crop_transparent(img)

            # Resize and pad image to square
            img = resize_and_pad(img, new_size)

            # Save the image
            img.save(os.path.join(output_folder, filename))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process images.')
    parser.add_argument('--input_folder', type=str, default="assets/to_convert", help='Path of the folder containing images.')
    parser.add_argument('--output_folder', type=str, default="assets/converted", help='Output folder for the images.')
    parser.add_argument('--size', type=int, default=1200, help='New size of images.')
    args = parser.parse_args()
    main(args.input_folder, args.output_folder, args.size)
