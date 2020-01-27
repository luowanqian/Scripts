#!/usr/bin/env bash

#   The MacTex website (https://www.tug.org/mactex/uninstalling.html) says it's "difficult"
# to uninstall Ghostscript, as installed by MacTex. Their suggestion is to:
#     open the MacTeX-2015 install package and select "Show Files" from the resulting "File" menu of Apple's installer
# and then:
#     Find files related to Ghostscript and remove them.
# which is exactly what this script does. It also prints the names of the deleted files, and moves the files to
# the user's Trash instead of actually deleting them. This can help you roll back the effects of the script in
# case something goes wrong.

# Note that this requires write access to the /tmp directory on your computer.

# Example usage:
#  You saved "mactex-20150613.pkg" in ~/Downloads and used that to install MacTex.bash uninstall-ghostscript.sh

#   This script comes with ABSOLUTELY NO WARRANTY WHATSOEVER. By running it, you agree to take full responsibility
# for anything that happens to your computer as a result.

#   At the end of the day, you should have deleted the files:
# /usr/local/bin/dvipdf
# /usr/local/bin/eps2eps
# /usr/local/bin/font2c
# /usr/local/bin/gs-X11
# /usr/local/bin/gs-X11-64Bit
# /usr/local/bin/gs-X11-Yosemite
# /usr/local/bin/gs-noX11
# /usr/local/bin/gs-noX11-64Bit
# /usr/local/bin/gs-noX11-Yosemite
# /usr/local/bin/gsbj
# /usr/local/bin/gsdj
# /usr/local/bin/gsdj500
# /usr/local/bin/gslj
# /usr/local/bin/gslp
# /usr/local/bin/gsnd
# /usr/local/bin/lprsetup.sh
# /usr/local/bin/pdf2dsc
# /usr/local/bin/pdf2ps
# /usr/local/bin/pf2afm
# /usr/local/bin/pfbtopfa
# /usr/local/bin/pphs
# /usr/local/bin/printafm
# /usr/local/bin/ps2ascii
# /usr/local/bin/ps2epsi
# /usr/local/bin/ps2pdf
# /usr/local/bin/ps2pdf12
# /usr/local/bin/ps2pdf13
# /usr/local/bin/ps2pdf14
# /usr/local/bin/ps2pdfwr
# /usr/local/bin/ps2ps
# /usr/local/bin/ps2ps2
# /usr/local/bin/unix-lpr.sh
# /usr/local/bin/wftopfa
# /usr/local/share/man/de/man1/dvipdf.1
# /usr/local/share/man/de/man1/font2c.1
# /usr/local/share/man/de/man1/gsnd.1
# /usr/local/share/man/de/man1/pdf2dsc.1
# /usr/local/share/man/de/man1/pdf2ps.1
# /usr/local/share/man/de/man1/printafm.1
# /usr/local/share/man/de/man1/ps2ascii.1
# /usr/local/share/man/de/man1/ps2pdf.1
# /usr/local/share/man/de/man1/ps2ps.1
# /usr/local/share/man/de/man1/wftopfa.1
# /usr/local/share/man/man1/dvipdf.1
# /usr/local/share/man/man1/font2c.1
# /usr/local/share/man/man1/gs.1
# /usr/local/share/man/man1/gslp.1
# /usr/local/share/man/man1/gsnd.1
# /usr/local/share/man/man1/pdf2dsc.1
# /usr/local/share/man/man1/pdf2ps.1
# /usr/local/share/man/man1/pf2afm.1
# /usr/local/share/man/man1/pfbtopfa.1
# /usr/local/share/man/man1/printafm.1
# /usr/local/share/man/man1/ps2ascii.1
# /usr/local/share/man/man1/ps2epsi.1
# /usr/local/share/man/man1/ps2pdf.1
# /usr/local/share/man/man1/ps2pdfwr.1
# /usr/local/share/man/man1/ps2ps.1
# /usr/local/share/man/man1/wftopfa.1
#
#   and the directory:
# /usr/local/share/ghostscript/

uninstall_ghostscript () {
  files=$(pkgutil --bom $1 | fgrep local.pkg | xargs lsbom -s -f | fgrep -v ghostscript | sed 's_^\._/usr/local_')
  command mv -i $files ~/.Trash
  command mv -i /usr/local/share/ghostscript ~/.Trash
}

uninstall_ghostscript $1
