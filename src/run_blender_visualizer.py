
import subprocess
import os


def find_blender_exe(min_version=2.8, max_version=5.0):
    """ Find the most recent version of Blender installed in the current device

    Args:
        min_version (float): Min supported Blender version. Defaults to 2.8.
        max_version (float): Max avaiable Blender version, 3.6 is the lastest. Defaults to 5.0.

    Returns:
        blender_exe (str): Abs path to blender.exe in this machine.

    """
    disks = ['C', 'D']
    program_files_names = ['Program Files', 'Program Files (x86)']
    min_version = 2.8  # lower than 2.8 is incompatible with this script
    versions = [str(round(ver, 1)) for ver in np.arange(min_version, max_version, 0.1)]
    versions.reverse()
    for disk in disks:
        for program_files in program_files_names:
            program_files_dir = f'{disk}:\{program_files}'
            blender_exe = os.path.join(program_files_dir, 'Steam', 'steamapps', 'common', 'Blender', 'blender.exe')
            if os.path.exists(blender_exe):
                return blender_exe

            for version in versions:
                blender_exe = os.path.join(program_files_dir, 'Blender Foundation', f'Blender {version}', 'blender.exe')
                if os.path.exists(blender_exe):
                    return blender_exe
    raise ValueError("Please install Blender 2.8 version or greater\nfrom www.blender.org/download/ or steam")


if __name__ == "__main__":
    blender_exe = find_blender_exe() 
    command = [blender_exe,
               '--python', 'blender_visualizer.py']
    
    # print('\n'.join(command))
    subprocess.run(command)
