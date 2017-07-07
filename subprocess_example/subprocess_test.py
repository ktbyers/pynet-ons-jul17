#!/usr/bin/env python
import subprocess

def main():
    """Test subprocess."""
    cmd_list = ['/bin/df', '-h']
    proc = subprocess.Popen(cmd_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (std_out, std_err) = proc.communicate()
    print
    print std_err
    print std_out
    print

if __name__ == "__main__":
    main()
