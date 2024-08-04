# Example: Routing landmarks

This is a simple application that generates a route between various landmarks in the United States and displays the distance and travel time between them.
The landmarks used in this example are the Statue of Liberty, Grand Canyon, Mount Rushmore National Memorial, Golden Gate Bridge, and Times Square.

Run:

```
python examples/routing_landmarks/routing.py
```

Output:

```
Planning a route from Statue of Liberty to Grand Canyon:
3962km with a travel time 37 hours 10 minutes, currently 5 minutes delay

Planning a route from Statue of Liberty to Mount Rushmore National Memorial:
2813km with a travel time 25 hours 42 minutes, currently 5 minutes delay

Planning a route from Statue of Liberty to Golden Gate Bridge:
5055km with a travel time 44 hours 18 minutes, currently 5 minutes delay

Planning a route from Statue of Liberty to Times Square:
20km with a travel time 1 hours 12 minutes, currently 2 minutes delay

Planning a route from Grand Canyon to Mount Rushmore National Memorial:
1684km with a travel time 17 hours 47 minutes, currently 0 minutes delay

Planning a route from Grand Canyon to Golden Gate Bridge:
1292km with a travel time 13 hours 40 minutes, currently 0 minutes delay

Planning a route from Grand Canyon to Times Square:
3910km with a travel time 36 hours 4 minutes, currently 1 minutes delay

Planning a route from Mount Rushmore National Memorial to Golden Gate Bridge:
2203km with a travel time 19 hours 24 minutes, currently 2 minutes delay

Planning a route from Mount Rushmore National Memorial to Times Square:
2780km with a travel time 23 hours 59 minutes, currently 0 minutes delay

Planning a route from Golden Gate Bridge to Times Square:
4718km with a travel time 40 hours 40 minutes, currently 6 minutes delay
```
