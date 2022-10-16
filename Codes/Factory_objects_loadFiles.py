
# a Object Factory class to load files of any extension.


class ObjectFactory:
    def __init__(self):
        self.extensions = {}

    def register_extension(self, extension, cls):
        self.extensions[extension] = cls

    def create(self, path):
        extension = path.split('.')[-1]
        if extension in self.extensions:
            return self.extensions[extension](path)
        else:
            raise ValueError('Unsupported extension')

# a class to load text files


class TextLoader:
    def __init__(self, path):
        self.path = path

    def read(self):
        with open(self.path) as f:
            return f.read()

# a class to load image files


class ImageLoader:
    def __init__(self, path):
        self.path = path

    def read(self):
        print('Reading data from an image')


if __name__ == '__main__':
    factory = ObjectFactory()
    factory.register_extension('txt', TextLoader)
    factory.register_extension('jpg', ImageLoader)

    t = factory.create('data.txt')
    print(t.read())

    i = factory.create('image.jpg')
    print(i.read())
    