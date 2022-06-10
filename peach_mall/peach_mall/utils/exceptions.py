import logging

from rest_framework.views import exception_handler as drf_exception_handler
from rest_framework.response import Response
from rest_framework import status

from django.db import DatabaseError
from redis.exceptions import RedisError

# 获取在settings/dev.py这个配置文件中定义的logger，用来做日志记录
logger = logging.getLogger('django')


def exception_handler(exc, context):
    response = drf_exception_handler(exc, context)
    if response is None:
        view = context['view']
        if isinstance(exc, DatabaseError) or isinstance(exc, RedisError):
            logger.error('[%s] %s' % (view, type(exc)))
            response = Response({'message': '服务器内部错误'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return response
