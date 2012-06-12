import sys
sys.path.append("/usr/lib/freecad/lib/")
import time

t_start = time.time()

import os
import FreeCAD
import Part
import MeshPart

cwd = os.getcwd() + "/"
extension = ".step"
list_of_files = [file for file in os.listdir(cwd) if file.lower().endswith(extension)]

for i in range(len(list_of_files)):

    # opening of file
    file = cwd + list_of_files[i]
    FreeCAD.newDocument()
    FreeCAD.setActiveDocument("Unnamed")
    doc = FreeCAD.getDocument("Unnamed")
    FreeCAD.ActiveDocument = doc
    Part.insert(file,"Unnamed")
    
    # before converting to mesh we need to merge all shapes in the document
    if len(doc.Objects) > 1:    
        FreeCAD.activeDocument().addObject("Part::MultiFuse","Fusion")
        #FreeCAD.activeDocument().Fusion.Shapes = [FreeCAD.activeDocument()._911_E0W001,FreeCAD.activeDocument()._911_E0W]
        FreeCAD.activeDocument().Fusion.Shapes = [doc.Objects[k].Content for k in range(len(doc.Objects))]
        FreeCAD.ActiveDocument.recompute()
        mesh = doc.addObject("Mesh::Feature","Mesh")
        mesh.Mesh = MeshPart.meshFromShape(doc.getObject("Fusion").Shape,5,0,0,0.5)
    else:
        mesh = doc.addObject("Mesh::Feature","Mesh")
        mesh.Mesh = MeshPart.meshFromShape(doc.getObject(doc.Objects[0].Name).Shape,5,0,0,0.5)
    
    del doc, mesh

    # saving the stl file 
    file_stl = file.replace(".step", ".stl")
    FreeCAD.ActiveDocument.getObject("Mesh").Mesh.write(file_stl,"STL")
    FreeCAD.closeDocument("Unnamed")

    # using meshlab to convert stl files to dae
    file_dae = file.replace(".step", ".dae")
    convert = "meshlabserver -i " + file_stl + " -o " + file_dae
    os.system(convert)
    os.system("rm " + file_stl)
    os.system("mkdir " + cwd + "done_step")
    os.system("mv " + file + " " + cwd + "done_step/")

t_end = time.time()

print "Started at ", time.ctime(t_start)
print "Finished at ", time.ctime(t_end)
print "Time elapsed: ", (t_end - t_start)/60, " minutes"
print "Number of models processed: ", len(list_of_files)
