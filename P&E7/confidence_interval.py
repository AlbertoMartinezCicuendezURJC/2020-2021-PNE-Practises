import Variance
import termcolor
from scipy.stats.distributions import chi2

SAMPLE = 100
CONFIDENCE_LEVEL = 99
SIGNIFICANCE_LEVEL = (100 - CONFIDENCE_LEVEL)
FREEDOOM_DEGREES = SAMPLE - 1
ALPHA = SIGNIFICANCE_LEVEL / 100
ALPHA_2 = 1 - ALPHA/2
ALPHA_3 = ALPHA/2

termcolor.cprint('The freedoom degree is:', 'cyan')
print(FREEDOOM_DEGREES)

termcolor.cprint('===========================================', 'green')

termcolor.cprint('Alpha is:', 'cyan')
print(ALPHA)

termcolor.cprint('===========================================', 'green')

termcolor.cprint('1-Alpha/2 is', 'cyan')
print(ALPHA_2)

termcolor.cprint('===========================================', 'green')

termcolor.cprint('Alpha/2 is', 'cyan')
print(ALPHA_3)

termcolor.cprint('===========================================', 'green')

CRITICAL_VALUE_1 = chi2.ppf(ALPHA_2, df=FREEDOOM_DEGREES)
CRITICAL_VALUE_2 = chi2.ppf(ALPHA_3, df=FREEDOOM_DEGREES)

FIRST_VALUE_INTERVAL = FREEDOOM_DEGREES * Variance.sample_variance / CRITICAL_VALUE_1
SECOND_VALUE_INTERVAL = FREEDOOM_DEGREES * Variance.sample_variance / CRITICAL_VALUE_2

termcolor.cprint('The first value of the interval is:', 'magenta')
print(FIRST_VALUE_INTERVAL)

termcolor.cprint('===========================================', 'green')

termcolor.cprint('The second value of the interval is:', 'magenta')
print(SECOND_VALUE_INTERVAL)

termcolor.cprint('===========================================', 'green')

termcolor.cprint('The process is under control as the variance is between 0.33 and 0.66 (lower than 0.75)', 'yellow')
