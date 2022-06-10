import logging

from rest_framework.views import exception_handler as drf_exception_handler
from rest_framework.response import Response
from rest_framework import status

from django.db import DatabaseError
from redis.exceptions import RedisError

# 获取在settings/dev.py这个配置文件中定义的logger，用来做日志记录
logger = logging.getLogger('django')


def exception_handler(exc, context):
    # 调用DRF默认的exception_handler方法对异常进行处理
    # 如果异常处理成功，则会返回一个Response类型的对象
    response = drf_exception_handler(exc, context)
    # 当response为None时，说明mysql连接或者redis连接异常了；
    # 这种异常不在DRF框架自带的异常处理范围；此时可以在这里对异常进行统一处理（报错信息写入到日志文件）
    if response is None:
        # 当前处理异常的view的信息
        view = context['view']
        if isinstance(exc, DatabaseError) or isinstance(exc, RedisError):
            logger.error('[%s] %s' % (view, type(exc)))
            response = Response({'message': '服务器内部错误'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return response
