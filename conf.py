# PATH to blender_cave directory
blender_cave_path        = 

# Which configuration file to load when running in full Virtual Environment ?
all_config_file          = 

# Which configuration file to load when running in standalone case ?
alone_config_file        = 

# Path for temporary files
temp_path                = 

# The path of blenderplayer executable file : under Mac OS X, you should have to set this variable to the path of blenderplayer binary file
# blenderplayer_path       = ??

# PATH to the local configuration files
arguments['config-path']    = 

# Level of verbosity : debug, info, warning, error, critical
arguments['verbosity']      = 'warning'

# Do we have to clear previous log files before running BlenderCave ?
arguments['clear_previous'] = True

# Path where to put BlenderCave logs.
arguments['log-path']       = os.path.join(blender_cave_path, 'logs')

# The path where we can find some external python module. That will be append to PYTHONPATH environment variable. Usefull to set the path to VRPN module
#arguments['python_path'] = ??

# For the psExec, we must define a login and a password per computer
# windows_logins = { 'master' : {'user' : 'me', 'password' : 'my password'} }
