# See http://code.google.com/p/python-nose/issues/detail?id=373
# The code below enables nosetests to work with i18n _() blocks

import __builtin__
import sys
import os
from ConfigParser import MissingSectionHeaderError

from swift.common.utils import readconf

setattr(__builtin__, '_', lambda x: x)

def get_config():
    config_file = os.environ.get('SWIFT_TEST_CONFIG_FILE',
                                 '/etc/swift/func_test.conf')
    config = {}
    try:
        config = readconf(config_file, 'func_test')
    except SystemExit:
        print >>sys.stderr, 'UNABLE TO READ FUNCTIONAL TESTS CONFIG FILE'
    except MissingSectionHeaderError:
        # rather than mock the stream to spoof a section header, display an
        # error to the user and let them fix it.
        print >>sys.stderr, 'UNABLE TO READ FUNCTIONAL TESTS CONFIG FILE ' \
                'DUE TO NO [func_test] SECTION'
    return config

