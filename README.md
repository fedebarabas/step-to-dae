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

All 


Known Bugs
------------

Contact
------------
