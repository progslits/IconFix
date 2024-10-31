# Icon Transparent Fill Tool

A utility for processing images with transparent areas. This tool can either maintain original colors or convert non-transparent areas to white, while intelligently filling transparent regions with colors from nearby pixels.

## Features

- **Smart Transparent Fill**: Automatically fills transparent areas based on surrounding colors
- **Color Options**: Choose between:
  - Keeping original colors
  - Converting non-transparent areas to white
- **Batch Processing**: 
  - Process multiple files at once
  - Choose between batch or individual settings
- **Non-Destructive**: Creates new files instead of modifying originals
- **Clear File Naming**: 
  - Original colors: adds "_filled" suffix
  - White conversion: adds "_whitefilled" suffix

## Usage

### Single Image Processing
1. Drag and drop a single image onto `FillTransparent.exe`
2. Choose your color preference:
   ```
   Choose how to process the non-transparent areas:
   1. Keep original colors
   2. Convert to white
   ```
3. A new file will be created with the appropriate suffix

### Batch Processing
1. Select multiple images and drag them onto `FillTransparent.exe`
2. Choose your processing method:
   ```
   How would you like to process the files?
   1. Process all files the same way
   2. Choose settings for each file individually
   ```
3. If you chose "Process all files the same way":
   - Select one color preference for all files
4. If you chose "Choose settings for each file individually":
   - Select color preferences for each file as it's processed
5. New files will be created for each processed image

### Output Files
- Original colors preserved: `filename_filled.png`
- Converted to white: `filename_whitefilled.png`

### Examples
Original file: `icon.png`
- With original colors: Creates `icon_filled.png`
- With white conversion: Creates `icon_whitefilled.png`

## File Support
- Supports PNG files with transparency
- Preserves transparency in output files
- Maintains original image quality

## Tips
- Original files are never modified
- Process any number of files at once
- Clear feedback shows success/failure for each file
- Each new file is saved in the same location as the original

## Troubleshooting
If you encounter any issues:
1. Ensure your images are in a supported format (PNG with transparency)
2. Check that you have write permissions in the folder
3. Make sure the original files aren't open in another program

## Credits
Created by [progslit * Claude]
