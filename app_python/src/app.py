from aiohttp import web
from time_provider import TimeProvider
from html_wrapper import HtmlWrapper


async def get_current_datetime(request):
    time = str(TimeProvider.get_current_datetime())
    html = HtmlWrapper.align_content_to_center(time)

    return web.Response(text=html, content_type='text/html')

app = web.Application()

app.add_routes([web.get('/', get_current_datetime)])

if __name__ == '__main__':
    web.run_app(app, host='0.0.0.0', port='8080')
