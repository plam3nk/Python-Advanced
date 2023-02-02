import os


def save_extensions(dir_name, first_level=False):
    for filename in os.listdir(dir_name):
        file = os.path.join(dir_name, filename)

        if os.path.isfile(filename):
            extension = filename.split('.')[-1]
            if extension not in extensions:
                extensions[extension] = []

            extensions[extension].append(filename)
        elif os.path.isdir(filename) and not first_level:
            save_extensions(filename, first_level=True)


directory = input()

extensions = {}

save_extensions(directory)

