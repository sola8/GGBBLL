# GGBBLL 

This is where all the scripts and exports used to manage GGBBLL are located.

The **exports** are all compressed, and are still being updated with each sim.

As of 6/20/21 - The **scripts** are complete!

## Assignments

The **assignments** script:
- Opens up two exports
  - Grabs all current players from source export
- Takes all players listed in ```.txt``` file, and matches names with names in source export
  - If match, take player's ```json```, and move to destination export
- Creates new file with new players in watchlist

## Points

The **points** script:
- Opens up two exports
  -  Creates a ```dict``` of all teams and their ```tid```
- Loops through all players in GGBBLL watchlist to calculate their **Training Points**
- Created players have a different formula, than normal players.
