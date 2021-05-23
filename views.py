import os

from aiohttp import web

from settings import FILES_DIR
from utils import RequestFileSaver

routes = web.RouteTableDef()

@routes.view('/images/format')
class PhotoUpdateView(web.View):

    async def post(self):
        params = dict(await self.request.post())
        if params.get('photo'):
            saver = RequestFileSaver('photo', FILES_DIR)
            filenames = await saver.save_files(self.request)

@routes.view('/photo/download/{file_name}')
class PhotoDownloadView(web.View):

    async def get(self):
        file_name = self.request.match_info['file_name']

@routes.view('')
class ReactView(web.View):

    async def get(self):
        return web.FileResponse(os.path.join(os.path.dirname(__file__), 'frontend/public/index.html'))




