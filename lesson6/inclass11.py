import sys
from datetime import datetime


d1 = datetime.strptime(sys.argv[1], '%Y-%m-%d')
d2 = datetime.strptime(sys.argv[2], '%Y-%m-%d')

date_diff = abs(d2 - d1)

print 'Total days: %s, hours: %s, minutes: %s, seconds: %s' % (date_diff.days,
                                                               (date_diff.total_seconds() / 3600),
                                                               (date_diff.total_seconds() / 60),
                                                               date_diff.total_seconds())
