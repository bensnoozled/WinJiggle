# WinJiggle
A jiggling windows python script

## Context
I was having issues with ghosting on some older monitors that I use for IM clients and text files. This script jiggles the windows on the target monitors every so often so that the gh

## Settings
There are some variables that will need to be customized per machine:

### Probably Required
- `IGNORE` Any windows you don't want jiggled. The current values are the defaults I found in my system.
- `FREQUENCY` How often to run the jiggle.
- `target_monitors_id` This is a list containing the device ids of the monitors you wish to jiggle.

### Optional
- `PIXELS` This is how many pixels to jiggle the windows. I've been using this for a few days, and I think 7 is a good medium.
- `PADDING` I found that on my system the display resolution varied by about 7 pixels. You may need to customize this on your machine.
