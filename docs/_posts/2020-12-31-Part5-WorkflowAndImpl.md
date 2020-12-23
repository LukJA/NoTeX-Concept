---
layout: post
title: "NoTeX Part 5 - Workflow and Software Implementation"
date: 2020-12-31
published: false
---

## Software Implementation

Although likely not the most sensible choice, - a functional language like **OCaml** would probably do a better job - **Python3** offers a very readable, quick and hopefully **contributive** option.

## Workflow

Initially it seems sensible to build an extension rather than an IDE equivalent, with **VSCode** the clear choice.

### Source Structure

In general files can be stored in **any tree structure** as long as the top level source file is at the top level of the tree [the file that will be passed to the program], overall:

- Source files will be basic text files with the `.ntx` extension [this seems to be uncommon at best].
- Template files will be basic

### Final Build

`notex build -f filename.ntx` -> `filename.pdf` [with errors sent to stderr].

This is my first concept of what I would see as a convenient and clear build process, and leaves open room for additional functionality. A distributed executable to run from a task inside a VSCode extension would be fairly simplistic to implement.

`build` may be omitted for succinctness, and other arguments that need to be considered:

- A 'build' directory should any cached files need to be stored during the construction process
- The name of the PDF to be created.
- The source tree should there be multiple required source files to build from.

### Linting / pre-processor

VSCode provides a special interface known as a language server:

> Language Server is a special kind of Visual Studio Code extension that powers the editing experience for many programming languages. With Language Servers, you can implement autocomplete, error-checking (diagnostics), jump-to-definition, and many other language features supported in VS Code.
>
> In VS Code, a language server has two parts:
>
>Language Client: A normal VS Code extension written in JavaScript / TypeScript. This extension has access to all VS Code Namespace API.
>
>Language Server: A language analysis tool running in a separate process.

Although a task, this appears the easiest option.

### Prose

The tool is at heart designed to be a wordprocessors, so should respect a natural prose typing experience - new line is new line, space is space and so on

### Maths

The plan would be to replicate the standard .md and LaTeX mathematic notation, possibly extending some features that packages are required for, such as bolding individual characters.

### Diagrams

See the next post.
