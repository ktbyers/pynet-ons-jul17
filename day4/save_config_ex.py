#!/usr/bin/env python
"""
Assumes 'git init' is already done on ~/CFGS directory.
git add *.cfg
git commit -m "Add configs"
"""
import subprocess
import os
from datetime import datetime
from email_helper import send_mail

GIT = '/usr/bin/git'
CFGS_DIR = '/home/kbyers/CFGS'

def subprocess_handler(cmd_list):
    proc = subprocess.Popen(cmd_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (std_out, std_err) = proc.communicate()
    if std_err:
        print std_err
    return std_out

def email_handler(message):
    sender = 'twb@twb-tech.com'
    recipient = 'ktbyersx@gmail.com'
    subject = 'Network device changes (pynet-nov-ons)'
    send_mail(recipient, subject, message, sender)
    print 'Email notification sent to {}'.format(recipient)

def main():
    os.chdir(CFGS_DIR)
    git_add = [GIT, 'add', '*.cfg']
    std_out = subprocess_handler(git_add)
    commit_str = "Add configs ({})".format(datetime.now())
    git_commit = [GIT, 'commit', '-m', commit_str]
    git_status = subprocess_handler(git_commit)
    if 'nothing to commit' in git_status:
        print "No changes...exiting."
        return 0
    git_changes = [GIT, 'log', '-p', '-1']
    router_changes = subprocess_handler(git_changes)
    email_handler(router_changes)

if __name__ == "__main__":
    main()
