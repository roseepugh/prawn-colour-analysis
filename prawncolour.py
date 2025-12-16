def prawncolour(filename):
    """
    This function attempts to identify the colour of a chameleon prawn (Hippolyte varians) from a photo. This works best if the prawn is photographed against a monochrome, light-coloured background.

    Args:
    filename - a number identifying the photo to be analysed from a list of photos named "hipvar[number].png". If a different naming convention or filetype is being used, line 20 can be modified to reflect this.

    Example:
    >>> prawncolour.prawncolour(1)
    """
    #imports necessary modules
    from PIL import Image
    import numpy as np
    from skimage import io
    import matplotlib.pyplot as plt
    import os
    print(f"File to be analysed: hipvar{filename}.png")
    #Importing and checking image
    print("Importing image")
    img_handle  = Image.open(f"./data/prawns/hipvar{filename}.png") #currently works for images named "hipvar[number].png". Can be changed for different filetypes or naming conventions
    img = np.array(img_handle)
    print("Image imported")
    print("Image Dimensions (Height, Width, Colour)", img.shape)
    print("Image Size", img.size)
    io.imshow(img)
    plt.show()
    #format colour data in data frame
    print("Formatting colour data")
    img2 = np.array(img, dtype=np.float64) / 255
    w, h, d = original_shape = tuple(img2.shape)
    img_array = np.reshape(img2, (w * h, d))
    
    from pandas import DataFrame

    #ensures that both images with alpha channels and those without are useable
    if img_array.shape[1] == 4:
        pixels = DataFrame(img_array, columns=["Red", "Green", "Blue", "Alpha"])
    elif img_array.shape[1] == 3:
        pixels = DataFrame(img_array, columns=["Red", "Green", "Blue"])
    
    from matplotlib import colors

    pixels["Hex"] = [colors.to_hex(p) for p in img_array]
    print("Pixel Colours:")
    print(pixels)
    
    #sampling subset of pixels
    print("Generating subset of pixels")
    pixels_sample = pixels.sample(frac=0.05)
    print("Subset of pixels generated")
    #2d visualisation of subset
    print("Plots of subset:")
    def plot_colours(df, c1, c2, c3):
        fig, ax = plt.subplots(1, 3)
        fig.set_size_inches(18, 6)
        df.plot.scatter(c1, c2, c=df["Red"], alpha=0.3, ax=ax[0])
        df.plot.scatter(c1, c3, c=df["Green"], alpha=0.3, ax=ax[1])
        df.plot.scatter(c2, c3, c=df["Blue"], alpha=0.3, ax=ax[2])
    plot_colours(pixels_sample, "Red", "Green", "Blue")
    plt.show()
    
    #3d visualisation of subset
    from mpl_toolkits import mplot3d
    fig = plt.figure(figsize=(10,8))
    ax = plt.axes(projection='3d')
    ax.set_xlabel("Red")
    ax.set_ylabel("Green")
    ax.set_zlabel("Blue",labelpad=-2,rotation=90)
    ax.scatter(pixels_sample["Red"], pixels_sample["Green"], pixels_sample["Blue"], c=pixels_sample["Hex"])
    plt.show()
    
    #colour clusters
    print("Clustering colours in subset")
    from sklearn.cluster import KMeans
    if img_array.shape[1] == 4:
        kmeans = KMeans(n_clusters=2, n_init="auto").fit(pixels_sample[["Red", "Green", "Blue", "Alpha"]])
    elif img_array.shape[1] == 3: 
        kmeans = KMeans(n_clusters=2, n_init="auto").fit(pixels_sample[["Red", "Green", "Blue"]])
    print("Colour clusters:")
    plt.imshow([kmeans.cluster_centers_])
    plt.show()
    #assign clusters to rest of dataset and visualise
    print("Assigning clusters to rest of image")
    if img_array.shape[1] == 4:
        labels = kmeans.predict(pixels[["Red", "Green", "Blue", "Alpha"]])
    elif img_array.shape[1] == 3:
        labels = kmeans.predict(pixels[["Red", "Green", "Blue"]])
    labels
    
    from pandas import DataFrame, Series
    
    Series(labels).value_counts(sort=False).plot.bar(color=kmeans.cluster_centers_)
    print("Colour cluster proportions:")
    plt.show()
    #convert back to 3d
    reduced = np.array([kmeans.cluster_centers_[p] for p in labels]).reshape(original_shape)
    f, axarr = plt.subplots(1, 2, sharex=True, sharey=True, figsize=(18, 9))
    axarr[0].imshow(img)
    axarr[0].set_title("Original")
    axarr[1].imshow(reduced)
    axarr[1].set_title("RGB clustered")
    plt.show()
    
    #analsyes prawn colour
    print("Analysing prawn colour")
    kmeans.cluster_centers_
    if kmeans.cluster_centers_[1,2] > kmeans.cluster_centers_[1,1] and kmeans.cluster_ceners_[1,2] > kmeans.cluster_centers_[1,0]: #if cluster is mostly blue
        print("Error. Please try again. Ensure prawn is photographed against a monochrome backdrop")
    elif kmeans.cluster_centers_[1,0] > kmeans.cluster_centers_[1,1]: #if cluster is mostly red
        print("Prawn is Red")
    elif kmeans.cluster_centers_[1,0] < kmeans.cluster_centers_[1,1]: #if cluster is mostly green
        print("Prawn is Green") 
    print("")
