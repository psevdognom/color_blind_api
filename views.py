from aiohttp import web

from settings import FILES_DIR
from utils import RequestFileSaver

routes = web.RouteTableDef()

@routes.view('photo')
class PhotoUpdateView(web.View):

    async def post(self):
        params = dict(await self.request.post())
        if params.get('photo'):
            saver = RequestFileSaver('photo', FILES_DIR)
            filenames = await saver.save_files(self.request)


