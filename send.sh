#!/bin/bash

rsync -av --delete --exclude .direnv --exclude .git . robo@roboberry.local:robocup2025_raspberrypi_fetch_picture