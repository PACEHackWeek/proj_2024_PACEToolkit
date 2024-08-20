# PACEToolkit - hackweek 2024

We are a team representing diverse end users of PACE data. During PACE Hackweek 2024, we collaborating on tools and tutorials that would help our end users access and use PACE data. 

See the Tutorials link in sidebar of our Jupyter Book or the `notenooks` folder for our tutorials developed during the hackweek. See the `scripts` folder for functions we created.

### Collaborators

| Name | Affiliation | Tutorial | Links |
| ------------- | ------------- | ------------- | ------------- |
| [Eli Holmes](https://github.com/eeholmes) | NOAA Fisheries, Office of Science and Technology  | Simple matchup on tracks  | [website](https://eeholmes.github.io/) |
| [Prem Maheshwarkar](https://github.com/pmaheshwarkar) | Universite Paris Est Creteil Val de Marne | Multi-source aerosol data visualization |  |
| [Thiago Nobrega](https://github.com/thiago-vg) | University of Sao Paulo | Re-gridding PACE data |  |
| [Bingqing Liu](https://github.com/bingqing-liu) |University of Louisiana Lafayette  |CyanoHABs  |  [HyperCoast](https://hypercoast.org/) [website](https://bingqingliu.com/) |
| [Jiaxu Zhang](https://github.com/JiaxuZ) | University of Washington (CICOES)/NOAA PMEL | Chl-a products of multiple sources  |  |
| [Rui Jin](https://github.com/RuiJinSZ) |  University of Washington (CICOES) | Simple PACE data manipulation  | [website](https://ruijinsz.github.io/)  |
| [Han Huynh](https://github.com/hnhuynh55) | University of Colorado at Boulder (CIRES)/NOAA CSL  |  Multi-source aerosol data visualization |   |

### Additional resources or background reading

* [Our JupyterBook](https://pacehackweek.github.io/proj_2024_PACEToolkit)
* [HyperCoast](https://hypercoast.org/)
* [EDM Workshop](https://nmfs-opensci.github.io/EDMW-EarthData-Workshop-2024/) -- similar tutorials
* [CoastWatch](https://github.com/coastwatch-training/CoastWatch-Tutorials) -- lots of Python tutorials on some typical science tasks with remote-sensing data


## Running notebook on CryoCloud

Note, all the earthaccess code will work fine on your laptop if you already have Python installed. We can edit `environment.yml` as we add needed modules. To clone this into the JupyterHub. Open a terminal (big button on the Launcher).

```
cd ~
git clone https://github.com/PACEHackWeek/proj_2024_PACEToolkit
```

To be able to push to the repo, run this from the terminal
```
gh-scoped-creds
```

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


## To add notebooks

1. Make sure your notebook has a markdown cell with a level 1 header at the top. For example
```
# My title
```
2. Do not include any html, like `<div>` or `<h1>` in your notebook. It will break the book build.
2. Add your notebook to the `notebooks` folder
3. Add your notebook to the `_toc.yml` file
4. Push to the repo and the book will automatically rebuild.
5. Watch the Actions tab on the repo to see when the rebuild is finished.
   
## To build book

Do `pip install ghp-import` if needed. Then build book and push to GitHub. Set Pages to use gh-pages branch.

```
jupyter-book build . --keep-going
ghp-import -n -p -f _build/html
```

  
