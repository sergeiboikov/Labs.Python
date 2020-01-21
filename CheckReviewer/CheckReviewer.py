import os
import re
import subprocess
import configparser
import sys
from datetime import datetime
from distutils import dir_util
import shutil

template_dir = os.path.join(os.getcwd(), 'templates')
config_file = 'config.ini'
outdir = os.path.join(os.getcwd(), '_Result')

class CheckReviewer:
    work_folder = 'workfolder'

    work_dir = os.path.join(os.getcwd(), work_folder)

    def __init__(self):
        self.template_dir = template_dir
        self.agrmnt_claim_cds_str = self.get_agrmnt_claim_sds()

    def run_sqlplus(seld, work_dir, log_file = ''):
        config = get_config(config_file)
        #run script and save output
        conndect_str = get_setting(config, 'DEFAULT', 'connect_str')
        if not log_file:
            command = ['sqlplus', connect_str, '<', os.path.join(work_dir, '_run.sqlp').replace(os.getcwd() + '\\', '')]
        else:
            command = ['sqlplus', connect_str, '@' + os.path.join(work_dir, '_run.sqlp'), '>', log_file]
        print('Running script _run.sqlp')
        subprocess.call(command, stdout = subprocess.DEVNULL, shell = True)

    def transform_sql(self, fname):
        print('Prepare and run ' + fname)
        #read from file
        with open(os.path.join(self.))