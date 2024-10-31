from PIL import Image
import numpy as np
from scipy.ndimage import distance_transform_edt
import os
import sys

def get_batch_choice():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("How would you like to process the files?")
        print("1. Process all files the same way")
        print("2. Choose settings for each file individually")
        choice = input("\nEnter your choice (1 or 2): ").strip()
        
        if choice in ['1', '2']:
            return choice == '1'  # Returns True if batch process, False if individual
        else:
            print("\nInvalid choice. Please enter 1 or 2.")
            input("\nPress Enter to try again...")

def get_color_choice(filename=None):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        if filename:
            print(f"Processing: {filename}")
        print("\nChoose how to process the non-transparent areas:")
        print("1. Keep original colors")
        print("2. Convert to white")
        choice = input("\nEnter your choice (1 or 2): ").strip()
        
        if choice in ['1', '2']:
            return choice == '2'  # Returns True if they want white, False if keep original
        else:
            print("\nInvalid choice. Please enter 1 or 2.")
            input("\nPress Enter to try again...")

def generate_output_path(input_path, make_white):
    # Split the file path into directory, filename, and extension
    directory = os.path.dirname(input_path)
    filename = os.path.basename(input_path)
    name, ext = os.path.splitext(filename)
    
    # Create new filename with appropriate suffix
    suffix = "_whitefilled" if make_white else "_filled"
    new_filename = f"{name}{suffix}{ext}"
    
    # Combine with original directory
    return os.path.join(directory, new_filename)

def process_single_image(input_path, make_white):
    try:
        # Load and process the image
        image = Image.open(input_path).convert("RGBA")
        
        # Convert image to numpy array
        image_data = np.array(image)
        
        # Separate the color and alpha channels
        rgb_data = image_data[..., :3]
        alpha_channel = image_data[..., 3]
        
        # Mask to identify non-transparent pixels
        non_transparent_mask = (alpha_channel != 0)
        
        # If user chose to make it white, apply white to non-transparent pixels
        if make_white:
            rgb_data[non_transparent_mask] = [255, 255, 255]
        
        # Mask to identify transparent pixels
        transparent_mask = (alpha_channel == 0)
        
        # Generate distance and nearest index maps
        distance_map, indices = distance_transform_edt(transparent_mask, return_indices=True)
        
        # Apply the nearest non-transparent color to transparent pixels
        rgb_data[transparent_mask] = rgb_data[tuple(indices[:, transparent_mask])]
        
        # Create new image data with updated RGB values and original alpha channel
        new_image_data = np.dstack((rgb_data, alpha_channel))
        
        # Generate output path and save
        output_path = generate_output_path(input_path, make_white)
        new_image = Image.fromarray(new_image_data, 'RGBA')
        new_image.save(output_path)
        
        return True, output_path
        
    except Exception as e:
        return False, str(e)

def process_images(input_paths):
    # If no files provided, show error
    if not input_paths:
        print("Please drag and drop image files onto the executable.")
        input("Press Enter to close...")
        return

    # Skip batch choice if only one file
    batch_process = False
    batch_make_white = None
    if len(input_paths) > 1:
        batch_process = get_batch_choice()
        if batch_process:
            batch_make_white = get_color_choice()
    
    # Process each file
    results = []
    for input_path in input_paths:
        # Get color choice based on number of files and batch settings
        if len(input_paths) == 1:
            make_white = get_color_choice()
        else:
            make_white = batch_make_white if batch_process else get_color_choice(os.path.basename(input_path))
        
        # Process the image
        success, result = process_single_image(input_path, make_white)
        results.append((input_path, success, result))
    
    # Show results
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Processing Complete!\n")
    print("Results:")
    for input_path, success, result in results:
        filename = os.path.basename(input_path)
        if success:
            output_filename = os.path.basename(result)
            print(f"✓ {filename} -> {output_filename}")
        else:
            print(f"✗ {filename} - Error: {result}")
    
    print("\nPress Enter to close...")
    input()

if __name__ == "__main__":
    # Get all files from command line arguments
    input_files = sys.argv[1:]
    process_images(input_files)