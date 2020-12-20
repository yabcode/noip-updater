import logging
import logging.config

LOG_LEVEL = logging.DEBUG
LOG_FORMAT_SIMPLE = '%(asctime)s %(levelname)-8s %(message)s'
LOG_FORMAT_JSON = '{' \
    '"timestamp": "%(asctime)s", ' \
    '"level": "%(levelname)s", ' \
    '"message": "%(message)s", ' \
    '"pid": %(process)d, ' \
    '"thread": %(thread)d, ' \
    '"file": "%(filename)s", ' \
    '"line": %(lineno)d}'
LOG_FORMAT = LOG_FORMAT_JSON

logging.config.dictConfig({
    'version': 1,

    # フォーマットの設定
    'formatters': {
        'my_format': {'format': LOG_FORMAT},
    },
    # ハンドラの設定
    'handlers': {
        'sh': {
            'class': 'logging.StreamHandler',
            'formatter': 'my_format',
            'level': LOG_LEVEL
        },
    },

    # ロガーの対象一覧
    'loggers': {
        'my_logger': {
            'handlers': ['sh'],
            'level': LOG_LEVEL,
            'propagate': False
        }
    }
})

LOG = logging.getLogger('my_logger')


if __name__ == '__main__':
    LOG.debug('This is DEBUG log.')
    LOG.info('This is INFO log.')
    LOG.warning('This is WARNING log.')
    LOG.error('This is ERROR log.')
    LOG.critical('This is CRITICAL log.')
