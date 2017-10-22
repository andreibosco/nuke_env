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

## DBTools
m = toolbar.addMenu("DB Tools", icon="DBTools_menu_icon.png")
m.addCommand("DBT_DiMisplacement", "nuke.createNode('DBT_DiMisplacement')")
m.addCommand("DBT_TextureOffset", "nuke.createNode('DBT_TextureOffset')")
m.addCommand("DBT_UVunwrapper", "nuke.createNode('DBT_UVunwrapper')")

## Others
m=toolbar.addMenu("Extra")
m.addCommand("Guides", "nuke.createNode('Guides')")
m.addCommand("Wipe", "nuke.createNode('Wipe')")
m.addCommand('WrapAround', "nuke.createNode('WrapAround')")
m.addCommand('Offset', "nuke.createNode('Offset')")
# m.addCommand('RepTile', "nuke.createNode('RepTile')")
m.addCommand('glitch', "nuke.createNode('glitch')")
m.addCommand('NS_EKG', "nuke.createNode('NS_EKG')")
m.addCommand("Extrude", "nuke.createNode('Extrude')")
m.addCommand("TX_Fog", "nuke.createNode('TX_Fog')")

## BL Tools
toolbar.addMenu('BL', 'BL.png')

#IMAGE
toolbar.addCommand('BL/Image/Arc', 'nuke.createNode("bl_Arc")', '')
toolbar.addCommand('BL/Image/Line', 'nuke.createNode("bl_Line")', '')
toolbar.addCommand('BL/Image/Random', 'nuke.createNode("bl_Random")', '')
toolbar.addCommand('BL/Image/Shape', 'nuke.createNode("bl_Shape")', '')
toolbar.addCommand('BL/Image/Star', 'nuke.createNode("bl_Star")', '')

#TIME
toolbar.addCommand('BL/Time/ITime', 'nuke.createNode("bl_ITime")', '')

#CHANNEL
toolbar.addCommand('BL/Channel/ChannelBox', 'nuke.createNode("bl_ChannelBox")', '')

#COLOR
toolbar.addCommand('BL/Color/Bytes', 'nuke.createNode("bl_Bytes")', '')
toolbar.addCommand('BL/Color/Compress', 'nuke.createNode("bl_Compress")', '')
toolbar.addCommand('BL/Color/Expand', 'nuke.createNode("bl_Expand")', '')
toolbar.addCommand('BL/Color/Monochrome', 'nuke.createNode("bl_Monochrome")', '')
toolbar.addCommand('BL/Color/Normalizer', 'nuke.createNode("bl_Normalizer")', '')
toolbar.addCommand('BL/Color/SaturationRGB', 'nuke.createNode("bl_SaturationRGB")', '')
toolbar.addCommand('BL/Color/Slice', 'nuke.createNode("bl_Slice")', '')
toolbar.addCommand('BL/Color/Threshold', 'nuke.createNode("bl_Threshold")', '')

#KEYER
toolbar.addCommand('BL/Keyer/ColorSupress', 'nuke.createNode("bl_ColorSupress")', '')
toolbar.addCommand('BL/Keyer/Despillator', 'nuke.createNode("bl_Despillator")', '')
toolbar.addCommand('BL/Keyer/HSV Keyer', 'nuke.createNode("bl_HSVKeyer")', '')
toolbar.addCommand('BL/Keyer/Simple Spill Supress', 'nuke.createNode("bl_SpillSupress")', '')

#LAYER
toolbar.addCommand('BL/Layer/LayerAE', 'nuke.createNode("bl_LayerAE")', '')

#FILTER
toolbar.addCommand('BL/Filter/Morphological/Binary', 'nuke.createNode("bl_mf_Binary")', '')
toolbar.addCommand('BL/Filter/Morphological/Border', 'nuke.createNode("bl_mf_Border")', '')
toolbar.addCommand('BL/Filter/Morphological/DirectionalBlur', 'nuke.createNode("bl_mf_DirectionalBlur")', '')
toolbar.addCommand('BL/Filter/Morphological/Occlusion', 'nuke.createNode("bl_mf_Occlusion")', '')
toolbar.addCommand('BL/Filter/Morphological/ShapeSofter', 'nuke.createNode("bl_mf_ShapeSofter")', '')

toolbar.addCommand('BL/Filter/BlurChroma', 'nuke.createNode("bl_BlurChroma")', '')
toolbar.addCommand('BL/Filter/Bokeh', 'nuke.createNode("bl_Bokeh")', '')
toolbar.addCommand('BL/Filter/IBokeh', 'nuke.createNode("bl_IBokeh")', '')
toolbar.addCommand('BL/Filter/ColorEdge', 'nuke.createNode("bl_ColorEdge")', '')
toolbar.addCommand('BL/Filter/Convolve', 'nuke.createNode("bl_Convolve")', '')
toolbar.addCommand('BL/Filter/CurveFilter', 'nuke.createNode("bl_CurveFilter")', '')
toolbar.addCommand('BL/Filter/EdgeExtend', 'nuke.createNode("bl_EdgeExtend2")', '')
toolbar.addCommand('BL/Filter/Emboss', 'nuke.createNode("bl_Emboss")', '')
toolbar.addCommand('BL/Filter/IBlur', 'nuke.createNode("bl_IBlur")', '')
toolbar.addCommand('BL/Filter/IDilateErode', 'nuke.createNode("bl_IDilateErode")', '')

#STYLISE
toolbar.addCommand('BL/Stylise/Mosaic', 'nuke.createNode("bl_Mosaic")', '')
toolbar.addCommand('BL/Stylise/Randomizer', 'nuke.createNode("bl_Randomizer")', '')
toolbar.addCommand('BL/Stylise/ScanLines', 'nuke.createNode("bl_ScanLines")', '')
toolbar.addCommand('BL/Stylise/Scatterize', 'nuke.createNode("bl_Scatterize")', '')
toolbar.addCommand('BL/Stylise/Solarize', 'nuke.createNode("bl_Solarize")', '')
toolbar.addCommand('BL/Stylise/TileMosaic', 'nuke.createNode("bl_TileMosaic")', '')
toolbar.addCommand('BL/Stylise/Zebrafy', 'nuke.createNode("bl_Zebrafy")', '')

#TRANSFORM
toolbar.addCommand('BL/Transform/Scroll', 'nuke.createNode("bl_Scroll")', '')
toolbar.addCommand('BL/Transform/ToBBOX', 'nuke.createNode("bl_ToBBOX")', '')

#WARP
toolbar.addCommand('BL/Warp/Bulge', 'nuke.createNode("bl_Bulge")', '')
toolbar.addCommand('BL/Warp/ChromaticAberation', 'nuke.createNode("bl_ChromaticAberation")', '')
toolbar.addCommand('BL/Warp/IDisplace', 'nuke.createNode("bl_IDisplace")', '')
toolbar.addCommand('BL/Warp/Twirl', 'nuke.createNode("bl_Twirl")', '')
toolbar.addCommand('BL/Warp/Wave', 'nuke.createNode("bl_Wave")', '')

#PIPE
toolbar.addCommand('BL/Pipe/GUI Switch', 'nuke.createNode("bl_GUISwitch")', '')
toolbar.addCommand('BL/Pipe/CleanOUT', 'nuke.createNode("bl_CleanOUT")', '')

#OTHER
toolbar.addCommand('BL/Other/Filler', 'nuke.createNode("bl_Filler")', '')
toolbar.addCommand('BL/Other/Match', 'nuke.createNode("bl_Match")', '')
toolbar.addCommand('BL/Other/Sample', 'nuke.createNode("bl_Sample")', '')
toolbar.addCommand('BL/Other/Scanner', 'nuke.createNode("bl_Scanner")', '')
toolbar.addCommand('BL/Other/ScanSlice', 'nuke.createNode("bl_ScanSlice")', '')
toolbar.addCommand('BL/Other/SetBBOXColor', 'nuke.createNode("bl_SetBBOXColor")', '')