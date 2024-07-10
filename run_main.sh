#!/bin/bash
HOME_DIR="/home/genaro"
PROJECT_DIR="/home/genaro/repos/scuba"


screen -dmS gui bash -c "exec bash"
screen -S gui -X stuff "source $HOME_DIR/.bashrc^M"
screen -S gui -X stuff "cd $PROJECT_DIR^M"
screen -S gui -X stuff "python main.py^M"

