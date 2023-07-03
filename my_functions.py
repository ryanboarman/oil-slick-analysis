import os
import requests
import numpy as np


def download_oil_data(urls, filenames):
    """
    Download data from a list of URLs and save it to local files.

    Parameters:
    urls (list of str): A list of URLs to download data from.
    filenames (list of str): A list of filenames to save the downloaded data to.

    Returns:
    None
    """
    
    # Create the download folder if it doesn't exist
    download_folder = 'data'
    os.makedirs(download_folder, exist_ok=True)

    for url, filename in zip(urls, filenames):
        file_path = os.path.join(download_folder, filename)  # Build the file path
        
        # Check if the file already exists
        if os.path.exists(file_path):
            print(f"File '{filename}' already exists. Skipping download.")
            continue

        response = requests.get(url)

        with open(file_path, "wb") as file:
            file.write(response.content)
        
        print(f"File '{filename}' downloaded successfully.")





def calculate_geometry_stats(data_dict, species_id, month, all_countries_gdf_allcat_clipped):
    """
    Calculate geometry statistics for a selected array based on species_id and month,
    and apply the statistics to a GeoDataFrame of clipped geometries.
    
    Parameters:
        data_dict (dict): A dictionary of arrays containing the data for different species and months.
        species_id (str): The ID of the species.
        month (str): The month for which the statistics are calculated.
        all_countries_gdf_allcat_clipped (GeoDataFrame): The GeoDataFrame containing the clipped geometries.

    Returns:
        GeoDataFrame: A new GeoDataFrame with added columns for the calculated geometry statistics.
    """
    
    # Create the key from species_id and month
    key = f"{species_id}_{month}"
    
    # Check if the key exists in data_dict
    if key not in data_dict:
        raise ValueError(f"No data found for species_id: {species_id}, month: {month}")
    
    # Get the selected array from data_dict based on the key
    selected_array = data_dict[key]
    
    # Filter rows in all_countries_gdf_allcat_clipped based on the month
    filtered_rows = all_countries_gdf_allcat_clipped.loc[
        all_countries_gdf_allcat_clipped['grd__starttime'].dt.month == int(month)
    ].copy()  # Create a copy of the filtered rows
    
    # Create blank lists for min, max, mean
    min_vals = []
    max_vals = []
    mean_vals = []

    # Loop through each geometry in the filtered GeoDataFrame
    for i, row in filtered_rows.iterrows():

        # Initialize min, max, and mean values to NaN
        min_val = np.nan
        max_val = np.nan
        mean_val = np.nan
        try:
            # Clip the raster to the geometry
            clipped = selected_array.rio.clip([row.geometry], all_touched=True)

            # Mask out negative values
            clipped = clipped.where(clipped >= 0)

            # Compute the desired statistics for the clipped raster
            min_val = clipped.min().values
            max_val = clipped.max().values
            mean_val = clipped.mean().values

        except rxr.exceptions.NoDataInBounds:
            # If there is no data in the bounds of the geometry, set min, max, and mean values to NaN
            min_val = np.nan
            max_val = np.nan
            mean_val = np.nan

        # Append the min, max, and mean values to their respective lists
        min_vals.append(min_val)
        max_vals.append(max_val)
        mean_vals.append(mean_val)

    # Assign the min, max, and mean values to the copied GeoDataFrame
    filtered_rows['min_val'] = min_vals
    filtered_rows['max_val'] = max_vals
    filtered_rows['mean_val'] = mean_vals
    
    return filtered_rows