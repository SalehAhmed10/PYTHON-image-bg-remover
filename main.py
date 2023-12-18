# import glob
# from rembg import remove

# # input_path = 'input/sample.jpg'
# # output_path = 'output/sample.png'
# output_dir = 'output/'



# # with open(input_path, 'rb') as i:
# #     with open(output_path , 'wb') as o:
# #         input = i.read()
# #         output = remove(input)
# #         o.write(output)

# # For multiple files

# for file in glob.glob('*.jpg'):
#     print(file)
#     input_path = file
#     ## output_path = f"{file.replace in output_dir}"
#     output_path = f"{output_dir}{file.replace('.jpg', '.png')}"

#     with open(input_path, 'rb') as i:
#         with open(output_path, 'wb') as o:
#             input = i.read()
#             output = remove(input)
#             o.write(output)


import glob
import os
from rembg import remove

input_dir = 'input/'
output_dir = 'output/'

# Create directories if they don't exist
if not os.path.exists(input_dir):
    os.makedirs(input_dir)

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# For multiple files
for file in glob.glob(f'{input_dir}*.jpg'):
    # print remove background for each file
    print(f"Removing background for {file}...")
    input_path = file
    output_path = f"{output_dir}{os.path.basename(file).replace('.jpg', '.png')}"

    with open(input_path, 'rb') as i:
        with open(output_path, 'wb') as o:
            input_img = i.read()
            output = remove(input_img)
            o.write(output)