import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cmocean

def plot_regional_map(dataset, min_lon, max_lon, min_lat, max_lat, 
                 title=None, colormap=cmocean.cm.thermal, vmin=-1.5, vmax=1.5, size=(5, 5), ax=None):
    """
    Plot a dataset within specified lat/lon boundaries.

    Parameters:
    dataset (xarray.DataArray): The data array to plot.
    min_lon (float): Minimum longitude.
    max_lon (float): Maximum longitude.
    min_lat (float): Minimum latitude.
    max_lat (float): Maximum latitude.
    title (str, optional): Title for the plot. Default is None.
    colormap (str, optional): Colormap for the plot. Default is cmocean.cm.thermal.
    vmin (float, optional): Minimum value for the color scale. Default is -1.5.
    vmax (float, optional): Maximum value for the color scale. Default is 1.5.
    size (tuple, optional): Figure size. Default is (5, 5).
    ax (matplotlib.axes._subplots.AxesSubplot, optional): Axis to plot on. Default is None.

    Returns:
    ax: The map handle.
    """
    
    # Calculate central longitude and latitude
    central_longitude = (min_lon + max_lon) / 2
    central_latitude = (min_lat + max_lat) / 2
    
    # Create a new figure if no axis is provided
    if ax is None:
        fig, ax = plt.subplots(figsize=size, subplot_kw={'projection': ccrs.LambertConformal(central_longitude=central_longitude, central_latitude=central_latitude)})
    
    # Set extent
    ax.set_extent([min_lon, max_lon, min_lat, max_lat], ccrs.PlateCarree())
    
    # Plotting using Matplotlib
    cf = dataset.plot(
        transform=ccrs.PlateCarree(), cmap=colormap,
        add_colorbar=False, vmin=vmin, vmax=vmax,
        ax=ax
    )
    
    # Color bar
    cbar = plt.colorbar(cf, ax=ax, fraction=0.027, pad=0.045, orientation="horizontal")
    clabel = f"{dataset.long_name}\n{dataset.units}"
    cbar.set_label(clabel, rotation=0, labelpad=5)
    cbar.ax.tick_params(labelsize=8)
    
    # Title
    if title:
        ax.set_title(title)
    
    # Plot lat/lon grid
    gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                      linewidth=0.1, color='k', alpha=1, linestyle='--')
    gl.top_labels = False
    gl.right_labels = False
    gl.xlabel_style = {'size': 8}
    gl.ylabel_style = {'size': 8}
    
    # Add coastlines
    ax.coastlines(linewidth=1)
    
    # Show plot if no axis is provided
    if ax is None:
        plt.show()
    
    # Return the map handle
    return ax