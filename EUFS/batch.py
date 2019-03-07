import os
import glob
import sys
import PIL
import PIL.Image as Image


# sys.argv[1] will give folder directory
# sys.argv2[2] will give image type (either jpg / png / both);

if (len(sys.argv) < 2):
    print("Usage: python predict_images.py <relative path to images directory> <type of images: 'jpg' [default] or 'png'>")
    sys.exit()
if (len(sys.argv) == 3):
    type = sys.argv[2]
    if (type != 'png') or (type != 'jpg'):
        print("Invalid second argument. Expecing 'jpg' or 'png'.")
        sys.exit()
else:
    type = 'jpg'

if (sys.argv[1][-1] != '/'):
    relative_path = sys.argv[1] + '/'
else:
    relative_path = sys.argv[1]

save_folder_name = 'pred_' + relative_path.split('/')[-2]

if os.path.exists(save_folder_name):
    os.rmdir(save_folder_name)
os.makedirs(save_folder_name)

cwd = os.getcwd()
command = './darknet detector test cfg/cones-obj.data cfg/cones-obj.cfg weights/v1/yolo-cones_2000.weights ' \
          '-i 0 -thresh 0.05 -dont_show'

for filename in glob.glob(relative_path + '*.' + type):
    image_name = filename.split('/')[-1].split('.')[-2]
    os.system(command + ' ' + filename)
    os.system('mv predictions.jpg ' + save_folder_name + '/p_' + image_name + '.' + type)
    # predicted_image = Image.open(cwd + '/' + 'predictions.jpg')
    # new_filename = cwd + '/' + save_folder_name + '/p_' + image_name + '.' + type
    # predicted_image.save(new_filename)
