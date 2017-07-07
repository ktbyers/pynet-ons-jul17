#!/usr/bin/env python
import subprocess

proc = subprocess.Popen(['/bin/pwd'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# proc.communicate returns a tuple of (STDOUT, STDERR)
std_out, std_err = proc.communicate()
print
print "STDOUT: {}".format(std_out.strip())
print "STDERR: {}".format(std_err)
print
