# ansible_shell
A (mostly unneccesary) shell for ansible.
  * Run adhoc commands as well as playbooks
  * Create aliases/macros to simplify commands
  * Switch between ansible projects (if set in the config file).
  * View ansible configs
  * View ansible inventory
  * List plugins, view plugin documentaion
  * Run shell commands inline
  * Run an ipython or python shell without exiting the shell or opening a seperate terminal
  * Change settings on the fly (debug, foreground color, etc)
  * Edit files without exiting the shell

Optional support files:

    Config file: ~/.anssh.cfg
        [DEFAULT]
        allow_style = {Never | Terminal | Always}
        editor = {vim, nano, etc}
        pager = {less, more, etc)
        foreground_color = {color}
        timing = True/False
        ansible_directory = /path/to/ansible/directory
        ansible_inventory = name_of_inventory
        ansible_projects = ProjectName1 ProjectName2

        [ProjectName1]
        ansible_directory = /path/to/ansible/directory
        ansible_inventory = hosts

        [ProjectName2]
        ansible_directory = /path/to/ansible/directory
        ansible_inventory = inventory

    Startup Script (permanently set aliases, etc): ~/.anssh.rc
        alias create {alias_name} {command}
        alias create show_log !cat "log file.txt"
        alias create save_results print_results ">" out.txt
        macro create {name} {command} "{1}" "|" {cmd}
        macro create lc ~cat "{1}" "|" less

ansible_shell requires some modules you might not have installed, but can attempt to install them for you - or you can handle it yourself (ansible_shell will list which modules are missing)


