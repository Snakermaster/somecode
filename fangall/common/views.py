"""
视图函数
"""
from urllib.parse import quote

from django.db import transaction
from django.http import HttpResponse, StreamingHttpResponse, FileResponse

from common.captcha import Captcha
from common.utils import gen_captcha_text


@transaction.atomic
def foo(request):
    pass


def download_file(request):
    file_stream = open("/Users/Hao/Downloads/身体健康管理系统.pdf", "rb")
    file_iter = iter(lambda: file_stream.read(512), b'')
    # openpyxl / reportlab
    # 生成CSV报表、Excel报表、Pdf报表也是按照下面的方式去处理
    # 如果报表或者文件的二进制数据体积较大那么最好用迭代器进行处理避免过多的占用服务器内存
    resp = StreamingHttpResponse(file_iter)
    filename = quote('身体健康管理系统.pdf', 'utf-8')
    # resp = FileResponse(file_iter, as_attachment=True, filename=filename)
    resp['Content-Type'] = 'application/pdf'
    resp['Content-Disposition'] = f'attachment; filename="{filename}"'
    return resp


def get_captcha(request):
    captcha_text = gen_captcha_text()
    image_bytes = Captcha.instance().generate(captcha_text)
    request.session['captcha'] = captcha_text.lower()
    return HttpResponse(image_bytes, content_type='image/png')
