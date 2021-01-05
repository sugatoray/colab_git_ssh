import os
import shlex
import subprocess

def setup_ssh(ssh_keys_dir: str):
    ## Only update SSH_KEYS_DIR
    # 
    #  This should be some Google Drive folder that 
    #  contains you SSH public and private keys to 
    #  - GitHub
    #  - GitLab
    #  - BitBucket
    #  - Or, some other Git cloud-provider. 
    
    #################### DONOT CHANGE ANYTHING BELOW ####################

    SSH_DIR_PATH = "~/.ssh" # DONOT CHANGE THIS
    CGS_REPO_NAME = "colab_git_ssh" # CGS: Colab-Git-SSH
    CGS_REPO_OWNER = "sugatoray"
    COLAB_GIT_SSH_REPO = f"https://github.com/{CGS_REPO_OWNER}/{CGS_REPO_NAME}"

    def section_seperator(N=60, section_seperator_pattern="-"):
        return f"{section_seperator_pattern}" * N

    sep = section_seperator(N=60, section_seperator_pattern="-")

    print(f'Machine user: {os.environ["HOME"]}')
    print(sep)

    # Clone colab_git_ssh repo
    # ! git clone git@github.com:sugatoray/colab_git_ssh.git 
    # ! git clone https://github.com/sugatoray/colab_git_ssh.git
    print("\n" + f"Cloning repo: {COLAB_GIT_SSH_REPO}")
    print(sep)
    #! git clone git@github.com:$CGS_REPO_OWNER/$CGS_REPO_NAME.git
    command = f"git clone f{COLAB_GIT_SSH_REPO}.git" # use https to clone this repo
    subprocess.run(shlex.split(command))

    # Create .ssh directory and fill contents
    print("\n" + f"Creating SSH Directory: {SSH_DIR_PATH}")
    print(sep)
    #! mkdir -p $SSH_DIR_PATH # ~/.ssh
    command = f"mkdir -p {SSH_DIR_PATH}"
    subprocess.run(shlex.split(command))
    print("\n" + "Creating empty 'known_hosts' file.")
    print(sep)
    #! touch $SSH_DIR_PATH/known_hosts # ~/.ssh/known_hosts
    command = f"touch {SSH_DIR_PATH}/known_hosts"
    subprocess.run(shlex.split(command))

    # Copy Public and Private keys to ~/.ssh/
    print("\n" + f"Copying your public and private keys to {SSH_DIR_PATH}...")
    print(sep)
    #! cp $ssh_keys_dir/id_rsa* $SSH_DIR_PATH/
    command = f"cp {ssh_keys_dir}/id_rsa* {SSH_DIR_PATH}/"
    subprocess.run(shlex.split(command))
    print("DONE!")

    # Copy config and ssh_setup files to their respective destinations
    print("\n" + f"Copying ssh config to: '{SSH_DIR_PATH}/config' ...")
    print(sep)
    #! cp /content/$CGS_REPO_NAME/$CGS_REPO_NAME/config $SSH_DIR_PATH/config
    command = f"cp /content/{CGS_REPO_NAME}/{CGS_REPO_NAME}/config {SSH_DIR_PATH}/config"
    subprocess.run(shlex.split(command))
    print("DONE!")
    print("\n" + f"Creating ssh-setup file: '~/.ssh_setup' ...")
    print(sep)
    #! cp /content/$CGS_REPO_NAME/$CGS_REPO_NAME/ssh_setup.sh ~/.ssh_setup
    command = f"cp /content/{CGS_REPO_NAME}/{CGS_REPO_NAME}/ssh_setup.sh ~/.ssh_setup"
    subprocess.run(shlex.split(command))
    print("DONE!")

    # Set file permissions
    print("\n" + "Setting file permisions...")
    print(sep)
    #! bash ~/.ssh_setup
    command = f"bash ~/.ssh_setup"
    subprocess.run(shlex.split(command))
    print("DONE!")

    print("\n" + "SSH Setup completed!")
    print(sep)

    print("\n" + f"Show contents of SSH Directory: {SSH_DIR_PATH}")
    print(sep)
    #! ls -la $SSH_DIR_PATH/
    # command  = f"ls -la {SSH_DIR_PATH}/"
    # subprocess.run(shlex.split(command))
    for f in os.listdir(SSH_DIR_PATH):
        print(f)

    # Now check ssh connection
    # print("\n" + f"Check SSH connection status")
    # print(sep)
    # ! ssh github.com 
    # ! ssh gitlab.com
