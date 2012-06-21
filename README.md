.step-to-.dae
=============

Script that helps to convert 3D models in .step format to .dae format using FreeCAD and Meshlab

Introduction
------------

I wrote this program because I wanted to use .step 3D models in Google Sketchup. The way I found was to convert to binary stl format using FreeCAD and then to Collada (DAE) with Meshlab. This program is just a Python script that makes this process automatic.

Dependencies
------------

* [FreeCAD](http://sourceforge.net/apps/mediawiki/free-cad/index.php?title=Main_Page)
* [MeshLab](http://meshlab.sourceforge.net/)
* Python v2.7

You can find them all in Ubuntu's repositories, I'm sure they are present in other distributions' repositories as well.

Usage
------------

There are two ways of using this script.

To convert all step files in current directory use

$ step-to-dae 

To convert a single step file (foo.step) use

$ step-to-dae foo.step

All processed step files are stored in a folder called "done_step" nested in the current directory


Known Bugs
------------

The script is not able to process ~30% of tested step files. The program fails during the conversion of the step file into a binary stl with FreeCAD. In some cases it hangs and in some others it breaks while using nearly all RAM.

Anyway, I know that it's not an issue of the script itself, because the same thing happens if I try to convert the file manually (using FreeCAD's GUI) but I'm not an expert so there's a chance that some of this bugs could be fixed. Please contact me if you know how.


Contact
------------

[fede.barabas@gmail.com](mailto:fede.barabas@gmail.com)
