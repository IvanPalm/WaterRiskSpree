import ee
from ee_plugin import Map

ee.Initialize()

pop = ee.ImageCollection("WorldPop/GP/100m/pop").filterBounds(hydrobasins_europe);

popVisParams = {
  bands: ['population'],
  min: 0.0,
  max: 50.0,
  palette: ['24126c', '1fff4f', 'd4ff50']
};

# set center of map on Mediterranean
Map.centerObject(hydrobasins_europe)

# add pop layer
Map.addLayer(pop, popVisParams, "Population")