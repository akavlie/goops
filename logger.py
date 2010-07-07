import logging
import logging.handlers

log = logging.getLogger('goops')
log.setLevel(logging.INFO)
log.addHandler(logging.handlers.SysLogHandler(address='/dev/log'))
