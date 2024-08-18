import oom_kicad
import oom_markdown
import os
import copy
import scad

#process
#  locations set in working_parts.ods 
#  export to working_parts.csv
#  put components on the right side of the board
#  run this script

def main(**kwargs):
    #place_parts(**kwargs)
    #make_readme(**kwargs)
    scad.make_scad(**kwargs)
    
    

def make_readme(**kwargs):
    os.system("generate_resolution.bat")
    oom_markdown.generate_readme_project(**kwargs)
    #oom_markdown.generate_readme_teardown(**kwargs)
    
def make_scad(**kwargs):
    import opsc
    import oobb 
    import oobb_base

    kwargs["save_type"] = "none"
    #kwargs["save_type"] = "all"
    kwargs["size"] = "oobb"
    kwargs["type"] = "oomlout_bolt_tool_funnel"
    kwargs["width"] = 3
    kwargs["height"] = 5
    kwargs["thickness"] = 6
     # default sets
    width = kwargs.get("width", 3)
    height = kwargs.get("height", 5)
    thickness = kwargs.get("thickness", 3)
    size = kwargs.get("size", "oobb")
    pos = kwargs.get("pos", [0, 0, 0])
    # extra sets
    holes = kwargs.get("holes", True)
    both_holes = kwargs.get("both_holes", True)    
    kwargs["pos"] = pos
    
        # get the default thing
    thing = oobb_base.get_default_thing(**kwargs)
    th = thing["components"]
    kwargs.pop("size","")

    th.append(oobb_base.get_comment("plate main","p"))
    # add plate
    p3 = copy.deepcopy(kwargs)
    p3["type"] = "p"   
    p3["shape"] = f"{size}_plate"
    p3["width"] = width
    p3["height"] = height  
    p3["depth"] = thickness
    p3["pos"] = pos
    #p3["m"] = ""  
    oobb_base.append_full(thing,**p3)      
    #th.append(oobb_base.oobb_easy(**p3))
    
    # add holes
    if holes:
        th.append(oobb_base.get_comment("holes main","n"))
        p3 = copy.deepcopy(kwargs)
        p3["type"] = "n"
        p3["shape"] = f"{size}_holes"
        p3["width"] = width
        p3["height"] = height
        p3["pos"] = pos
        p3["both_holes"] = both_holes
        #p3["m"] = ""
        oobb_base.append_full(thing,**p3)      
        #th.extend(oobb_base.oobb_easy(**p3))   
        
        
        save_type = kwargs.get("save_type", "all")
        overwrite = True
        modes = ["3dpr", "laser", "true"]
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
            
 


#take component positions from working_parts.csv and place them in working.kicad_pcb
def place_parts(**kwargs):
    board_file = "kicad/current_version/working/working.kicad_pcb"
    parts_file = "working_parts.csv"
    #load csv file
    import csv
    with open(parts_file, 'r') as f:
        reader = csv.DictReader(f)
        parts = [row for row in reader]


    
    oom_kicad.kicad_set_components(board_file=board_file, parts=parts, corel_pos=True, **kwargs)






if __name__ == '__main__':
    main()