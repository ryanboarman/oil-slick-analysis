# oil-slick-analysis
Ryan Boarman 2023 Capstone Project

[![DOI](https://zenodo.org/badge/637486224.svg)](https://zenodo.org/badge/latestdoi/637486224)



## Project Description


### The Devastating Impact of Oil Spills on Marine Wildlife:
The ecological impact of oil spills form ships and oil platforms on our oceans cannot be overlooked. As a major contributor to pollution, ships and oil platforms release a dangerous cocktail of contaminants, including oil spills, toxic chemicals, micro-plastics, and noise pollution. The consequences of chronic oil pollution are often downplayed, undetected, and unreported, with routine spills posing threats to marine wildlife.

In the North Sea, this concerning scenario is playing out, as oil platforms and ships encroach upon vital marine habitats causing irreversible habitat loss with potentially long recovery periods, if any recovery is possible at all. These habitats play a crucial role in nutrient cycling within the ocean, and their degradation poses a serious threat to this essential function. Adding to the distress, oil and gas activities are impacting the very foundation of marine food webs - plankton – through oil pollution.

Oil spills have devastating effects on marine mammals, impacting them in various ways. Direct contact with oil during swimming, ingestion of oil-contaminated prey, and inhalation of toxic vapors at the surface pose significant threats. These spills can lead to immediate deaths among marine mammals. These harmful consequences not only affect individual animals but also disrupt populations and entire ecosystems, underscoring the grave impact of oil spills on marine mammal species (Matkin et al., 2008). The oil spilled during these incidents possesses the capacity to be equally lethal to seabirds (Camphuysen et al., 2010).

I investigate the effects oil spills from offshore oil platforms and ships have on the North Sea’s wildlife, shedding light on the urgent need for more responsible and sustainable practices to safeguard our marine ecosystems.

### Vital Data Used

Two data sources were used for this analysis. Oil slick locations and species distribution maps.

**Oil slicks** were provided by SkyTruth. SkyTruth’s project Cerulean is an innovative algorithm designed to detect oil slicks using Synthetic Aperture Radar (SAR) imagery. The algorithm scans Sentinel-1 SAR imagery with a focus on vertical polarization emitted and received (VV) for dark, smooth areas that indicate oil slicks. SAR imagery is useful for this purpose because of its ability to penetrate clouds and its 6-day temporal resolution, allowing for timely and frequent acquisition of images. Additionally, the contrast between the surface scattering of radar pulses off the small wavelets in clean water versus the smoother, darker appearance of oil slicks on radar images makes SAR imagery a useful tool for detecting oil spills (SkyTruth, 2023). I used oil slicks from 2020 in the North Sea. I filtered the oil slick by category to only included "Infrastructure", "Vessel Old", "Recent", and "Adjacent.


**Species distribution** maps used in this analysis are from Waggitt et al. 2019. Waggit et al. 2019 generated monthly distribution models of cetaceans and seabirds. A comprehensive survey of the North-East Atlantic was conducted between 1980 and 2018, collecting 2.68 million km of data. The data was collated, standardized and used to create distribution maps for 12 cetacean and 12 seabird species. These models are at a resolution of 10 km2 and are at a monthly temporal scale.

Species distribution models were preprocessed and filtered to the study areas spatial and temporal resolution. After data cleaning, zonal statistics were generated from each oil spill resulting in an average animal per km2 value for each oil spill.

- *SkyTruth, 2023, https://skytruth.org*
- *Waggitt, J. J., Evans, P. G., Andrade, J., Banks, A. N., Boisseau, O., Bolton, M., ... & Hiddink, J. G. (2020). Distribution maps of cetacean and seabird populations in the North‐East Atlantic. Journal of Applied Ecology, 57(2), 253-269.*



### Benefits to society:
The research on oil spills in the North Sea will enhance our understanding of their ecological impact, guiding policymakers and industry practices towards more sustainable management, monitoring and conservation efforts. By raising public awareness and the importance of interdisciplinary collaboration, the findings will contribute to the protection of marine ecosystems, benefiting both human and marine life in the long run.


## Environment
  * [Start with instructions for installing the ea-python environment](https://www.earthdatascience.org/workshops/setup-earth-analytics-python/) 
  
  *  Ensure you have Jupyter Notebook installed to run the script.

## Repository Files and Their Roles

oil_spill_species_north_sea.ipynb: This Jupyter notebook contains the main analysis script. It fetches data, processes it, and outputs the results.
my_functions.py: Contains custom functions utilized in the main analysis script for processing and analyzing the data.
environment.yml: This file contains a list of all dependencies and packages required for the project, allowing users to easily recreate the necessary Python environment for running the scripts.


## Data Access
Data download is integrated into the script. The script contains URLs to download .geojson oil slicks and .asc species distribution maps. The script is designed to run in a Jupyter notebook.

## Collaborators and Acknowledgements
Oil spill data was provided by SkyTruth. www.skytruth.org
Species distribution models: Waggitt, James J., et al. "Distribution maps of cetacean and seabird populations in the North‐East Atlantic." Journal of Applied Ecology 57.2 (2020): 253-269.

## Citing this Work

If you use this work in your research or project, please cite it as:

Ryan Boarman. 2023 . Spilled Secrets: Uncovering the Effects of Oil Spills on the North Sea Ecosystem. Publisher. DOI 10.5281/zenodo.8099823
