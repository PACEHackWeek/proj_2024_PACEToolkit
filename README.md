# PACEToolkit - hackweek 2024

## Files and folders

* **`contributors/`**
<br> Each team member can create their own folder under contributors, within which they can work on their own scripts, notebooks, and other files. Having a dedicated folder for each person helps to prevent conflicts when merging with the main branch. This is a good place for team members to start off exploring data and methods for the project.
* **`notebooks/`**
<br> Notebooks that are considered delivered results for the project should go in here.
* **`scripts/`**
<br> Code that is shared by the team should go in here (e.g. functions or subroutines). These will be files other than Jupyter Notebooks such as Python scripts (.py).
* `.gitignore`
<br> This file sets the files that will be globally ignored by `git` for the project. (e.g. you may want git to ignore temporary files or large data files, [read more about ignoring files here](https://docs.github.com/en/get-started/getting-started-with-git/ignoring-files))
* `environment.yml`
<br> `conda` environment description needed to run this project.
* `README.md`
<br> Description of the project (see suggested headings below)
* `model-card.md`
<br> Description (following a metadata standard) of any machine learning models used in the project

## Tools and tutorials for end users

We are a team representing diverse end users of PACE data. We will be collaborating on tools and tutorials that would help our end users access and use PACE data. 

Ideas:

* Given a track (e.g. KML file) get PACE data and output in a format familiar to the end user
* Create a data cube that is ready for a machine-learning or statistics application. Save in a format familiar for end users.
* Take the [earthaccess tutorial](https://pacehackweek.github.io/pace-2024/presentations/hackweek/earthdata_cloud_access.html) and re-write using data for one of our end user groups.
* Make a tutorial showing how to re-grid level-3 PACE data so that it can be used with model data on a different grid.
* Make a tutorial showing how to create a time-series for a region defined by a shape file. Combine [this](https://nmfs-opensci.github.io/EDMW-EarthData-Workshop-2024/tutorials/python/3-extract-satellite-data-within-boundary.html) and [this](https://nmfs-opensci.github.io/EDMW-EarthData-Workshop-2024/tutorials/python/4-data-cubes.html)
* Make a time series comparing PACE Chl-a and some other Chl-a product.
  
### Collaborators

| Name | Affiliation | Interests and end users | Links |
| ------------- | ------------- | ------------- | ------------- |
| [Eli Holmes](https://github.com/eeholmes) | NOAA Fisheries, Office of Science and Technology  | Fisheries scientists who want time series and point values to match tracks.  | [website](https://eeholmes.github.io/) |
| [Prem Maheshwarkar](https://github.com/pmaheshwarkar) |  |  |  |
| [Thiago Nobrega](https://github.com/thiago-vg) |  |  |  |
| [Bingqing Liu](https://github.com/bingqing-liu) |  |  |  [HyperCoast](https://hypercoast.org/) |
| [Jiaxu Zhang](https://github.com/JiaxuZ) | |  |  |
| [Rui](https://github.com/RuiJinSZ) |   |   |   |
| [Han Huynh](https://github.com/hnhuynh55) |   |   |   |


### Additional resources or background reading

* [HyperCoast](https://hypercoast.org/)
* [EDM Workshop](https://nmfs-opensci.github.io/EDMW-EarthData-Workshop-2024/) -- tutorials that we can adapt
* [CoastWatch[(https://github.com/coastwatch-training/CoastWatch-Tutorials) -- lots of Python tutorials on some typical science tasks with remote-sensing data
  
<!--
## Project goals and tasks

### Project goals

List the specific project goals or research questions you want to answer. Think about what outcomes or deliverables you'd like to create (e.g. a series of tutorial notebooks demonstrating how to work with a dataset, results of an anaysis to answer a science question, an example of applying a new analysis method, or a new python package).

* Goal 1
* Goal 2
* ...

### Tasks

What are the individual tasks or steps that need to be taken to achieve each of the project goals identified above? What are the skills that participants will need or will learn and practice to complete each of these tasks? Think about which tasks are dependent on prior tasks, or which tasks can be performed in parallel.

* Task 1 (all team members will learn to use GitHub)
* Task 2 (team members will use the scikit-learn python library)
  * Task 2a (assigned to team member A)
  * Task 2b (assigned to team member B)
* Task 3
* ...

## Project Results

Use this section to briefly summarize your project results. This could take the form of describing the progress your team made to answering a research question, developing a tool or tutorial, interesting things found in exploring a new dataset, lessons learned for applying a new method, personal accomplishments of each team member, or anything else the team wants to share.

You could include figures or images here, links to notebooks or code elsewhere in the repository (such as in the [notebooks](notebooks/) folder), and information on how others can run your notebooks or code.
-->
