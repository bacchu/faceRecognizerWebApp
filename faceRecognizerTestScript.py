import argparse
from imutils import paths
import facevector_generator


ap = argparse.ArgumentParser()

ap.add_argument("-i", "--dataset", required=True,
                help="path to input directory of images")

args = vars(ap.parse_args())

image_paths = list(paths.list_images(args["dataset"]))

file = open('face_existence_data.txt', 'w')

for (i, image_path) in enumerate(image_paths):
    print("[INFO] processing image {}/{}".format(i + 1,
                                                 len(image_paths)))
    image_data = facevector_generator.generate_vector(image_path)

    if len(image_data) == 0:
        print("FALSE: Face not found in {}".format(image_path), file=file)
    else:
        print("TRUE: Face found in {}".format(image_path), file=file)

print("Image processing completed. Output data is in {}".format(file.name))

file.close()
