import copy
import opsc
import oobb
import oobb_base

def main(**kwargs):
    make_scad(**kwargs)

def make_scad(**kwargs):
    parts = []

    # save_type variables
    if True:
        filter = ""
        filter = "hanger"

        kwargs["save_type"] = "none"
        kwargs["save_type"] = "all"
        
        kwargs["overwrite"] = True
        
        kwargs["modes"] = ["3dpr", "laser", "true"]
        #kwargs["modes"] = ["3dpr"]
        #kwargs["modes"] = ["laser"]

    # default variables
    if True:
        kwargs["size"] = "oobb"
        kwargs["width"] = 1
        kwargs["height"] = 1
        kwargs["thickness"] = 9

    # project_variables
    if True:
        pass
    
    # declare parts
    if True:

        part_default = {} 
        part_default["project_name"] = "oomlout_decorative_wall_mount_camera_cctv_dome_140_mm" ####### neeeds setting
        part_default["full_shift"] = [0, 0, 0]
        part_default["full_rotations"] = [0, 0, 0]
        
        
        part = copy.deepcopy(part_default)
        p3 = copy.deepcopy(kwargs)
        p3["thickness"] = 2
        p3["extra"] = "half"
        part["kwargs"] = p3
        part["name"] = "spacer_star"
        parts.append(part)
        
        part = copy.deepcopy(part_default)
        p3 = copy.deepcopy(kwargs)
        p3["thickness"] = 2
        p3["extra"] = "quarter"
        part["kwargs"] = p3
        part["name"] = "spacer_star"
        parts.append(part)

        
        
        part = copy.deepcopy(part_default)
        p3 = copy.deepcopy(kwargs)
        #p3["thickness"] = 6
        part["kwargs"] = p3
        part["name"] = "screw_standoff"
        parts.append(part)

        
        part = copy.deepcopy(part_default)
        p3 = copy.deepcopy(kwargs)
        #p3["thickness"] = 6
        p3["width"] = 5
        p3["height"] = 4
        p3["thickness"] = 12
        part["kwargs"] = p3
        part["name"] = "hanger"
        parts.append(part)





        
    #make the parts
    if True:
        for part in parts:
            name = part.get("name", "default")
            if filter in name:
                print(f"making {part['name']}")
                make_scad_generic(part)            
                print(f"done {part['name']}")
            else:
                print(f"skipping {part['name']}")

def get_base(thing, **kwargs):

    depth = kwargs.get("thickness", 4)
    prepare_print = kwargs.get("prepare_print", False)

    pos = kwargs.get("pos", [0, 0, 0])
    #pos = copy.deepcopy(pos)
    #pos[2] += -20

    #add 5 mm cylinder
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "p"
    p3["shape"] = f"oobb_cylinder"    
    p3["depth"] = depth
    p3["radius"] = 4.75/2
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)         
    p3["zz"] = "bottom"
    p3["pos"] = pos1
    oobb_base.append_full(thing,**p3)
    
    #add 8mm cylinder top
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "p"
    p3["shape"] = f"oobb_cylinder"
    ex = 5
    p3["depth"] = 3 + ex
    p3["radius"] = 8/2
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)
    pos1[2] += depth + ex
    p3["pos"] = pos1
    p3["zz"] = "top"
    oobb_base.append_full(thing,**p3)
    
    #add hole
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "n"
    p3["shape"] = f"oobb_hole"
    p3["radius_name"] = "m3"
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)         
    p3["pos"] = pos1
    oobb_base.append_full(thing,**p3)

    #add countersunk screw
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "n"
    p3["shape"] = f"oobb_screw_socket_cap"
    p3["radius_name"] = "m3"
    p3["depth"] = 16
    p3["nut"] = True
    p3["m"] = "#"
    pos1 = copy.deepcopy(pos)
    pos1[2] += depth + 2
    p3["pos"] = pos1
    rot1 = [0,0,0]
    p3["rot"] = rot1
    oobb_base.append_full(thing,**p3)


    if prepare_print:
        #put into a rotation object
        components_second = copy.deepcopy(thing["components"])
        return_value_2 = {}
        return_value_2["type"]  = "rotation"
        return_value_2["typetype"]  = "p"
        pos1 = copy.deepcopy(pos)
        pos1[0] += 50
        return_value_2["pos"] = pos1
        return_value_2["rot"] = [180,0,0]
        return_value_2["objects"] = components_second
        
        thing["components"].append(return_value_2)

    
        #add slice # top
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_slice"
        #p3["m"] = "#"
        oobb_base.append_full(thing,**p3)

def get_hanger(thing, **kwargs):

    depth = kwargs.get("thickness", 4)
    prepare_print = kwargs.get("prepare_print", False)

    extra = kwargs.get("extra", "")

    pos = kwargs.get("pos", [0, 0, 0])
    #pos = copy.deepcopy(pos)
    #pos[2] += -20

    #add rounded rectangle
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "p"
    p3["shape"] = f"rounded_rectangle"
    dep = depth
    wid = 74
    hei = 59
    size = [wid, hei, dep]
    p3["size"] = size
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)             
    pos1[1] += -hei/2 + 22
    p3["pos"] = pos1
    rot = [0,0,0]
    p3["rot"] = rot    
    oobb_base.append_full(thing,**p3)
    

    #cutoff main piece
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "n"
    p3["shape"] = f"oobb_slice"
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)
    pos1[0] += -500/2 
    pos1[1] += (74-59) - 500 - 15 + 6
    pos1[2] += depth - 3
    p3["pos"] = pos1
    p3["zz"] = "top"
    oobb_base.append_full(thing,**p3)


    #add countersunk screwa
    hole_positions = []
    offset_x = 30
    offset_y = 15
    hole_positions.append([offset_x, offset_y,depth])
    hole_positions.append([0, offset_y,depth])
    hole_positions.append([-offset_x, offset_y,depth])

    p3 = copy.deepcopy(kwargs)
    p3["type"] = "n"
    p3["shape"] = f"oobb_screw_countersunk"
    p3["radius_name"] = "m3_screw_wood"
    p3["depth"] = depth
    p3["pos"] = hole_positions
    #p3["m"] = "#"
    oobb_base.append_full(thing,**p3)

    


    #add m3 holes
    hole_positions = []
    offset = 30
    hole_positions.append([offset, 0,0])
    hole_positions.append([-offset, 0,0])
    hole_positions.append([0, -offset,0])
    hole_positions.append([0, offset,0])
    #hole_positions.append([0, 0,0])

    p3 = copy.deepcopy(kwargs)
    p3["type"] = "n"
    p3["shape"] = f"oobb_hole"    
    p3["radius_name"] = "m3"
    #p3["m"] = "#"    
    p3["pos"] = hole_positions
    oobb_base.append_full(thing,**p3)
    
    #add cylinder cutouts
    positions_cylinder = []
    offset_cylinder = 65
    #positions_cylinder.append([offset_cylinder, offset_cylinder,depth/2])
    #positions_cylinder.append([-offset_cylinder, offset_cylinder,depth/2])
    positions_cylinder.append([offset_cylinder, -offset_cylinder,depth/2])
    positions_cylinder.append([-offset_cylinder, -offset_cylinder,depth/2])
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "n"
    p3["shape"] = f"oobb_cylinder"
    p3["radius"] = 135/2
    p3["depth"] = depth
    #p3["m"] = "#"
    p3["pos"] = positions_cylinder
    oobb_base.append_full(thing,**p3)




    if extra == "half" or extra == "quarter":
        #add big cube to cut in half
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_slice"    
        #p3["m"] = "#"
        pos1 = copy.deepcopy(pos)
        pos1[0] += -250
        pos1[1] += 5
        pos1[2] += -250
        p3["pos"] = pos1
        oobb_base.append_full(thing,**p3)

    if extra == "quarter":
        #add big cube to cut in half
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_slice"    
        #p3["m"] = "#"
        pos1 = copy.deepcopy(pos)
        pos1[1] += -250
        pos1[0] += 5
        pos1[2] += -250
        p3["pos"] = pos1
        oobb_base.append_full(thing,**p3)
    

    if prepare_print:
        #put into a rotation object
        components_second = copy.deepcopy(thing["components"])
        return_value_2 = {}
        return_value_2["type"]  = "rotation"
        return_value_2["typetype"]  = "p"
        pos1 = copy.deepcopy(pos)
        pos1[0] += 50
        return_value_2["pos"] = pos1
        return_value_2["rot"] = [180,0,0]
        return_value_2["objects"] = components_second
        
        thing["components"].append(return_value_2)

    
        #add slice # top
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_slice"
        #p3["m"] = "#"
        oobb_base.append_full(thing,**p3)


def get_screw_standoff(thing, **kwargs):

    depth = kwargs.get("thickness", 4)
    prepare_print = kwargs.get("prepare_print", False)

    pos = kwargs.get("pos", [0, 0, 0])
    #pos = copy.deepcopy(pos)
    #pos[2] += -20

    #add 5 mm cylinder
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "p"
    p3["shape"] = f"oobb_cylinder"    
    p3["depth"] = depth
    p3["radius"] = 4.75/2
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)         
    p3["zz"] = "bottom"
    p3["pos"] = pos1
    oobb_base.append_full(thing,**p3)
    
    #add 8mm cylinder top
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "p"
    p3["shape"] = f"oobb_cylinder"
    ex = 5
    p3["depth"] = 3 + ex
    p3["radius"] = 8/2
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)
    pos1[2] += depth + ex
    p3["pos"] = pos1
    p3["zz"] = "top"
    oobb_base.append_full(thing,**p3)
    
    #add hole
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "n"
    p3["shape"] = f"oobb_hole"
    p3["radius_name"] = "m3"
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)         
    p3["pos"] = pos1
    oobb_base.append_full(thing,**p3)

    #add countersunk screw
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "n"
    p3["shape"] = f"oobb_screw_socket_cap"
    p3["radius_name"] = "m3"
    p3["depth"] = 16
    p3["nut"] = True
    p3["m"] = "#"
    pos1 = copy.deepcopy(pos)
    pos1[2] += depth + 2
    p3["pos"] = pos1
    rot1 = [0,0,0]
    p3["rot"] = rot1
    oobb_base.append_full(thing,**p3)


    if prepare_print:
        #put into a rotation object
        components_second = copy.deepcopy(thing["components"])
        return_value_2 = {}
        return_value_2["type"]  = "rotation"
        return_value_2["typetype"]  = "p"
        pos1 = copy.deepcopy(pos)
        pos1[0] += 50
        return_value_2["pos"] = pos1
        return_value_2["rot"] = [180,0,0]
        return_value_2["objects"] = components_second
        
        thing["components"].append(return_value_2)

    
        #add slice # top
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_slice"
        #p3["m"] = "#"
        oobb_base.append_full(thing,**p3)

def get_spacer_star(thing, **kwargs):

    depth = kwargs.get("thickness", 4)
    prepare_print = kwargs.get("prepare_print", False)

    extra = kwargs.get("extra", "")

    pos = kwargs.get("pos", [0, 0, 0])
    #pos = copy.deepcopy(pos)
    #pos[2] += -20

    #add rounded rectangle
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "p"
    p3["shape"] = f"rounded_rectangle"
    dep = depth
    wid = 74
    hei = 74
    size = [wid, hei, dep]
    p3["size"] = size
    #p3["m"] = "#"
    pos1 = copy.deepcopy(pos)             
    p3["pos"] = pos1
    rot = [0,0,0]
    p3["rot"] = rot    
    oobb_base.append_full(thing,**p3)
    
    #add centrall rounded triangle twist
    if extra != "half" and extra != "quarter":            
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "p"
        p3["shape"] = f"rounded_rectangle"
        dep1 = depth + 3
        wid = 29
        hei = 29
        size = [wid, hei, dep1]
        p3["size"] = size
        #p3["m"] = "#"
        pos1 = copy.deepcopy(pos)             
        p3["pos"] = pos1
        rot = [0,0,45]
        p3["rot"] = rot
        oobb_base.append_full(thing,**p3)


    #add m3 holes
    hole_positions = []
    offset = 30
    hole_positions.append([offset, 0,0])
    hole_positions.append([-offset, 0,0])
    hole_positions.append([0, -offset,0])
    hole_positions.append([0, offset,0])
    #hole_positions.append([0, 0,0])

    p3 = copy.deepcopy(kwargs)
    p3["type"] = "n"
    p3["shape"] = f"oobb_hole"    
    p3["radius_name"] = "m3"
    #p3["m"] = "#"    
    p3["pos"] = hole_positions
    oobb_base.append_full(thing,**p3)
    
    #add cylinder cutouts
    positions_cylinder = []
    offset_cylinder = 65
    positions_cylinder.append([offset_cylinder, offset_cylinder,depth/2])
    positions_cylinder.append([-offset_cylinder, offset_cylinder,depth/2])
    positions_cylinder.append([offset_cylinder, -offset_cylinder,depth/2])
    positions_cylinder.append([-offset_cylinder, -offset_cylinder,depth/2])
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "n"
    p3["shape"] = f"oobb_cylinder"
    p3["radius"] = 135/2
    p3["depth"] = depth
    #p3["m"] = "#"
    p3["pos"] = positions_cylinder
    oobb_base.append_full(thing,**p3)




    if extra == "half" or extra == "quarter":
        #add big cube to cut in half
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_slice"    
        #p3["m"] = "#"
        pos1 = copy.deepcopy(pos)
        pos1[0] += -250
        pos1[1] += 5
        pos1[2] += -250
        p3["pos"] = pos1
        oobb_base.append_full(thing,**p3)

    if extra == "quarter":
        #add big cube to cut in half
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_slice"    
        #p3["m"] = "#"
        pos1 = copy.deepcopy(pos)
        pos1[1] += -250
        pos1[0] += 5
        pos1[2] += -250
        p3["pos"] = pos1
        oobb_base.append_full(thing,**p3)
    

    if prepare_print:
        #put into a rotation object
        components_second = copy.deepcopy(thing["components"])
        return_value_2 = {}
        return_value_2["type"]  = "rotation"
        return_value_2["typetype"]  = "p"
        pos1 = copy.deepcopy(pos)
        pos1[0] += 50
        return_value_2["pos"] = pos1
        return_value_2["rot"] = [180,0,0]
        return_value_2["objects"] = components_second
        
        thing["components"].append(return_value_2)

    
        #add slice # top
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"oobb_slice"
        #p3["m"] = "#"
        oobb_base.append_full(thing,**p3)


###### utilities



def make_scad_generic(part):
    
    # fetching variables
    name = part.get("name", "default")
    project_name = part.get("project_name", "default")
    
    kwargs = part.get("kwargs", {})    
    
    modes = kwargs.get("modes", ["3dpr", "laser", "true"])
    save_type = kwargs.get("save_type", "all")
    overwrite = kwargs.get("overwrite", True)

    kwargs["type"] = f"{project_name}_{name}"

    thing = oobb_base.get_default_thing(**kwargs)
    kwargs.pop("size","")

    #get the part from the function get_{name}"
        
    func = globals()[f"get_{name}"]    
    # test if func exists
    if callable(func):            
        func(thing, **kwargs)        
    else:            
        get_base(thing, **kwargs)   
    
        

    for mode in modes:
        depth = thing.get(
            "depth_mm", thing.get("thickness_mm", 3))
        height = thing.get("height_mm", 100)
        layers = depth / 3
        tilediff = height + 10
        start = 1.5
        if layers != 1:
            start = 1.5 - (layers / 2)*3
        if "bunting" in thing:
            start = 0.5
        opsc.opsc_make_object(f'scad_output/{thing["id"]}/{mode}.scad', thing["components"], mode=mode, save_type=save_type, overwrite=overwrite, layers=layers, tilediff=tilediff, start=start)    


if __name__ == '__main__':
    kwargs = {}
    main(**kwargs)