# Change default project settings
## Project Settings > Default format: HD 1280x720
nuke.knobDefault("Root.format", "HD_720")
## Project Settings > Default frame rate: 30fps
nuke.knobDefault("Root.fps", "30")

# Gizmos
nuke.pluginAddPath('./gizmos')

# Icons
nuke.pluginAddPath('./icons')

# Python scripts
nuke.pluginAddPath('./python')