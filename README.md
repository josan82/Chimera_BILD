# Chimera_BILD
Implementation of some BILD format commands as a Chimera extension, to work directly with them in the Chimera's command line.


Installation (Linux):
-------------

1 - If you don't have Chimera installed, download the [latest stable copy](http://www.cgl.ucsf.edu/chimera/download.html) and install it with:

``chmod +x chimera-*.bin && ./chimera-*.bin``

2 - If you don't have git installed, install it with:

``sudo apt-get install git``

3 - Install the chimera_BILD extension with pip (substituting ``<$PATH>`` by the path where you want the extension to be installed):

``pip install -U git+https://github.com/josan82/Chimera_BILD.git -t <$PATH>``

4 - Register the chimera_BILD extension in UCSF Chimera: You have to add the ``<$PATH>`` where you installed the extension in ``Favorites -> Preferences -> Category:Tools`` dialog of UCSF Chimera.

Usage of the commands:
----------------------

- In all commands, the ``color`` parameter can be set as a name or as a RGB code:
The name can be a built-in name, a name defined previously with colordef, or an integer that refers to the old BILD color wheel (0-65, inclusive). Alternatively, a color can be described by its red (r), green (g), and blue (b) components, each in the range 0-1, inclusive. Any transparency in the color is ignored, but transparency can be set separately.

- In all commands, the ``transparency`` parameter (optional, default 0) can be set with a value of a range from 0.0 (not transparent) to 1.0 (completely transparent).

- In all commands, the id of the Chimera's object that will be created can be set with an integer value with the optional paremeter ``id`` (default 100).

For now, the following commands are implemented to use in the command line of UCSF Chimera:

``arrow x1 y1 z1 x2 y2 z2 color [transparency] [r1] [r2] [rho] [id]``

Draw an arrow from (x1, y1, z1) to (x2, y2, z2). An arrow consists of a cylinder stretching from the initial point to an intermediary junction, and a cone stretching from the junction to the final point. The radius of the cylinder is r1 (default 0.1), the radius of the base of the cone is r2 (default 4*r1), and the fraction of the total distance taken up by the cylinder is rho (default 0.75). 

``box x1 y1 z1 x2 y2 z2 color [transparency]``

Draw a box with opposite corners at (x1, y1, z1) and (x2, y2, z2).

``cone x1 y1 z1 x2 y2 z2 r color [transparency] [open] [id]``

Draw a cone with a base of radius r centered at (x1, y1, z1) and a tip at (x2, y2, z2). If the optional parameter open is True (default is False), the base of the cone will be invisible.

``cylinder x1 y1 z1 x2 y2 z2 r color [transparency] [open] [id]``

Draw a cylinder with radius r and bases centered at (x1, y1, z1) and (x2, y2, z2). If the optional parameter open is True (default is False), the bases of the cylinder will be invisible.

``sphere x y z r color [transparency] [id]``

Draw a sphere centered at (x, y, z) with radius r.

``vector x1 y1 z1 x2 y2 z2 color [transparency] [id]``

Draw a line segment from (x1, y1, z1) to (x2, y2, z2).
