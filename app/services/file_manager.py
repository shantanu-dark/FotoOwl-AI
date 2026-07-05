import os
import shutil


class FileManager:

    @staticmethod
    def ensure_dir(path):
        os.makedirs(path, exist_ok=True)

    @staticmethod
    def copy_file(src, dst):
        FileManager.ensure_dir(os.path.dirname(dst))
        shutil.copy2(src, dst)

    @staticmethod
    def copy_images(image_paths, destination):

        FileManager.ensure_dir(destination)

        for image in image_paths:

            shutil.copy2(
                image,
                os.path.join(
                    destination,
                    os.path.basename(image)
                )
            )