import os

import secrets
import hashlib

from colorblind.recolor import Core


class RequestFileSaver:

    def __init__(self, form_name, upload_folder):
        self._form_name = form_name
        self._upload_folder = upload_folder

    async def save_files(self, request):
        post = await request.post()

        images = post.getall(self._form_name, [''])
        filenames = []
        if images != ['']:
            for image in images:
                if isinstance(image, bytearray):
                    filename = secrets.token_urlsafe(64) + '.png'
                    with open(os.path.join(self._upload_folder, filename)) as f:
                        f.write(image)
                else:
                    filename = secrets.token_urlsafe(64) + '.' + image.filename.split('.')[-1]
                    with open(os.path.join(self._upload_folder, filename), 'wb') as f:
                        print(f)
                        f.write(image.file.read())
                filenames.append(os.path.join(self._upload_folder, filename))
        resp_filenames = []
        for filename in filenames:
            resp_filename = secrets.token_urlsafe(64) + '.png'
            Core.correct(filename, save_path=os.path.join(self._upload_folder,resp_filename))
            resp_filenames.append(filename)

        return filenames