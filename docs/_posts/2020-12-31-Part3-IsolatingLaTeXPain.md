---
layout: post
title: "NoTeX Part 3 - Isolating LaTeX Pain Points"
date: 2020-12-23
published: true
---

## LaTeX - Pain Points and Architecture

### Pain

#### 1 - Errors and Debugging

In my experience a key frustration is hard-to-read errors and warnings, often due to unenclosed braces or missing delimiters etc. A more strongly linted schema to prevent errors waiting until compile time would be appreciated, and an error system optimized for readability is also a key upgrade.

#### 2 - Identifying the Tool for the Job

Often there are multiple ways of achieving the same result, or similar results with entirely different methods, and often the method to achieve a desired solution is hard to find.

### LaTeX Architecture - from [Stack](https://tex.stackexchange.com/questions/3274/latex-architecture-how-does-it-all-work)

#### A Quick Overview

LaTeX is a macro stack of several layers, and at its lowest layer consists of TeX primitives such as `\hbox` and `\vskip` that provide the basic document functionality.

Above this exists the LaTeX kernel, which provides macros such as `\usepackage` and `\begin` for more complex document management.

A standard document will begin with `\documentclass{x}` which will load another file containing more macros `x.cls`. These can use primitives, LaTeX macros or any other packages to provide these components.

Packages `.sty` are additional sets of macros that combine macros from lower levels. These are loaded in with `\usepackage`.

Documents are essentially a class file, used packages, and a collection of text and maths data. LaTeX has evolved over TeX with layers of diverse and expansive macro implementations.

#### Analysis

The macro architecture allows for massive extensibility, and the ability to use packages is almost baked into the fundamental nature of the application.

Multi-level macros do however have soe downsides:

- **Repeated Functionality** - Often there are multiple methods the achieve the same, or close to the same thing. This has often caused me trouble and confusion.
- **Abstraction** - Abstraction is great in creating a uniform user experience, but can hide the true functionality of the chosen commands, and make it difficult to identify the tool to do what is required.

This draws the conclusion that having an arguably more difficult entry for packages and extension would prevent repeated functionality from causing confusion.

*Further discussion in the section on **programmatic thoughts and language architecture**.
