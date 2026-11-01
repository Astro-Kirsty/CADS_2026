# Hands-on sessions for the advanced users

The used Gammapy version will be the **v2.1**. See the installation page
[here](https://docs.gammapy.org/2.1/getting-started/index.html#recommended-setup).

**Disclaimer** : still under construction!

Locations:
- Wednesday: Salle CIAS, Observatoire de Meudon ([OpenStreeMap](https://www.openstreetmap.org/note/new?lat=48.805069&lon=2.230761#map=17/48.805092/2.231694&layers=N))
- Thursday: Observatoire de Paris, 77 Av. Denfert Rochereau, Paris

## Table of contents
1. [Gammapy in depth](#intro)
2. [Joint analyses](#joint)
3. [Systematic uncertainties](#sys)
4. [Project or source detection](#project-1)
5. [Timing analysis](#timing)
6. [Model selection and Bayesian analyses](#nested)
7. [GAMERA](#gamera)
8. [Project or Machine-learning representation of physical models](#project-2)

<a name="intro"></a>
## Session of Wednesday, 9h30/10h45
**Gammapy in Depth** : the data analysis workflow, the GADF data format, makers and estimators, models and catalogs, 
multi-processing (multi-core and multi-CPU), etc.

Made by Régis Terrier (APC, Paris). Location : room CIAS, Observatoire de Meudon

- Notebooks : xxx
- Open exercises : xxx

<a name="joint"></a>
## Session of Wednesday, 11h15/12h30
**Joint analyses**
Made by Quentin Remy (IRAP, Toulouse). Location : room CIAS, Observatoire de Meudon

***Fermi-LAT analysis*** :
datasets creation, source catalog, diffuse emission

[Link to the notebook](2a_fermi_lat_analysis.ipynb)

***IACTs data reduction (H.E.S.S. example)*** :
observation handling, IRFs, safe mask, exclusion masks, background fitting, diffuse emission

[Link to the notebook](2b_hess_data_reduction.ipynb)


### Joint analysis
TS and significance maps, fitting

[Link to the notebook](3a_joint_analysis_ts_maps)

<a name="sys"></a>
## Session of Wednesday, 14h00/15h45
**Systematic uncertainties**
Made by Kirsty Feijen (APC, Paris) and Quentin Remy (IRAP, Toulouse). Location : room CIAS, Observatoire de Meudon

### Systematics uncertainties estimates from Jackniffe tests (data perturbations)
***Observation leave-k-out:***
 How sensitive is the fit to the removal of a randomly selected observation?
 
 Probes the stability of the fit with respect to observation-to-observation variability, including potential unknown systematic effects.
 
 [Link to the notebook](jackknife_observations.ipynb)


***Random FoV masking:***
 How sensitive is the fit to the removal of a randomly selected subset of the field of view?
 
 Probes the stability of the fit with respect to spatially localized systematic effects, such as diffuse-model mismatches, acceptance uncertainties, or residual background structures.
 
 [Link to the notebook](jackknife_pixels.ipynb)


### Systematic uncertainty propagation through model variations (model perturbations)
**Multi-instrument energy-scale systematic:**
How sensitive is the fit to uncertainties in the relative energy calibration of the instruments?

Probes the stability of the fit with respect to inter-instrument energy-scale systematic effects, such as calibration biases, atmospheric uncertainties, and instrumental response mismatches, introducing a nuisance parameter in the fitted models

[Link to the notebook](joint_energy_scale_systematics.ipynb)

**Alternative IRF models:**
 How sensitive are the source parameters to uncertainties in the instrument response, and other model components?
 
 Propagates IRFs-related systematic uncertainties by repeating the fit with alternative IRFs and marginalising over the results. 
- Notebook : xxx

<a name="project-1"></a>
## Session of Wednesday, 16h15/18h
**Project Session** : multiple options, each to be selected individually and supervised by the Gammapy experts. Location : room CIAS, Observatoire de Meudon
- Individual follow-up study of the tutorials covered this morning,
- Personal project,
- or *Source detection using pattern recognition techniques*, prepared by Quentin Remy (IRAP, Toulouse).

  [Link to the notebook](3b_joint_analysis_sources_detection.ipynb)

<a name="timing"></a>
## Session of Thursday, 9h30/10h45
**Timing Analysis** : handling light curves. Made by Jean-Philippe Lenain (LPNHE, Paris). Location : room Danjon, Observatoire de Paris

[Link to the notebook](./5.%20Timing%20analysis/exercise.ipynb)

<a name="nested"></a>
## Session of Thursday, 11h15/12h30
**Model selection and bayesian analyses** : Made by Quentin Remy (IRAP, Toulouse). Location : room Danjon, Observatoire de Paris

### Nested sampling utilities

[Link to the notebook](nested_sampling.ipynb)

  
### Alternative hypotheses testing, bayesian model selection

[Link to the notebook](bayesian_model_selection.ipynb)


<a name="gamera"></a>
## Session of Thursday, 14h00/15h45
**GAMERA** : adjust data with a physically-motivated modeling library. Made by Laura Olivera-Nieto (APIA, Amsterdam). Location : room Danjon, Observatoire de Paris

- Notebooks : xxx

<a name="project-2"></a>
## Session of Thursday, 16h15/18h
**Project Session** : multiple options, each to be selected individually and supervised by the Gammapy experts. Location: Room Danjon, Observatoire de Paris
- Individual follow-up study of the tutorials covered this morning,
- Personal project,
- or *Machine-learning representation of physical models* (Custom models, ML surrogate model training), prepared by Quentin Remy (IRAP, Toulouse) and  Lea Heckmann (APC, Paris). 

[Link to the Naima surrogate notebook](NaimaSurrogate.ipynb)
[Link to the pytorch power-law notebook](PyTorchEmulator)
