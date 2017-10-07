#radial node - custom knob#
radialcustom_util='''
softness 0
addUserKnob {20 Radius}
addUserKnob {22 squareexpr l "inject radius expr" T "this=nuke.thisNode()\nradius=this.knob('radius')\nx1='-radius+shift.x'\nx2='(-radius2*pixel_aspect)+shift.y'\nx3='radius+shift.x'\nx4='(radius2*pixel_aspect)+shift.y'\nthis.knob('area').setExpression(x1,0)\nthis.knob('area').setExpression(x2,1)\nthis.knob('area').setExpression(x3,2)\nthis.knob('area').setExpression(x4,3)" -STARTLINE}
addUserKnob {22 linkhv l " link hv " T "this=nuke.thisNode()\nthis.knob('radius2').setExpression('useaspect?radius/pixel_aspect:radius')" }
addUserKnob {22 unlinkhv l " unlink hv " -STARTLINE T nuke.thisNode().knob('radius2').clearAnimated()}
addUserKnob {26 "" +STARTLINE}
addUserKnob {7 radius l "radius h" R 0 2000}
radius 200
addUserKnob {7 radius2 l "radius v" R 0 2000}
radius2 {{useaspect?radius/pixel_aspect:radius}}
addUserKnob {12 shift l center}
addUserKnob {22 setcenterinput l " input center " -STARTLINE T "this=nuke.thisNode()\nif this.input(0) :\n        x=this.input(0).width()/2\n        y=this.input(0).height()/2\nelse:\n        x=nuke.root().width()/2\n        y=nuke.root().height()/2\nthis.knob('shift').clearAnimated()\nthis.knob('shift').setValue(\[x,y])"}
addUserKnob {22 setcenterinputexpr l " input center expr " -STARTLINE T "this=nuke.thisNode()\nx='input.width/2'\ny='input.height/2'\nthis.knob('shift').setExpression(x,0)\nthis.knob('shift').setExpression(y,1)\n"}
addUserKnob {22 setcenterroot l " root center " -STARTLINE T "this=nuke.thisNode()\nx=nuke.root().width()/2\ny=nuke.root().height()/2\nthis.knob('shift').clearAnimated()\nthis.knob('shift').setValue(\[x,y])"}
addUserKnob {6 useaspect l "use pixel aspect" +STARTLINE}
useaspect 1
area {-radius+shift.x (-radius2*pixel_aspect)+shift.y radius+shift.x (radius2*pixel_aspect)+shift.y}
'''

