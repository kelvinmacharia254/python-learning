#!/usr/bin/env python3

"""Report the application's run mode.

Reads APP_MODE from the environment (defaults to 'unset' if it is not
exported), prints it, and exits with status 0.
"""

import os
import sys

APP_MODE=os.getenv('APP_MODE','unset')
print(f"Running mode:{APP_MODE}")
sys.exit(0)
