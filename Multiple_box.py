This python can create multiple box in blender

import bpy

# Create the box mesh
gbox_mesh = bpy.data.meshes.new("Green BoxMesh")
gbox_obj = bpy.data.objects.new("Box1", gbox_mesh)
gbox_verts = [(-4, 0, 0), (-4, 2, 0), (-3, 2, 0), (-3, 0, 0), (-4, 0, 3), (-4, 2, 3), (-3, 2, 3), (-3, 0, 3)]
gbox_faces = [(0, 1, 2, 3), (0, 4, 5, 1), (1, 5, 6, 2), (2, 6, 7, 3), (3, 7, 4, 0), (4, 7, 6, 5)]
gbox_mesh.from_pydata(gbox_verts, [], gbox_faces)

ybox_mesh = bpy.data.meshes.new("Yellow BoxMesh")
ybox_obj = bpy.data.objects.new("Box2", ybox_mesh)
ybox_verts = [(0, 0, 0), (0, 1, 0), (1, 1, 0), (1, 0, 0), (0, 0, 1), (0, 1, 1), (1, 1, 1), (1, 0, 1)]
ybox_faces = [(0, 1, 2, 3), (0, 4, 5, 1), (1, 5, 6, 2), (2, 6, 7, 3), (3, 7, 4, 0), (4, 7, 6, 5)]
ybox_mesh.from_pydata(ybox_verts, [], ybox_faces)

rbox_mesh = bpy.data.meshes.new("Red BoxMesh")
rbox_obj = bpy.data.objects.new("Box3", rbox_mesh)
rbox_verts = [(3, 0, 0), (3, 4, 0), (5, 4, 0), (5, 0, 0), (3, 0, 2), (3, 4, 2), (5, 4, 2), (5, 0, 2)]
rbox_faces = [(0, 1, 2, 3), (0, 4, 5, 1), (1, 5, 6, 2), (2, 6, 7, 3), (3, 7, 4, 0), (4, 7, 6, 5)]
rbox_mesh.from_pydata(rbox_verts, [], rbox_faces)

# Create the lid mesh
glid_mesh = bpy.data.meshes.new("LidMesh")
glid_obj = bpy.data.objects.new("Lid", lid_mesh)
glid_verts = [(-4.1, -0.5, 3), (-4.1, 2.5, 3), (-2.9, 2.5,3), (-2.9, -0.5, 3), (-4.1, -0.5, 3.5), (-4.1, 2.5, 3.5), (-2.9, 2.5, 3.5), (-2.9, -0.5, 3.5)]
glid_faces = [(0, 1, 2, 3), (4, 7, 6, 5), (0, 4, 5, 1), (1, 5, 6, 2), (2, 6, 7, 3), (3, 7, 4, 0)]
glid_mesh.from_pydata(lid_verts, [], lid_faces)

ylid_mesh = bpy.data.meshes.new("YLidMesh")
ylid_obj = bpy.data.objects.new("YLid", ylid_mesh)
ylid_verts = [(-0.1, -0.1, 1), (-0.1, 1.1, 1), (1.1, 1.1,1), (1.1, -0.1, 1), (-0.1, -0.1, 1.3), (-0.1, 1.1, 1.3), (1.1, 1.1, 1.3), (1.1, -0.1, 1.3)]
ylid_faces = [(0, 1, 2, 3), (4, 7, 6, 5), (0, 4, 5, 1), (1, 5, 6, 2), (2, 6, 7, 3), (3, 7, 4, 0)]
ylid_mesh.from_pydata(ylid_verts, [], ylid_faces)

rlid_mesh = bpy.data.meshes.new("RLidMesh")
rlid_obj = bpy.data.objects.new("RLid", rlid_mesh)
rlid_verts = [(2.9, -0.1, 2), (2.9, 4.1, 2), (5.1, 4.1,2), (5.1, -0.1, 2), (2.9, -0.1, 2.5), (2.9, 4.1, 2.5), (5.1, 4.1, 2.5), (5.1, -0.1, 2.5)]
rlid_faces = [(0, 1, 2, 3), (4, 7, 6, 5), (0, 4, 5, 1), (1, 5, 6, 2), (2, 6, 7, 3), (3, 7, 4, 0)]
rlid_mesh.from_pydata(rlid_verts, [], rlid_faces)


# Join the box and lid objects into a single object
scene = bpy.context.scene
scene.collection.objects.link(gbox_obj)
scene.collection.objects.link(glid_obj)
scene.collection.objects.link(ybox_obj)
scene.collection.objects.link(ylid_obj)
scene.collection.objects.link(rbox_obj)
scene.collection.objects.link(rlid_obj)
scene.view_layers[0].objects.active = gbox_obj
scene.view_layers[0].objects.active = ybox_obj
scene.view_layers[0].objects.active = rbox_obj
bpy.ops.object.select_all(action='DESELECT')
gbox_obj.select_set(True)
glid_obj.select_set(True)
ybox_obj.select_set(True)
ylid_obj.select_set(True)
rbox_obj.select_set(True)
rlid_obj.select_set(True)
bpy.ops.object.join()

# Set the location of the object
gbox_obj.location = (0, 0, 0)
ybox_obj.location = (0, 0, 0)
rbox_obj.location = (0, 0, 0)


# Create a new material and set its color to brown
mat1 = bpy.data.materials.new("GreenMaterial")
mat1.diffuse_color = (0, 1, 0, 1.0)
mat2 = bpy.data.materials.new("YBrownMaterial")
mat2.diffuse_color = (0.8, 0.6, 0.2, 1.0)
mat3 = bpy.data.materials.new("RedMaterial")
mat3.diffuse_color = (1, 0, 0, 1.0)


# Assign the material to the mesh
gbox_mesh.materials.append(mat1)
glid_mesh.materials.append(mat1)
ybox_mesh.materials.append(mat2)
ylid_mesh.materials.append(mat2)
rbox_mesh.materials.append(mat3)
rlid_mesh.materials.append(mat3)


# Update the mesh with the new data
gbox_mesh.update()
glid_mesh.update()
ybox_mesh.update()
ylid_mesh.update()
rbox_mesh.update()
rlid_mesh.update()
