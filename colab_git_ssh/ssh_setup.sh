#!/bin/bash
## %%writefile ~/.ssh_setup

##################################### FILE INFO #####################################
## FILENAME: ~/.ssh_setup
## OBJECTIVE:
##   Sets SSH permission
##    - ~/.ssh folder:          700  (WHERE? SERVER/CLIENT)
##    - public-keys:            644  (pattern: "id_rsa.*\.pub"; ending in ".pub")
##    - private-keys:           600  (pattern: "id_rsa.*" BUT WITHOUT ".pub")
##    - authorized_keys file:   600  (WHERE? SERVER)
##    - other files:            700  (example: "config", "known_hosts")
##
##################################### FILE INFO #####################################


################################# To RUN THIS FILE ##################################
## cd ~
## bash ~/.ssh_setup
################################# To RUN THIS FILE ##################################


############################## BEGIN PERMISSION UPDATE ##############################

## A. Set PERMISSION
#       FOR: SSH directory
#       TO: 700
chmod 700 ~/.ssh

## B. Go into SSH directory
cd ~/.ssh

## C. Set PERMISSION
#       FOR: ALL private-key files
#       TO: 600
#       PATTERN: "id_rsa.*" BUT NOT CONTAINING ".pub"
chmod 600 $(ls | grep -v ".*\.pub" | grep "id_rsa.*")

## D. Set PERMISSION
#       FOR: ALL public-key (*.pub) files
#       TO: 644
#       PATTERN: "id_rsa.*\.pub"
chmod 644 $(ls | grep "id_rsa.*\.pub")

## E. Set PERMISSION
#       FOR: ANY other file
#       TO: 700
#       PATTERN: NOT "id_rsa.*"
#  Use the following pattern based chmod
#  expression carefully and selectively:
#  >>> chmod 700 $(ls | grep -v "id_rsa.*")
chmod -f 700 config || true
chmod -f 700 known_hosts || true


## F. Set PERMISSION
#       FOR: "authorized_keys" file (on **SERVER**)
#       TO: 600
chmod -f 600 authorized_keys || true

############################### END PERMISSION UPDATE ###############################


##################################### REFERENCES ####################################
##
## 1. For (E, F): https://unix.stackexchange.com/a/193282/390882
## 2. For (C): https://stackoverflow.com/a/4538335/8474894
## 3. For grep: https://www.cyberciti.biz/faq/grep-regular-expressions/
##
##################################### REFERENCES ####################################
