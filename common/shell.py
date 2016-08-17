from subprocess import STDOUT
from subprocess import check_output
from subprocess import TimeoutExpired

def execute(cmd, timeout=5):
    try:
        output = check_output(cmd, stderr=STDOUT, timeout=timeout, shell=True)
        return output
    except TimeoutExpired:
        return False
