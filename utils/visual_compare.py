from PIL import Image, ImageChops

def compare_images(baseline, current, diff_path):
    image1 = Image.open(baseline)
    image2 = Image.open(current)
    diff = ImageChops.difference(image1, image2)

    if diff.getbbox():
        diff.save(diff_path)
        return False
    return True
