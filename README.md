#  Python Data Analytics Task:

This asssignment is intended to extract some of the useful information from data collected about certain resource infrastructures.

The data is hosted at [This Place](https://raw.githubusercontent.com/onaio/ona-tech/master/data/water_points.json)

The information is eventually displayed in the format:

1. The number of water points that are functional,
2. The number of water points per community,
3. The rank for each community by the percentage of broken water points.


```json
{

  number_functional: …,

  number_water_points: {

    communityA: …,

  },

  community_ranking: …

}
```