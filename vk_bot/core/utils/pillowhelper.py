from PIL import Image
class Pillowhelper():
    def resize_image(input_image_path,
                 size):
        original_image = Image.open(input_image_path)
        width, height = original_image.size
        resized_image = original_image.resize(size)
        width, height = resized_image.size
        return resized_image
    def scale_image(input_image_path,width=None,
                    height=None):
        original_image = Image.open(input_image_path)
        w, h = original_image.size
        if width and height:
            max_size = (width, height)
        elif width:
            max_size = (width, h)
        elif height:
            max_size = (w, height)
        else:
            raise RuntimeError('Не передал  пральна аргументы')

        original_image.thumbnail(max_size, Image.ANTIALIAS)
        return original_image

