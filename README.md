# Crossy: Road Crossing Game

A 2D arcade game inspired by classic Frogger and Crossy Road, built purely with Python's native `turtle` module. Players navigate a turtle safely across busy multi-lane highways while avoiding oncoming vehicles that increase in speed with every successful level.



## Key Features
- **Dynamic Difficulty Scaling:** Traffic movement speed increases incrementally upon completing each level.
- **Randomized Traffic Generation:** Cars are instantiated dynamically at randomized intervals along vertical lanes with varying color attributes.
- **Precision Collision Detection:** Continuous distance monitoring between the player avatar and active car objects.
- **Flicker-Free Rendering:** manual screen updates to ensure clean visual transitions across frame refreshes.

## Controls

| Action | Key |
| :--- | :--- |
| **Move Up / Forward** | `Up Arrow` |

## Computer Science Concepts Applied
- **Object-Oriented Architecture (OOP):** Decoupled entities into distinct classes (`Pedestrian`, `Car`, `Level`) to enforce separation of concerns and maintainable code.
- **Frame-Rate Optimization:** Used `time.sleep` and `screen.update()` to suppress automatic animation repaints, eliminating screen flickering during complex multi-object updates.

### Prerequisites
- Python 3.x (Includes the standard `turtle` library)
