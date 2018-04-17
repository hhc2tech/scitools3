# SciTools

SciTools was a Python package containing many useful tools for scientific
computing in Python, built on top of other widely used
packages such as NumPy, SciPy, ScientificPython, Matplotlib, Gnuplot,
VisIt, etc.

However, the library only supported Python 2. With this newer version of
scitools, I plan to remove Python 2 support completely and focus on porting
useful existing modules of the package to Python 3.

When the time is ready, I will include these versions of the scitools modules
in Python package `sciren`. Maybe, when you are reading this, the time is
already long ready (or long gone), then you will find out about sciren on
this website: https://onnoeberhard.com/sciren

### Update 2018-05-17
I will abandon all work on this project (there hasn't been a lot), because I
realize most modules are either not useful anymore, not really useful in general,
or functions are better implemented in larger open source projects.
Because of this, this is as far as I will go with the scitools project; if I find
that certain functions or classes are indeed useful, I will make sure to include
them in the sciren package and mark them accordingly :)

## Credits

The original version of this package was developed by these lovely people:

SciTools was initially mainly developed by Hans Petter Langtangen
<hpl@simula.no> for his book "Python Scripting for Computational
Science" (Springer, 1st edition 2003, 3rd edition 2009).
The Easyviz package was mainly developed by Johannes H. Ring
<johannr@simula.no>. Johannes H. Ring has been the principal
maintainer of SciTools. The package was extended for the
book "A Primer on Scientific Programming with Python", bu H. P. Langtangen,
4th edition, Springer, 2014.

Some modules included in SciTools are written by others:

 * Allen B. Downey <downey@allendowney.com> wrote Lumpy.py and Gui.py
 * Imri Goldberg <lorgandon@gmail.com> wrote aplotter.py
 * Fred L. Drake, Jr. <fdrake@acm.org> wrote pprint2.py
 * Gael Varoquaux <gael.varoquaux@normalesup.org> wrote pyreport

Code contributors include:

 * Rolv E. Bredesen <rolveb@simula.no>
 * Joachim B. Haga <jobh@simula.no>
 * Mario Pernici <Mario.Pernici@mi.infn.it>
 * Ilmar Wilbers <ilmarw@simula.no>
 * Arve Knudsen <arvenk@simula.no>

## License

SciTools is licensed under the new BSD license, see the LICENSE file.

Lumpy.py and Gui.py are licensed under GPL, however, permission is
granted by Allen Downey to include these under a BSD license.
