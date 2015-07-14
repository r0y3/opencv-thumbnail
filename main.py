import os
import cv2

def crop_landscape(image, dim):
  r = (dim[0] / image.shape[0]) / (dim[0] / dim[1])
  nw = int(image.shape[1] * r)

  resized = cv2.resize(image, (nw, int(dim[1])), interpolation=cv2.INTER_AREA)

  half_width = int(dim[0]) / 2
  half_shape_width = int(resized.shape[1]) / 2

  start_x = half_shape_width - half_width
  end_x = half_width + half_shape_width
  cropped = resized[0:dim[1], start_x:end_x]

  return cropped

def crop_portrait(image, dim):
  r = dim[1] / image.shape[1] / (dim[1] / dim[0])
  nh = int(image.shape[0] * r)

  resized = cv2.resize(image, (int(dim[0]), nh), interpolation=cv2.INTER_AREA)
  half_height = int(dim[1]) / 2
  half_shape_height = int(resized.shape[0]) / 2

  start_y = half_shape_height - half_height
  end_y = half_height + half_shape_height
  cropped = resized[start_y:end_y, 0:dim[0]]

  return cropped

def create_other_size(image, file_name, dim, location):
  # 1 => width index, 0 => height index
  try:
      if image.shape[0] > image.shape[1]:
          cropped = crop_portrait(image, dim)
      else:
          cropped = crop_landscape(image, dim)

      cv2.imwrite(os.path.join(location, file_name), cropped)

  except Exception, ex:
      pass

file_name = '/home/user/picture.jpg'
output_dir = '/home/user/output/'
image = cv2.imread(file_name)
create_other_size(image, file_name, (100.0, 100.0), output_dir)
