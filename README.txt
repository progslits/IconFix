Icon Transparent Fill Tool
=========================

A utility for processing images with transparent areas. This tool can either maintain original colors or convert non-transparent areas to white, while intelligently filling transparent regions with colors from nearby pixels.

FEATURES
--------
* Smart Transparent Fill
  - Automatically fills transparent areas based on surrounding colors

* Color Options
  - Keep original colors
  - Convert non-transparent areas to white

* Batch Processing
  - Process multiple files at once
  - Choose between batch or individual settings

* Non-Destructive
  - Creates new files instead of modifying originals

* Clear File Naming
  - Original colors: adds "_filled" suffix
  - White conversion: adds "_whitefilled" suffix

USAGE
-----
1. Single Image Processing:
   - Drag and drop a single image onto FillTransparent.exe
   - Choose your color preference when prompted
   - A new file will be created with the appropriate suffix

2. Batch Processing:
   - Select multiple images and drag them onto FillTransparent.exe
   - Choose whether to:
     a) Process all files the same way
     b) Choose settings for each file individually
   - Follow the prompts to select color preferences
   - New files will be created for each processed image

COLOR OPTIONS MENU
----------------
Choose how to process the non-transparent areas:
1. Keep original colors
2. Convert to white

BATCH PROCESSING MENU
-------------------
How would you like to process the files?
1. Process all files the same way
2. Choose settings for each file individually

OUTPUT FILES
-----------
The tool creates new files with these naming patterns:
- Original colors preserved: "filename_filled.png"
- Converted to white: "filename_whitefilled.png"

Example:
Original file: icon.png
- With original colors -> icon_filled.png
- With white conversion -> icon_whitefilled.png

FILE SUPPORT
-----------
- Supports PNG files with transparency
- Preserves transparency in output files
- Maintains original image quality

TIPS
----
- Original files are never modified
- Process any number of files at once
- Clear feedback shows success/failure for each file
- Each new file is saved in the same location as the original

TROUBLESHOOTING
--------------
If you encounter any issues:
1. Ensure your images are in a supported format (PNG with transparency)
2. Check that you have write permissions in the folder
3. Make sure the original files aren't open in another program

CREDITS
-------
Created by [progslit & Claude AI]


