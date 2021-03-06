import os
import sys
from main_helper import *

from dotenv import load_dotenv


class PsalmModule:

    def init_composer(self, p_dir):
        init_comp_cmd = "cd " + p_dir + " && " + "./vendor/bin/psalm.phar --init"
        try:
            os.system(init_comp_cmd)
            init = True
        except Exception:
            print("Can't init psalm")
            sys.exit()

        return init

    def download_psalm_to_project(self, p_dir):
        wget_cmd = "cd " + p_dir + " && " + "wget https://github.com/vimeo/psalm/releases/latest/download/psalm.phar -O " + str(
            p_dir)
        try:
            os.system(wget_cmd)
            downloaded = True
        except Exception:
            print("Can't download phar to project directory")
            sys.exit()

        return downloaded

    def download_composer(self, p_dir):
        download_comp_cmd = "cd " + p_dir + " && " + "composer require --dev psalm/phar"
        try:
            os.system(download_comp_cmd)
            dl = True
        except Exception:
            print("Cannot download composer to project directory")
            sys.exit()

        return dl

    def run_psalm_scan(self, p_dir, p_name):
        psalm_cmd = "cd " + p_dir + " && " + " ./vendor/bin/psalm.phar --taint-analysis " + "--report=" + "./" + p_name + ".txt"  # Focus on security with --taint-analyis
        try:
            os.system(psalm_cmd)
            insert_log_file(p_name, str(p_dir + "/" + p_name + ".txt"))
        except Exception:
            print("Error while running psalm")
            sys.exit()
        finally:
            return True
