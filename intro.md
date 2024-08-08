# PACEToolkit

<img src="qr-pace.png" alt="QR" style="width:70px; float: right"/>

We are a team representing diverse end users of PACE data. During PACE Hackweek 2024, we collaborating on tools and tutorials that would help our end users access and use PACE data. 

See the Tutorials link in sidebar for our tutorials developed during the hackweek. See the `scripts` folder for functions we created.

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

* [HyperCoast](https://hypercoast.org/)
* [EDM Workshop](https://nmfs-opensci.github.io/EDMW-EarthData-Workshop-2024/) -- tutorials that we can adapt
* [CoastWatch](https://github.com/coastwatch-training/CoastWatch-Tutorials) -- lots of Python tutorials on some typical science tasks with remote-sensing data

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
