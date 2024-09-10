# Example: London traffic

This is a simple application that downloads the map and traffic tiles for London, a 3x3 grid on zoom level 10.
These tiles are displayed on a simple html page which can be viewed in a browser.

Note that the tiles aren't checked in, you need to run this locally to see the results.

Run:

```
python examples/maps_london_traffic/download_tiles.py
```

Output:

```
ls -lah examples/maps_london_traffic/tiles
total 644K
.gitignore
incidents_10_510_339.png
incidents_10_510_340.png
incidents_10_510_341.png
incidents_10_511_339.png
incidents_10_511_340.png
incidents_10_511_341.png
incidents_10_512_339.png
incidents_10_512_340.png
incidents_10_512_341.png
main_10_510_339.png
main_10_510_340.png
main_10_510_341.png
main_10_511_339.png
main_10_511_340.png
main_10_511_341.png
main_10_512_339.png
main_10_512_340.png
main_10_512_341.png
```

Browser:

<img src="example.png" alt="Example" width="885"/>
