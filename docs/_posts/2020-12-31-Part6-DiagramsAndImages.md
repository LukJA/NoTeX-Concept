---
layout: post
title: "NoTeX Part 5 - Diagrams and Images"
date: 2020-12-31
published: false
---

## Diagrams and Images

When it comes to writing reports, diagrams sketches and pictures are 'worth a thousand words'. The problem is always that quickly sketching a situation is much, much faster than creating the equivalent.

For this reason, **the ability to quickly and clearly generate diagrams and sketches is the main reason I wanted to begin to work on this concept.** Hence development will begin with the diagram component, and the development of this component will act as a precursor and a playground in which features of the broader NoTeX tool can be tested and conceptualized.

### Python Application Distribution

#### Overview

Firstly why python? Distribution and build would likely be far simpler with C++ and CMake, but I've done that before, and python distribution is a new challenge. Plus, python handles strings without complaining nearly as much as C does...

The interface will be a command-line invocation against a source file, and will produce 1 (or more) SVG output files. The first step is to consider how best to package and distribute such an executable.

As Python3 will be the initial dev environment of choice, [Python Packaging](https://packaging.python.org/overview/) seems like a good place to start. For discrete application deployment a number of levels of packaging are available, a few of which are as follows:

[PEX](https://pex.readthedocs.io/en/latest/buildingpex.html)

[pyinstaller](http://www.pyinstaller.org/)

[Appimage](https://docs.appimage.org/index.html)

[Snap](https://snapcraft.io/docs)

The ability to integrate the tool into the broader NoTeX application must also be considered when deciding on a build process.

The distribution options broadly go from raw python file through to a containerized app environment [appimage and snap]. For the sake of simplicity, and as is outlined in [this post](https://discourse.appimage.org/t/how-to-create-an-appimage-from-start-to-finish-from-a-python-project/1375) Appimages seem like the simplest option from an end user perspective (aside from the need to make them executable and path them...), plus it avoids the issues around snaps relating to the power Canonical holds over their maintenance and distribution. Maybe we can build both at some point.

However, making python appimages seems... [complex](https://github.com/AppImage/AppImageKit/wiki/Bundling-Python-apps), but possible! see [For Developers](https://github.com/niess/python-appimage#for-applications-developers). An example appimage python tool exists [https://github.com/xonsh/xonsh](https://github.com/xonsh/xonsh). By contrast Snaps have a specific python plugin and support from the very start.

#### Looking at Xonsh Appimage Build

Xonsh uses the [python-appimage](https://github.com/niess/python-appimage#for-applications-developers) tool to create and package the tool with a pre-made appimage executable - neat!

From the Xonsh docs:

> The best way to build xonsh AppImage in 5 minutes is to using python-appimage:

```bash
mkdir -p /tmp/build && cd /tmp/build
git clone --depth 1 https://github.com/xonsh/xonsh
cd xonsh/appimage
echo 'xonsh' > requirements.txt
cat pre-requirements.txt >> requirements.txt  # here you can add your additional PyPi packages to pack them into AppImage
cd ..
pip install git+https://github.com/niess/python-appimage
python -m python_appimage build app ./appimage
./xonsh-x86_64.AppImage
```

