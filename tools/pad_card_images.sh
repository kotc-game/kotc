#!/bin/sh
# Mass image resizer
# c.f.: https://graphicdesign.stackexchange.com/questions/37261/how-to-batch-resize-canvas-of-multiple-files-placing-the-original-pictures-in-th
# Requires ImageMagick (package "imagemagick" in Debian and its derivatives)
# License: CC0 (public domain)

rm -r ../cards-padded ../tip_cards-padded
mkdir ../cards-padded
mkdir ../tip_cards-padded
cp ../cards/*.png ../cards-padded
cp ../tip_cards/*.png ../tip_cards-padded
mogrify -extent 1200x1600 -gravity Center -fill white ../cards-padded/*.png ../tip_cards-padded/*.png

