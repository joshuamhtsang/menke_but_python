# menke_but_python
Implementation and hacking the algorithms in the book 'Environmental Data Analysis with MATLAB', but in Python instead


# Setup: Windows 11, VS Code, Python, VS Code Python Extension, Venv Setup

Here is some guidance on how to set up Python development in Windows. The basic requirements are to install the 3 components listed in this [guide](https://code.visualstudio.com/docs/python/python-tutorial):

1. VS Code
2. Python binary (https://www.python.org/downloads/)
3. VS Code Python Extension (Extension ID: ms-python.python): Use 'ctrl+shift+x' to search for this extension.

The guide also shwos you how to use Venv Virtual Environments.  Once Venv is setup (you see a .venv directory), you can spawn the VS Code Terminal and you'll see it automatically do the 'source' action:

$ source <path_to_activate>

and you can use 'pip install' as usual, for example:

$ pip install numpy


# Setup: github, git, ssh git clone

I use gitbash on Windows.  'git' is already installed.  Generate a new SSH key:

$ ssh-keygen.exe

Add a passcode, preferably. Add the public key to your github's 'SSH and GPG keys' settings. Now use VS Code's 'Source Control' panel to 'clone' the repo into the directory of your choice.





