"""
ImageHistograph.py

Get an image from the user and compute a histogram based on the pixel values in the image.
Allows colour RGB histogram.

User can change threshold to see different values on the histogram, based on the binary changes.

Uses tkinter for window, PIL for image manipulation, and matplotlib for graphing

"""

## MODULES AND VARIABLES
import tkinter as tk
from colorsys import rgb_to_yiq
from tkinter import filedialog
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import os

isRGB = False  # grey or rgb histogram
image = None  # image
greyImage = None  # greyscale image
rgbImage = None  # coloured image
histogram = None
currentHistogram = None

## CANVASES
# Create main window and frames
root = tk.Tk()
root.title("Image Colour Analysis")

leftFrame = tk.Frame(root)
leftFrame.pack(side=tk.LEFT, padx=10, pady=10)

rightFrame = tk.Frame(root)
rightFrame.pack(side=tk.RIGHT, padx=10, pady=10, fill=tk.BOTH, expand=True)

# Canvas for image
canvas = tk.Canvas(leftFrame, width=300, height=300)
canvas.pack()

# Canvas for histogram
histCanvas = tk.Canvas(rightFrame, width=400, height=300)
histCanvas.pack()


## FUNCTIONS
def find_image_file(base_name):
    # find the image which the user specified
    extensions = ["jpg", "png", "bmp", "gif", "tiff"]  # general image formats
    for ext in extensions:
        fileName = f"{base_name}.{ext}"
        if os.path.isfile(fileName):
            return fileName
    return None


def display_image(img):
    # Stretch image to fit the canvas and display it.
    resized = img.resize((300, 300))
    tkImg = ImageTk.PhotoImage(resized)
    canvas.create_image(150, 150, image=tkImg)
    canvas.image = tkImg


def compute_histogram(img):
    # compute a histogram based on the image data
    global histogram
    if isRGB:
        # Compute separate histograms for rgb
        rHist = [0] * 256
        gHist = [0] * 256
        bHist = [0] * 256
        for r, g, b in img.getdata():
            rHist[r] += 1
            gHist[g] += 1
            bHist[b] += 1
        histogram = (rHist, gHist, bHist)
    else:
        # Compute a single histogram for grey
        hist = [0] * 256
        for pixel in img.getdata():
            hist[pixel] += 1
        histogram = hist


def update_histogram(fig):
    # update the histogram  the image was updated
    global currentHistogram
    if currentHistogram is not None:
        currentHistogram.get_tk_widget().destroy()
    currentHistogram = FigureCanvasTkAgg(fig, master=histCanvas)
    currentHistogram.draw()
    currentHistogram.get_tk_widget().pack()


def apply_threshold_delayed(threshold):
    # apply the threshold (after the user lets go of the slider)
    base_img = rgbImage if isRGB else greyImage

    # thresholding
    new_img = base_img.point(lambda p: 0 if p < threshold else 255)
    display_image(new_img)

    # make histogram from base image
    compute_histogram(base_img)

    if isRGB:
        plot_histogram(grey=False)
    else:
        plot_histogram(grey=True, threshold=threshold)


def on_slider_release(event):
    # Get slider value when mouse is released and update thresholding once
    val = threshold_slider.get()
    apply_threshold_delayed(val)


def plot_histogram(grey=True, threshold=None):
    # Close any existing matplotlib figures
    plt.close('all')
    fig, ax = plt.subplots()
    if grey:
        # grey mode: plot histogram bars in black.
        for i in range(256):
            ax.bar(i, histogram[i], color='black', width=1)
        # overlay threshold marker if provided
        if threshold is not None:
            ax.axvline(x=threshold, color='red', linestyle='--', linewidth=1, label='Threshold')
            ax.legend()
        ax.set_title("Grey Histogram")
    else:
        # In colour mode, plot all three channels.
        r_hist, g_hist, b_hist = histogram
        ax.bar(range(256), r_hist, color='red', alpha=0.5, label='Red', edgecolor='red')
        ax.bar(range(256), g_hist, color='green', alpha=0.5, label='Green', edgecolor='green')
        ax.bar(range(256), b_hist, color='blue', alpha=0.5, label='Blue', edgecolor='blue')
        ax.set_title("Colour Histogram")
        ax.legend()
    ax.set_xlim([0, 255])
    ax.set_xlabel("Intensity")
    ax.set_ylabel("Frequency")
    update_histogram(fig)


def toggle_rgb_grey():
    # toggle between either grey/rgb histograms
    global isRGB
    isRGB = not isRGB
    if isRGB:
        display_image(rgbImage)
        compute_histogram(rgbImage)
        plot_histogram(grey=False)
    else:
        display_image(greyImage)
        compute_histogram(greyImage)
        plot_histogram(grey=True)


def toggle_histogram(colour):
    # this only applies in colour mode, toggles between red/green/blue individual
    if not isRGB:
        return
    r_hist, g_hist, b_hist = histogram
    plt.close('all')
    fig, ax = plt.subplots()
    if colour == 'red':
        ax.bar(range(256), r_hist, color='red', edgecolor='red')
        ax.set_title("Red Histogram")
    elif colour == 'green':
        ax.bar(range(256), g_hist, color='green', edgecolor='green')
        ax.set_title("Green Histogram")
    elif colour == 'blue':
        ax.bar(range(256), b_hist, color='blue', edgecolor='blue')
        ax.set_title("Blue Histogram")
    ax.set_xlim([0, 255])
    ax.set_xlabel("Intensity")
    ax.set_ylabel("Frequency")
    update_histogram(fig)


def show_all_rgb_histograms():
    # default, all stacked histograms
    if not isRGB:
        return
    plot_histogram(grey=False)


def select_image():
    # ask the user what image to show
    global image, greyImage, rgbImage
    file_path = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp *.gif *.tiff")])
    if file_path:
        image = Image.open(file_path)
        greyImage = image.convert("L")
        rgbImage = image.convert("RGB")
        # Display the image based on the current mode
        if isRGB:
            display_image(rgbImage)
            compute_histogram(rgbImage)
            plot_histogram(grey=False)
        else:
            display_image(greyImage)
            compute_histogram(greyImage)
            plot_histogram(grey=True)


## BUTTONS
# image selector
select_image_button = tk.Button(leftFrame, text="Select Image", command=select_image, width=30)
select_image_button.pack(pady=2)

# threshold slider
threshold_slider = tk.Scale(leftFrame, from_=0, to=255, orient=tk.HORIZONTAL,
                            label="Threshold", length=300)
threshold_slider.pack(pady=5)
threshold_slider.bind("<ButtonRelease-1>", on_slider_release)

# rgb or greyscale
toggle_rgb_button = tk.Button(leftFrame, text="Toggle RGB/Grey", command=toggle_rgb_grey, width=30)
toggle_rgb_button.pack(pady=2)

# r
show_red_button = tk.Button(leftFrame, text="Show Red Histogram", command=lambda: toggle_histogram('red'), width=30)
show_red_button.pack(pady=2)

# g
show_green_button = tk.Button(leftFrame, text="Show Green Histogram", command=lambda: toggle_histogram('green'),
                              width=30)
show_green_button.pack(pady=2)

# b
show_blue_button = tk.Button(leftFrame, text="Show Blue Histogram", command=lambda: toggle_histogram('blue'), width=30)
show_blue_button.pack(pady=2)

# rgb (assuming separated)
show_all_button = tk.Button(leftFrame, text="Show All RGB Histograms", command=show_all_rgb_histograms, width=30)
show_all_button.pack(pady=2)

# load default image
file_path = find_image_file("image")  # default value
if file_path:
    image = Image.open(file_path)
    greyImage = image.convert("L")
    rgbImage = image.convert("RGB")
    # Start in grey mode
    display_image(greyImage)
    compute_histogram(greyImage)
    plot_histogram(grey=True)
else:
    print("No image file found with the name 'image'.")

## MAIN
root.mainloop()
