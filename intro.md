# PACEToolkit

We are a team representing diverse end users of PACE data. During PACE Hackweek 2024, we collaborating on tools and tutorials that would help our end users access and use PACE data. 

See the Tutorials link in sidebar for our tutorials developed during the hackweek. See the `scripts` folder for functions we created.

### Collaborators

| Name | Affiliation | Tutorial | Links |
| ------------- | ------------- | ------------- | ------------- |
| [Eli Holmes](https://www.linkedin.com/in/elizabeth-eli-holmes-354b76/) | NOAA Fisheries, Office of Science and Technology  | Simple matchup on tracks  | [<i class="fa-solid fa-envelope"></i>](mailto:eli.holmes@noaa.gov) [<i class="fa-brands fa-orcid"></i>](https://orcid.org/0000-0001-9128-8393) [<i class="fa-solid fa-globe"></i>](https://eeholmes.github.io/) [<i class="fa-brands fa-github"></i>](https://github.com/eeholmes) |
| [Prem Maheshwarkar](https://www.linkedin.com/in/prem-maheshwarkar-78b263128/?originalSubdomain=fr) | Universite Paris Est Creteil Val de Marne | Multi-source aerosol data visualization | [<i class="fa-brands fa-orcid"></i>](https://orcid.org/0000-0001-6708-7460) [<i class="fa-brands fa-github"></i>](https://github.com/pmaheshwarkar) |
| Thiago Nobrega | University of Sao Paulo | Re-gridding PACE data | [<i class="fa-brands fa-github"></i>](https://github.com/thiago-vg) |
| [Bingqing Liu](https://www.linkedin.com/in/bingqing-liu-02492027a/) |University of Louisiana Lafayette  |CyanoHABs  |  [HyperCoast](https://hypercoast.org/) [<i class="fa-solid fa-globe"></i>](https://bingqingliu.com/)  [<i class="fa-brands fa-orcid"></i>](https://orcid.org/0000-0003-4651-6996) [<i class="fa-brands fa-github"></i>](https://github.com/bingqing-liu) |
| [Jiaxu Zhang](https://www.linkedin.com/in/jiaxuzhang/) | University of Washington (CICOES)/NOAA PMEL | Chl-a products of multiple sources  | [<i class="fa-solid fa-globe"></i>](https://www.pmel.noaa.gov/people/dr-jiaxu-zhang) [<i class="fa-brands fa-orcid"></i>](https://orcid.org/0000-0002-8564-3026) [<i class="fa-brands fa-github"></i>](https://github.com/JiaxuZ) |
| Rui Jin |  University of Washington (CICOES) | Simple PACE data manipulation  | [<i class="fa-solid fa-globe"></i>](https://ruijinsz.github.io/) [<i class="fa-brands fa-orcid"></i>](https://orcid.org/0000-0001-9853-127X) [<i class="fa-brands fa-github"></i>](https://github.com/RuiJinSZ) |
| [Han Huynh](https://www.linkedin.com/in/hannhuynh/) | University of Colorado at Boulder (CIRES)/NOAA CSL  |  Multi-source aerosol data visualization |  [<i class="fa-solid fa-globe"></i>](https://cires.colorado.edu/people/han-huynh) [<i class="fa-brands fa-orcid"></i>](https://orcid.org/0000-0002-2467-7134) [<i class="fa-brands fa-github"></i>](https://github.com/hnhuynh55) |


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
