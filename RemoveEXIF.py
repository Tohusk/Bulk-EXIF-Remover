from PIL import Image
import piexif
import os

directory = input("Enter a directory:")
count = 0
for filename in os.listdir(directory):
    # jpg or tif or wav
    if filename.endswith(".jpg") or filename.endswith(".png"):
        count += 1
        image = Image.open(directory + filename)
        # only do if has exif
        if image._getexif() != None:
            exif_dict = piexif.load(image.info["exif"])
            exif_bytes = piexif.dump(exif_dict)

            # rotate accordingly
            if piexif.ImageIFD.Orientation in exif_dict["0th"]:
                orientation = exif_dict["0th"].pop(piexif.ImageIFD.Orientation)
                if orientation == 2:
                    image = image.transpose(Image.FLIP_LEFT_RIGHT)
                elif orientation == 3:
                    image = image.rotate(180)
                elif orientation == 4:
                    image = image.rotate(180).transpose(Image.FLIP_LEFT_RIGHT)
                elif orientation == 5:
                    image = image.rotate(-90, expand=True).transpose(Image.FLIP_LEFT_RIGHT)
                elif orientation == 6:
                    image = image.rotate(-90, expand=True)
                elif orientation == 7:
                    image = image.rotate(90, expand=True).transpose(Image.FLIP_LEFT_RIGHT)
                elif orientation == 8:
                    image = image.rotate(90, expand=True)

            # create empty exif data to be used as new image's exif
            empty_exif_bytes = piexif.dump({})

            # save as new image with _1 at the end
            image.save(filename.split('.')[0] + "_1." + filename.split('.')[1], exif=empty_exif_bytes, quality=95)