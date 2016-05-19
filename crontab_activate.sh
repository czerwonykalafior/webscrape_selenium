#!/usr/bin/env bash
# adding a cronjob
frequency="* * * * *"
display="export DISPLAY=:99"
proj_dir="/home/stiven/PycharmProjects/WebScraping02"
venv_dir="/home/stiven/.virtualenvs/WebScrpSelenium/bin/python"
scr_name="selenium_targeo_rout.py"
log="listener.log 2>&1"
(crontab -l ; echo "$frequency $display && cd $proj_dir && $venv_dir $scr_name > $log") | crontab -
# starting virtual framebuffer at display 99
x-terminal-emulator -e Xvfb :99 -ac