# Concurrent Hello World in PBP (Parts Based Programming) - Python version

This looks very simple, but contains concurrency and parallelism and a way to reason about mevent (message-event) ordering.

![hello world source code](helloworld.drawio.png)

2 Parts to make Hello World.

A 3rd Part to guarantee ordering of mevents.

# Usage
clone the [repo](https://github.com/guitarvydas/pbp_helloworld_py) and cd into the new directory
`make init`
`make`

View the source code by opening `helloworld.drawio` in the [drawio](https://www.drawio.com) editor and `hello.py` and `world.py` in a programmers' text editor

# Do It Yourself

If you'd like to build a PBP project from scratch, I recommend using the pbp-kit template to create a fresh repo, then creating your own version of the drawing and running `make`.

## Links
- https://github.com/guitarvydas/pbp-kit PBP kit template
- https://github.com/guitarvydas/pbp_helloworld finished project in video
- https://www.drawio.com Draw.io diagram editor

## Video

There is no video for building the Python version from scratch. You are referred to the first-principles video for setting up a PBP project. From there, you can manually edit the two Python parts (`hello.py` and `world.py`) and import them and install them in `main.py`. (See `main.py` in this repo for an example of what the final DIY version of `main.py` needs to look like).

This [video](https://www.youtube.com/watch?v=EFTzFA82YRc&list=PLHh2_dCKBPjbBN2R8xwBiS4nHlo5iQjqS&index=1) shows how to build this version of hello world from first principles. It begins with drawing a sequential pipeline, then moves on to parallelizing it, then inserting a `1→2` part to specify order. Note that, traditional programming languages hard-wire order into code (top down, left to right), PBP lifts ordering to where a programmer/artchitect can deal with it explicitly. In this simple example, this makes it look like programming this way is "more difficult", but, it opens the door up to other kinds of programming solutions that are not (easily) available with traditional programming languages. The power of allowing programmers to specify order becomes apparent only in larger solutions.




## Steps
- create new project using the pbp-kit template
- git clone the project locally
- cd into the new project
- edit Makefile - change `???` to `helloworld`
- `make init`
- open draw.io (see above to download and install) and name the drawing `helloworld`
- change name of tab to `main` (arbitrary name, but must correspond with argv 3 of python line in Makefile)
- `make`

# UTF-8
Some of the Part names contain Unicode. 

You may need to enable Unicode before running `make` using this version of PBP.

In Linux/Mac:
`export PYTHONUTF8=1`

In Windows:
`set PYTHONUTF8=1`

![API](./pbp/api.md)

# See Also 
- [hello world from first principles](https://github.com/guitarvydas/pbp_helloworld)
- [hello world using Python](https://github.com/guitarvydas/pbp_helloworld_py) <-- the same as this repo that you are currently looking at
- [hello world using node.js](https://github.com/guitarvydas/pbp_helloworld_nodejs)
- [LLM as a PBP Part (5 Whys project)](https://github.com/guitarvydas/pbp-llm)
- the [PBP kernel](https://github.com/guitarvydas/pbp-dev) itself (advanced use of the PBP technique) 
- [mevent flow basics](https://www.youtube.com/watch?v=yPg4wVRQfYE&list=PLHh2_dCKBPjbBN2R8xwBiS4nHlo5iQjqS&index=2)
