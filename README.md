## or-applet - A Gtk+ Tor System Tray applet
#### Yawning Angel (yawning at schwanenlied dot me)

### What?

This is a stem/pygobject based Tor controller.  It primarily exists so I can
get quick info out of the system Tor instance on my laptop, if it happens to be
useful for other people, that's great.

![screeenshot](https://raw.github.com/Yawning/or-applet/screenshots/screenshot-0.0.1.png)

### Dependencies

 * [pygobject3](https://wiki.gnome.org/PyGObject)
 * [stem](https://stem.torproject.org/)

The versions used for development are pygobject 3.12 and stem fb2734b, other
versions are not supported.  The "Stem Prompt" launcher requires urxvt and
stem/interpretor (not installed by default) to work, and modifications to the
code to fix readline brain damage with the colored prompt.

### WON'T DO

 * Go out of my way to support OSes/distributions I don't use.  Patches
   accepted.
 * Anything involving the words "GeoIP".  I don't reduce my anonymity set by
   enaging in StrictExitNodes/ExitNodes tinfoil-hattery.

### Credits

 * Leek icon by Robin Weatherall (http://www.robinweatherall.eu)

