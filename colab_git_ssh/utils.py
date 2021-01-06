import os
import shlex
import subprocess
import re
from typing import Dict, NoReturn

def run_shell_command(command: str): -> NoReturn
    subprocess.run(shlex.split(command))


def get_git_info(git_repo_address: str) -> Dict:
    """Returns the various parts of the git_repo_address as a dictionary.

    Example:

    get_git_info(git_repo_address="https://github.com/sugatoray/colab_git_ssh")
    """
    gitpatterns = {
        "ssh": "(git)@(.*):(.*)/(.*).git", 
        "https": "(https)://(.*)/(.*)/(.*)"
    }
    if git_repo_address.startswith("git@"):
        git_protocol = "ssh"
    elif git_repo_address.startswith("https://"):
        git_protocol = "https"
    if git_protocol in ["ssh", "https"]:
        parts = re.findall(gitpatterns[git_protocol], git_repo_address)[0]
        git_info = dict(
            host = parts[1],
            owner = parts[2],
            repo = parts[3],
            protocol = git_protocol,
            address = git_repo_address
        )
        return git_info
    else:
        raise ValueError("Non standard git_repo_address provided.")


def git_clone_repo(git_repo_address: str=None, verbose=True) -> Dict:
    """Clones a repo by the given git_repo_address. Returns the git_info as a dict.
    Supports both SSH and HTTPS protocols.
    
    Example:

    git_clone_repo(git_repo_address="https://github.com/sugatoray/colab_git_ssh")
    """
    if git_repo_address is None:
        git_repo_address = "https://github.com/sugatoray/colab_git_ssh"
    git_info = get_git_info(git_repo_address)
    if os.path.isdir(git_info["repo"]):
        #! rm -r test_private
        command = f'rm -r {git_info["repo"]}'
        run_shell_command(command)
    # git_repo_address examples:
    #   git@github.org:<git_username>/<git_repo_name>.git
    #   git@gitlab.org:<git_username>/<git_repo_name>.git
    #   git@bitbucket.org:<git_username>/<git_repo_name>.git
    # ! git clone $git_repo_address
    run_shell_command(command=f'git clone {git_repo_address}')
    
    if verbose:
        # print(f"Cloned repo: {git_repo_address} " + emoji.emojize(":fire:") * 3)
        print(f"Cloned repo: {git_repo_address} " + "🔥🔥🔥")
    return git_info


def get_githost(host: str="github.com") -> str:
    """Returns the git host for GitHub, GitLab, BitBucket.

    Parameters:

        host (str): {("gh", "github", "github.com"), 
                     ("gl", "gitlab", "gitlab.com"), 
                     ("bb", "bitbucket", "bitbucket.org")}.

                     (default: "github.com")

    Example:

    The folloing three will return: "github.com"
        get_githost(host="gh")
        get_githost(host="github")
        get_githost(host="github.com")

    The folloing three will return: "gitlab.com"
        get_githost(host="gl")
        get_githost(host="gitlab")
        get_githost(host="gitlab.com")

    The folloing three will return: "bitbucket.org"
        get_githost(host="bb")
        get_githost(host="bitbucket")
        get_githost(host="bitbucket.org")

    """
    host = host.lower() 
    if any(x in host for x in ["gh", "github", "github.com"]):
        host = "github.com"
    elif any(x in host for x in ["gl", "gitlab", "gitlab.com"]):
        host = "gitlab.com"
    elif any(x in host for x in ["bb", "bitbucket", "bitbucket.org"]):
        host = "bitbucket.org"        
    
    return host


def make_git_address(repo: str="repo", owner: str="owner", host: str="github.com", protocol: str="ssh") -> str:
    """Constructs git repo address from given components.

    Parameters:

        repo (str): git repository name. (default: "repo")
        owner (str): git repository owner-name. (default: "owner") 
        host (str): git cloud host domain. (default: "github.com")
        protocol (str): {ssh, https}. (default: "ssh")

    Example:

    For this repository: https://github.com/sugatoray/colab_git_ssh

        repo = "colab_git_ssh"
        owner = "sugatoray"
        host = "github.com"
        protocol = "https"

    For this repository: git@github.com:sugatoray/colab_git_ssh.git

        repo = "colab_git_ssh"
        owner = "sugatoray"
        host = "github.com"
        protocol = "ssh"

    """
    host = get_githost(host)    
    if protocol=="ssh":
        address = f"git@{host}:{owner}/{repo}.git"
    else:
        # protocol=="https"
        address = f"https://{host}/{owner}/{repo}"
    return address
