# Copyright (C) 2010-2013 Cuckoo Sandbox Developers.
# This file is part of Cuckoo Sandbox - http://www.cuckoosandbox.org
# See the file 'docs/LICENSE' for copying permission.

import os
import re
import time
import logging
import subprocess
import os.path
try:
    import paramiko
except (CuckooDependencyError, ImportError) as e:
    sys.exit("ERROR: Missing dependency: %s" % e)

from lib.cuckoo.common.abstracts import NestManager
from lib.cuckoo.common.exceptions import CuckooCriticalError
from lib.cuckoo.common.exceptions import CuckooMachineError

log = logging.getLogger(__name__)

class Linux(NestManager):
    """Virtualization layer for Linux."""

    # states.
    SAVED = "saved"
    RUNNING = "running"
    POWEROFF = "poweroff"
    ABORTED = "aborted"
    ERROR = "machete"

    def run(self,label, command):
        """run 
        Execute this command on the nest"""
        if command:
            stdin, stdout, stderr = self.connections[label].exec_command(command)
            stdin.close()
            for line in stdout.read().splitlines():
                print 'host: %s: %s' % (label, line)

    def close(self):
        self.connection.close()


    def _initialize_check(self):
        """Runs all checks when a machine manager is initialized.
        @raise CuckooMachineError: if VBoxManage is not found.
        """
        pass

    def start(self, label):
        """Start a virtual machine.
        @param label: virtual machine name.
        @raise CuckooMachineError: if unable to start.
        """
        log.debug("Starting nest %s" % label)

        # Here we should get the ssh connection to the nest.
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            nest_ip = self.get_ip(label)
            nest_username = self.get_username(label)
            nest_password = self.get_password(label)
            client.connect(nest_ip, username=nest_username, password=nest_password)
            self.connections[label] = client

        except KeyboardInterrupt:
            return

        



    def stop(self, label):
        """Stops a virtual machine.
        @param label: virtual machine name.
        @raise CuckooMachineError: if unable to stop.
        """
        log.debug("Stopping nest %s" % label)


    def _list(self):
        """Lists virtual machines installed.
        @return: virtual machine names list.
        """
        pass

    def _status(self, label):
        """Gets current status of a vm.
        @param label: virtual machine name.
        @return: status string.
        """
        pass

    def dump_memory(self, label, path):
        """Takes a memory dump.
        @param path: path to where to store the memory dump.
        """
        pass
