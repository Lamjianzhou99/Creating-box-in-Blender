# Creating-box-in-Blender
This is SMJE 4263 Computer Integrated Manufacturing (CIM) Digital Twin Exercise 1 with creating single and multiple boxes in Blender.

# Goal 1: Create Single Box

Coding:
import bpy

//Create the box mesh
box_mesh = bpy.data.meshes.new("BoxMesh")
box_obj = bpy.data.objects.new("Box", box_mesh)
box_verts = [(0, 0, 0), (0, 1, 0), (1, 1, 0), (1, 0, 0), (0, 0, 1), (0, 1, 1), (1, 1, 1), (1, 0, 1)]
box_faces = [(0, 1, 2, 3), (0, 4, 5, 1), (1, 5, 6, 2), (2, 6, 7, 3), (3, 7, 4, 0), (4, 7, 6, 5)]
box_mesh.from_pydata(box_verts, [], box_faces)

//Create the lid mesh
lid_mesh = bpy.data.meshes.new("LidMesh")
lid_obj = bpy.data.objects.new("Lid", lid_mesh)
lid_verts = [(-0.1, -0.1, 1), (-0.1, 1.1, 1), (1.1, 1.1,1), (1.1, -0.1, 1), (-0.1, -0.1, 1.3), (-0.1, 1.1, 1.3), (1.1, 1.1, 1.3), (1.1, -0.1, 1.3)]
lid_faces = [(0, 1, 2, 3), (4, 7, 6, 5), (0, 4, 5, 1), (1, 5, 6, 2), (2, 6, 7, 3), (3, 7, 4, 0)]
lid_mesh.from_pydata(lid_verts, [], lid_faces)

//Join the box and lid objects into a single object
scene = bpy.context.scene
scene.collection.objects.link(box_obj)
scene.collection.objects.link(lid_obj)
scene.view_layers[0].objects.active = box_obj
bpy.ops.object.select_all(action='DESELECT')
box_obj.select_set(True)
lid_obj.select_set(True)
bpy.ops.object.join()

//Set the location of the object
box_obj.location = (0, 0, 0)

//Create a new material and set its color to brown
mat1 = bpy.data.materials.new("YBrownMaterial")
mat1.diffuse_color = (0.8, 0.6, 0.2, 1.0)
mm = bpy.data.materials.new("RedMaterial")
mm.diffuse_color = (0, 0, 0, 1)

//Assign the material to the mesh
box_mesh.materials.append(mat1)
lid_mesh.materials.append(mm)

//Update the mesh with the new data
box_mesh.update()
lid_mesh.update()



