import os


def main(**kwargs):
    #clone or pull oomlout_oompbuilder into temporary/oomlout_oomp_builder
    repo_url = "https://github.com/oomlout/oomlout_oomp_builder"
    repo_dir = "temporary\\oomlout_oomp_builder"
    if not os.path.exists(repo_dir):
        os.system(f"git clone {repo_url} {repo_dir}")
    else:
        os.system(f"cd {repo_dir} && git pull")

    #check the configuration directory exists and isn't empty
    config_dir = "configuration"
    if not os.path.exists(config_dir) or not os.listdir(config_dir):
        input("Configuration directory is empty or doesn't exist. Press enter to continue to copy default build configuration")
        #copy the default build configuration to the configuration directory in windows
        command = f"copy {repo_dir}\\configuration {config_dir}"
        print(command)
        os.system(command)
        
    

    
    
    #import run.py from the cloned repo
    import sys
    sys.path.append(repo_dir)
    import run
    run.main(**kwargs)





if __name__ == '__main__':
    kwargs = {}
    main(**kwargs)