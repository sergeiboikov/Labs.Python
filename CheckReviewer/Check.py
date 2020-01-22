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
        self.agrmnt_claim_cds_str = self.get_agrmnt_claim_cds()

    def run_sqlplus(self, work_dir, log_file = ''):
        config = get_config(config_file)
        #run script and save output
        connect_str = get_setting(config, 'DEFAULT', 'connect_str')
        if not log_file:
            command = ['sqlplus', connect_str, '<', os.path.join(work_dir, '_run.sqlp').replace(os.getcwd() + '\\', '')]
        else:
            command = ['sqlplus', connect_str, '@' + os.path.join(work_dir, '_run.sqlp'), '>', log_file]
        print('Running script _run.sqlp')
        subprocess.call(command, stdout = subprocess.DEVNULL, shell = True)

    def transform_sql(self, fname):
        print('Prepare and run ' + fname)
        #read from file
        with open(os.path.join(self.template_dir, fname + '.sql'), 'r') as file:
            src_data = file.read()

        if fname == 'Check3':
            src_data = src_data.replace('&1', self.agrmnt_claim_cds_str)
            src_data = src_data.replace('&&patch', '_Patch\\' + fname.upper() + '.txt')

        #write into file
        with open(os.path.join(self.work_dir, fname + 'Copy.sql'), 'w') as file:
            file.write(src_data)
        with open(os.path.join(self.work_dir, '_run.sqlp'), 'w') as file:
            file.write('@' + self.work_folder + '\\' + fname + 'Copy.sql')
        self.run_sqlplus(self.work_dir)

    def get_agrmnt_claim_cds(self) -> str:
        config = get_config(config_file)
        agrmnt_claim_cds_str = get_setting(config, 'CHECKS', 'agrmnt_claim_cds_str')
        return agrmnt_claim_cds_str

def get_config(path):
    """
    return the config object
    """
    config = configparser.ConfigParser()
    config.read(path)
    return config

def get_setting(config, section, settings):
    """
    return setting
    """
    value = config.get(section, settings)
    return value

def main():
    cr = CheckReviewer()
    print(f"Начало проверки для требований {cr.agrmnt_claim_cds_str}")
    cr.transform_sql('Check3')
    print("Проверка завершена")

main()