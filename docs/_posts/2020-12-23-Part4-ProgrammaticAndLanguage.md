---
layout: post
title: "NoTeX Part 4 - Programmatic Thoughts (DOM and language architecture)"
date: 2020-12-23
published: true
---

## Programmatic Thoughts (DOM and language architecture)

### Language Architecture

#### Document Construction Model

**The key question**, from a top level perspective to me is to balance the distribution of contents among source files.

Taking C as an example, distributing functions among several source files separated by functionality makes for a much clearer and more readable source, rather than stacking functions into a single file. Prose and reports are more readable by nature, as they naturally fall into a chronological formal, while software and functions often have no clear 'order' to be defined or necessarily used.
I was once told no function should require more than a single screen-height, i.e. one should be able to observe the functionality in its totality at once. The option to separate out chapters or subheadings as separate files and include them in a top level document is valuable, and something LaTeX is capable of doing.

LaTeX also uses a system of 'class' files, effectively a pre-formatting and template-ing system that includes custom macros.
What occurs to me as a peculiarity, is that the templates are pre-made and provided as is for basic users, while the more advanced users can create custom classes.
It makes sense to me to design a class system that intends to be modified, such that a new class file is created for each large project that decides generic things like margin sizes, page numbers etc [of course the option to override these on a page by page basis would also be required]. This should not forego the option to use a standard template as is for quick projects, but should encourage creating a custom template to change things like page margins.

The actual content of source and template files will be near identical, and is a problem bigger than I currently feel like solving.

#### Editor Input

**We** can be certain that a function character will be required to identify keywords from prose, for which LaTeX proposed the backslash `\`.

I propose either the pipe `|`, the *whatever this is* `¬`, the fullstop `.` or the backquote itself ~`~.

The first two are optimal as arguable the least frequently used glyphs on a keyboard, but both require pressing the shift key, which is slow.

Alternatively the full-stop and backtick both are immediately available, but more frequently needed in general prose.

In a moment of nostalgia, `;`, the semicolon may be workable option at the beginning of lines. However these are clearly used in prose so would require a dependance on newline or whitespace, which I am reluctant to do as a dependance on a new line brings up the issue of `\r` and `\n` and possible inconsistencies. Whitespace dependance should be limited to either none, or one or more as multiple white-spaces are difficult to differentiate.

**In summary - an operator shortlist**

- `|` ~ pipe
- `¬` ~ *this thing*
- `.` ~ Full-stop
- ` ~ Back Tick
- `;` ~ Semicolon

***I expect further evolution and choices about the language format to be made through use testing and the creation of the tool itself***
