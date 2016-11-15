import logging
logging.basicConfig(filename='swarm_test.log', filemode='w', format='%(asctime)s %(levelname)s:%(message)s',level=logging.INFO)

log = logging.getLogger(__name__)

log.debug('Very granular logging message, useful for debuggin.')
log.info('Simple update on normal execution, e.g. "Processing record {} of {}"'. format(10,100))
log.warning('You\'ve seen these in sklearn, warning about methods being deprecated')
log.error('Logs an error message')
log.critical('Well this is an issue')


