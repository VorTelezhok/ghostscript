# -*- mode: python ; coding: utf-8 -*-
#
# Build requirements
# - inkscape
#

# create PNG projectlogo for project homepage
Command('projectlogo.png', 'projectlogo.svg',
        'inkscape -z -f $SOURCE -e $TARGET --export-height=100')

# create PNG projectlogo for bitbucket
Command('projectlogo-35.png', 'projectlogo.svg',
        'convert  -resize 35x -crop 35x35+0+0 $SOURCE $TARGET')
