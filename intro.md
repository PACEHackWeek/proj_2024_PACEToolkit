# proj_2024_PACEToolkit

We are a team representing diverse end users of PACE data. We will be collaborating on tools and tutorials that would help our end users access and use PACE data. 

See the Tutorials link in sidebar for our tutorials developed during the hackweek.

### Collaborators

| Name | Affiliation | Tutorial | Links |
| ------------- | ------------- | ------------- | ------------- |
| [Eli Holmes](https://github.com/eeholmes) | NOAA Fisheries, Office of Science and Technology  | Simple matchup on tracks  | [website](https://eeholmes.github.io/) |
| [Prem Maheshwarkar](https://github.com/pmaheshwarkar) | Universite Paris Est Creteil Val de Marne | Visualization multi-source aerosols |  |
| [Thiago Nobrega](https://github.com/thiago-vg) | University of Sao Paulo | More re-gridding |  |
| [Bingqing Liu](https://github.com/bingqing-liu) |  |  |  [HyperCoast](https://hypercoast.org/) |
| [Jiaxu Zhang](https://github.com/JiaxuZ) | University of Washington (CICOES)/NOAA PMEL | Chl-a products of multiple sources  |  |
| [Rui Jin](https://github.com/RuiJinSZ) |  University of Washington (CICOES) | Simple re-grid  |   |
| [Han Huynh](https://github.com/hnhuynh55) | University of Colorado at Boulder (CIRES)/NOAA CSL  |  Visualization multi-source aerosols |   |


### Additional resources or background reading

* [HyperCoast](https://hypercoast.org/)
* [EDM Workshop](https://nmfs-opensci.github.io/EDMW-EarthData-Workshop-2024/) -- tutorials that we can adapt
* [CoastWatch](https://github.com/coastwatch-training/CoastWatch-Tutorials) -- lots of Python tutorials on some typical science tasks with remote-sensing data
  
## To build book

Do `pip install ghp-import` if needed. Then build book and push to GitHub. Set Pages to use gh-pages branch.

```
jupyter-book build . --keep-going
ghp-import -n -p -f _build/html
```