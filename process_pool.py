import glob
import os
from PIL import Image
import concurrent.futures


def make_image_thumbnail(filename):
    # The thumbnail will be named "<original_filename>_thumbnail.jpg"
    base_filename, file_extension = os.path.splitext(filename)
    thumbnail_filename = f"{base_filename}_thumbnail{file_extension}"

    # Create and save thumbnail image
    image = Image.open(filename)
    image.thumbnail(size=(128, 128))
    image.save(thumbnail_filename, "JPEG")

    return thumbnail_filename


# Create a pool of processes. By default, one is created for each CPU in your machine.
with concurrent.futures.ProcessPoolExecutor() as executor:
    # Get a list of files to process
    image_files = glob.glob("*.jpg")

    # Process the list of files, but split the work across the process pool to use all CPUs!
    for image_file, thumbnail_file in zip(image_files, executor.map(make_image_thumbnail, image_files)):
        print(f"A thumbnail for {image_file} was saved as {thumbnail_file}")

   
 