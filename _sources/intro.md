# proj_2024_PACEToolkit

We are a team representing diverse end users of PACE data. We will be collaborating on tools and tutorials that would help our end users access and use PACE data. 

See the Tutorials link in sidebar for our tutorials developed during the hackweek.

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
* [CoastWatch](https://github.com/coastwatch-training/CoastWatch-Tutorials) -- lots of Python tutorials on some typical science tasks with remote-sensing data
  
## To build book

Do `pip install ghp-import` if needed. Then build book and push to GitHub. Set Pages to use gh-pages branch.

```
jupyter-book build . --keep-going
ghp-import -n -p -f _build/html
```