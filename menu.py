# Python
import pixelfudger
import AnimationMaker
import h_viewerShortcuts # hagbarth viewer shortcuts
nuke.load("cradial.py")

# Gizmos
toolbar = nuke.toolbar("Nodes")

## Damian Binder Tools
m = toolbar.addMenu("DamianBinder", icon="DamianBinderNukeLogo.png")
m.addCommand("HeatWave", "nuke.createNode(\"HeatWave\")", icon="HeatWave_Icon.png")

## Claystudio
m=toolbar.addMenu('claystudiofx',icon="claystudiofx.png")
m.addCommand("Draw/cbar", "nuke.createNode('cbar')")
m.addCommand("Draw/cring", "nuke.createNode('cring','shift {'+str(nuke.selectedNodes()[0].width()/2 if nuke.selectedNodes() else nuke.root().width()/2)+' '+str(nuke.selectedNodes()[0].height()/2 if nuke.selectedNodes() else nuke.root().height()/2)+'}',True)")
m.addCommand("Draw/cpie", "nuke.createNode('cpie')")
m.addCommand("Draw/cradial", "nuke.createNode('Radial',radialcustom_util+'shift {'+str(nuke.selectedNodes()[0].width()/2 if nuke.selectedNodes() else nuke.root().width()/2)+' '+str(nuke.selectedNodes()[0].height()/2 if nuke.selectedNodes() else nuke.root().height()/2)+'}',True)")

## Ramps/Gradients
m=toolbar.addMenu("Draw")
m.addCommand('RampColor', "nuke.createNode('RampColor')")
m.addCommand("Grad_CB", "nuke.createNode('Grad_CB')", icon="GradCB.png")

## X_Tools
m = toolbar.addMenu("X_Tools", icon="X_Tools.png")
m.addCommand("X_Distort", "nuke.createNode(\"X_Distort\")", icon="X_Distort.png")
m.addCommand("X_Tesla", "nuke.createNode(\"X_Tesla\")", icon="X_Tesla.png")

## Others
m=toolbar.addMenu("Extra")
m.addCommand("Guides", "nuke.createNode('Guides')")
m.addCommand("Wipe", "nuke.createNode('Wipe')")
m.addCommand('WrapAround', "nuke.createNode('WrapAround')")