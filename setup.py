import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
    "packages": ["PIL", "numpy", "scipy.ndimage"],
    "excludes": ["tkinter", "unittest"],
    "include_files": ["README.txt"],
}

setup(
    name="Icon Transparent Fill",
    version="1.0",
    description="Tool to fill transparent areas in images",
    options={"build_exe": build_exe_options},
    executables=[
        Executable(
            "fill_transparent.py",
            base="Win32GUI" if sys.platform == "win32" else None,
            target_name="FillTransparentexe",
            icon="icon.ico"
    ]
)