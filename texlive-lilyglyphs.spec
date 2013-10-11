# revision 31814
# category Package
# catalog-ctan /macros/luatex/latex/lilyglyphs
# catalog-date 2013-10-02 17:17:58 +0200
# catalog-license lppl1.3
# catalog-version 9.2.2
Name:		texlive-lilyglyphs
Version:	9.2.2
Release:	1.1
Summary:	Access lilypond fragments and glyphs, in LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/luatex/latex/lilyglyphs
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lilyglyphs.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lilyglyphs.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lilyglyphs.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
# FIXME temporary
Provides:	texlive-lilyglyphs.bin
#Requires:	texlive-lilyglyphs.bin

%description
The package provides the means to include arbitrary elements of
Lilypond notation, including symbols from Lilypond's Emmentaler
font, in a LaTeX document. The package uses OpenType fonts, and
as a result must be compiled with LuaLaTeX or XeLaTeX.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/opentype/public/lilyglyphs/FONTLOG
%{_texmfdistdir}/fonts/opentype/public/lilyglyphs/LICENSE.OFL
%{_texmfdistdir}/fonts/opentype/public/lilyglyphs/emmentaler-11.otf
%{_texmfdistdir}/fonts/opentype/public/lilyglyphs/emmentaler-13.otf
%{_texmfdistdir}/fonts/opentype/public/lilyglyphs/emmentaler-14.otf
%{_texmfdistdir}/fonts/opentype/public/lilyglyphs/emmentaler-16.otf
%{_texmfdistdir}/fonts/opentype/public/lilyglyphs/emmentaler-18.otf
%{_texmfdistdir}/fonts/opentype/public/lilyglyphs/emmentaler-20.otf
%{_texmfdistdir}/fonts/opentype/public/lilyglyphs/emmentaler-23.otf
%{_texmfdistdir}/fonts/opentype/public/lilyglyphs/emmentaler-26.otf
%{_texmfdistdir}/fonts/opentype/public/lilyglyphs/emmentaler-brace.otf
%{_texmfdistdir}/scripts/lilyglyphs/lily-glyph-commands.py
%{_texmfdistdir}/scripts/lilyglyphs/lily-image-commands.py
%{_texmfdistdir}/scripts/lilyglyphs/lily-rebuild-pdfs.py
%{_texmfdistdir}/scripts/lilyglyphs/lilyglyphs_common.py
%{_texmfdistdir}/tex/lualatex/lilyglyphs/README-tex
%{_texmfdistdir}/tex/lualatex/lilyglyphs/commands/README-commands
%{_texmfdistdir}/tex/lualatex/lilyglyphs/commands/accidentals.inp
%{_texmfdistdir}/tex/lualatex/lilyglyphs/commands/accordion.inp
%{_texmfdistdir}/tex/lualatex/lilyglyphs/commands/beamednotes.inp
%{_texmfdistdir}/tex/lualatex/lilyglyphs/commands/clefs.inp
%{_texmfdistdir}/tex/lualatex/lilyglyphs/commands/dynamics.inp
%{_texmfdistdir}/tex/lualatex/lilyglyphs/commands/fancyexamples.inp
%{_texmfdistdir}/tex/lualatex/lilyglyphs/commands/noteheads.inp
%{_texmfdistdir}/tex/lualatex/lilyglyphs/commands/numbers.inp
%{_texmfdistdir}/tex/lualatex/lilyglyphs/commands/rests.inp
%{_texmfdistdir}/tex/lualatex/lilyglyphs/commands/scripts.inp
%{_texmfdistdir}/tex/lualatex/lilyglyphs/commands/singlenotes.inp
%{_texmfdistdir}/tex/lualatex/lilyglyphs/commands/timesignatures.inp
%{_texmfdistdir}/tex/lualatex/lilyglyphs/core/README-core
%{_texmfdistdir}/tex/lualatex/lilyglyphs/core/dotted.inp
%{_texmfdistdir}/tex/lualatex/lilyglyphs/core/genericAccess.inp
%{_texmfdistdir}/tex/lualatex/lilyglyphs/core/keyval.inp
%{_texmfdistdir}/tex/lualatex/lilyglyphs/core/opticals.inp
%{_texmfdistdir}/tex/lualatex/lilyglyphs/lilyglyphs.sty
%{_texmfdistdir}/tex/lualatex/lilyglyphs/pdfs/lily-crescHairpin.pdf
%{_texmfdistdir}/tex/lualatex/lilyglyphs/pdfs/lily-crotchet.pdf
%{_texmfdistdir}/tex/lualatex/lilyglyphs/pdfs/lily-crotchetDotted.pdf
%{_texmfdistdir}/tex/lualatex/lilyglyphs/pdfs/lily-crotchetDottedDouble.pdf
%{_texmfdistdir}/tex/lualatex/lilyglyphs/pdfs/lily-crotchetDottedDoubleDown.pdf
%{_texmfdistdir}/tex/lualatex/lilyglyphs/pdfs/lily-crotchetDottedDown.pdf
%{_texmfdistdir}/tex/lualatex/lilyglyphs/pdfs/lily-crotchetDown.pdf
%{_texmfdistdir}/tex/lualatex/lilyglyphs/pdfs/lily-decrescHairpin.pdf
%{_texmfdistdir}/tex/lualatex/lilyglyphs/pdfs/lily-fancyExample.pdf
%{_texmfdistdir}/tex/lualatex/lilyglyphs/pdfs/lily-halfNote.pdf
%{_texmfdistdir}/tex/lualatex/lilyglyphs/pdfs/lily-halfNoteDotted.pdf
%{_texmfdistdir}/tex/lualatex/lilyglyphs/pdfs/lily-halfNoteDottedDouble.pdf
%{_texmfdistdir}/tex/lualatex/lilyglyphs/pdfs/lily-halfNoteDottedDoubleDown.pdf
%{_texmfdistdir}/tex/lualatex/lilyglyphs/pdfs/lily-halfNoteDottedDown.pdf
%{_texmfdistdir}/tex/lualatex/lilyglyphs/pdfs/lily-halfNoteDown.pdf
%{_texmfdistdir}/tex/lualatex/lilyglyphs/pdfs/lily-quaver.pdf
%{_texmfdistdir}/tex/lualatex/lilyglyphs/pdfs/lily-quaverDotted.pdf
%{_texmfdistdir}/tex/lualatex/lilyglyphs/pdfs/lily-quaverDottedDouble.pdf
%{_texmfdistdir}/tex/lualatex/lilyglyphs/pdfs/lily-quaverDottedDoubleDdown.pdf
%{_texmfdistdir}/tex/lualatex/lilyglyphs/pdfs/lily-quaverDottedDoubleDown.pdf
%{_texmfdistdir}/tex/lualatex/lilyglyphs/pdfs/lily-quaverDottedDown.pdf
%{_texmfdistdir}/tex/lualatex/lilyglyphs/pdfs/lily-quaverDown.pdf
%{_texmfdistdir}/tex/lualatex/lilyglyphs/pdfs/lily-semiquaver.pdf
%{_texmfdistdir}/tex/lualatex/lilyglyphs/pdfs/lily-semiquaverDotted.pdf
%{_texmfdistdir}/tex/lualatex/lilyglyphs/pdfs/lily-semiquaverDottedDouble.pdf
%{_texmfdistdir}/tex/lualatex/lilyglyphs/pdfs/lily-semiquaverDottedDoubleDown.pdf
%{_texmfdistdir}/tex/lualatex/lilyglyphs/pdfs/lily-semiquaverDottedDown.pdf
%{_texmfdistdir}/tex/lualatex/lilyglyphs/pdfs/lily-semiquaverDown.pdf
%{_texmfdistdir}/tex/lualatex/lilyglyphs/pdfs/lily-twoBeamedQuavers.pdf
%doc %{_texmfdistdir}/doc/lualatex/lilyglyphs/CHANGES.md
%doc %{_texmfdistdir}/doc/lualatex/lilyglyphs/INSTALL
%doc %{_texmfdistdir}/doc/lualatex/lilyglyphs/README
%doc %{_texmfdistdir}/doc/lualatex/lilyglyphs/README-scripts
%doc %{_texmfdistdir}/doc/lualatex/lilyglyphs/VERSION
%doc %{_texmfdistdir}/doc/lualatex/lilyglyphs/documentation/lilyglyphs-example-400.png
%doc %{_texmfdistdir}/doc/lualatex/lilyglyphs/documentation/lilyglyphs-example-600.png
%doc %{_texmfdistdir}/doc/lualatex/lilyglyphs/documentation/lilyglyphs-example-de.pdf
%doc %{_texmfdistdir}/doc/lualatex/lilyglyphs/documentation/lilyglyphs-example-de.tex
%doc %{_texmfdistdir}/doc/lualatex/lilyglyphs/documentation/lilyglyphs-example.pdf
%doc %{_texmfdistdir}/doc/lualatex/lilyglyphs/documentation/lilyglyphs-example.png
%doc %{_texmfdistdir}/doc/lualatex/lilyglyphs/documentation/lilyglyphs-example.tex
%doc %{_texmfdistdir}/doc/lualatex/lilyglyphs/documentation/lilyglyphs.pdf
%doc %{_texmfdistdir}/doc/lualatex/lilyglyphs/documentation/lilyglyphs.tex
%doc %{_texmfdistdir}/doc/lualatex/lilyglyphs/documentation/lilyglyphs_logo/lilyglyphs_logo.pdf
%doc %{_texmfdistdir}/doc/lualatex/lilyglyphs/documentation/lilyglyphs_logo/lilyglyphs_logo.png
%doc %{_texmfdistdir}/doc/lualatex/lilyglyphs/documentation/lilyglyphs_logo/lilyglyphs_logo.tex
%doc %{_texmfdistdir}/doc/lualatex/lilyglyphs/documentation/lilyglyphs_private.zip
%doc %{_texmfdistdir}/doc/lualatex/lilyglyphs/documentation/resources/lily-088c978c.png
%doc %{_texmfdistdir}/doc/lualatex/lilyglyphs/documentation/resources/lily-1981c3c7.png
%doc %{_texmfdistdir}/doc/lualatex/lilyglyphs/documentation/resources/lily-20e8632d.png
%doc %{_texmfdistdir}/doc/lualatex/lilyglyphs/documentation/resources/lily-2abb8a04.png
%doc %{_texmfdistdir}/doc/lualatex/lilyglyphs/documentation/resources/lily-2be182be.png
%doc %{_texmfdistdir}/doc/lualatex/lilyglyphs/documentation/resources/lily-3b47d3fe.png
%doc %{_texmfdistdir}/doc/lualatex/lilyglyphs/documentation/resources/lily-3f4afecc.png
%doc %{_texmfdistdir}/doc/lualatex/lilyglyphs/documentation/resources/lily-40869867.png
%doc %{_texmfdistdir}/doc/lualatex/lilyglyphs/documentation/resources/lily-5b13ce04.png
%doc %{_texmfdistdir}/doc/lualatex/lilyglyphs/documentation/resources/lily-5c91a201.png
%doc %{_texmfdistdir}/doc/lualatex/lilyglyphs/documentation/resources/lily-707477b7.png
%doc %{_texmfdistdir}/doc/lualatex/lilyglyphs/documentation/resources/lily-76dbcd67.png
%doc %{_texmfdistdir}/doc/lualatex/lilyglyphs/documentation/resources/lily-7fd84ff8.png
%doc %{_texmfdistdir}/doc/lualatex/lilyglyphs/documentation/resources/lily-8155deab.png
%doc %{_texmfdistdir}/doc/lualatex/lilyglyphs/documentation/resources/lily-8b332c94.png
%doc %{_texmfdistdir}/doc/lualatex/lilyglyphs/documentation/resources/lily-8d82df0c.png
%doc %{_texmfdistdir}/doc/lualatex/lilyglyphs/documentation/resources/lily-8d8bb8a3.png
%doc %{_texmfdistdir}/doc/lualatex/lilyglyphs/documentation/resources/lily-907bc72d.png
%doc %{_texmfdistdir}/doc/lualatex/lilyglyphs/documentation/resources/lily-a2bf82dd.png
%doc %{_texmfdistdir}/doc/lualatex/lilyglyphs/documentation/resources/lily-ae3fd948.png
%doc %{_texmfdistdir}/doc/lualatex/lilyglyphs/documentation/resources/lily-b3dc0958.png
%doc %{_texmfdistdir}/doc/lualatex/lilyglyphs/documentation/resources/lily-b69af986.png
%doc %{_texmfdistdir}/doc/lualatex/lilyglyphs/documentation/resources/lily-d9988a2c.png
%doc %{_texmfdistdir}/doc/lualatex/lilyglyphs/documentation/resources/lily-dffaecd2.png
%doc %{_texmfdistdir}/doc/lualatex/lilyglyphs/documentation/resources/lily-f4d0afc9.png
%doc %{_texmfdistdir}/doc/lualatex/lilyglyphs/documentation/resources/lilyglyphsManualFonts.sty
%doc %{_texmfdistdir}/doc/lualatex/lilyglyphs/documentation/resources/lilyglyphsStyle.sty
%doc %{_texmfdistdir}/doc/lualatex/lilyglyphs/documentation/resources/lilypond-manuals.css
%doc %{_texmfdistdir}/doc/lualatex/lilyglyphs/documentation/the-feta-font-2-16-2.html
%doc %{_texmfdistdir}/doc/lualatex/lilyglyphs/license/COPYING.LPPL
%doc %{_texmfdistdir}/doc/lualatex/lilyglyphs/license/MANIFEST
%doc %{_texmfdistdir}/doc/lualatex/lilyglyphs/license/license-preamble.inp
#- source
%doc %{_texmfdistdir}/source/luatex/lilyglyphs/fonts/README-emmentaler
%doc %{_texmfdistdir}/source/luatex/lilyglyphs/fonts/emmentaler-2-16-2.zip
%doc %{_texmfdistdir}/source/luatex/lilyglyphs/glyphimages/definitions/_template.ly
%doc %{_texmfdistdir}/source/luatex/lilyglyphs/glyphimages/definitions/beamednotes.ly
%doc %{_texmfdistdir}/source/luatex/lilyglyphs/glyphimages/definitions/dynamicsigns.ly
%doc %{_texmfdistdir}/source/luatex/lilyglyphs/glyphimages/definitions/fancyexamples.ly
%doc %{_texmfdistdir}/source/luatex/lilyglyphs/glyphimages/definitions/score.ily
%doc %{_texmfdistdir}/source/luatex/lilyglyphs/glyphimages/definitions/singlenotes.ly
%doc %{_texmfdistdir}/source/luatex/lilyglyphs/glyphimages/generated_src/lily-crescHairpin.ly
%doc %{_texmfdistdir}/source/luatex/lilyglyphs/glyphimages/generated_src/lily-crotchet.ly
%doc %{_texmfdistdir}/source/luatex/lilyglyphs/glyphimages/generated_src/lily-crotchetDotted.ly
%doc %{_texmfdistdir}/source/luatex/lilyglyphs/glyphimages/generated_src/lily-crotchetDottedDouble.ly
%doc %{_texmfdistdir}/source/luatex/lilyglyphs/glyphimages/generated_src/lily-crotchetDottedDoubleDown.ly
%doc %{_texmfdistdir}/source/luatex/lilyglyphs/glyphimages/generated_src/lily-crotchetDottedDown.ly
%doc %{_texmfdistdir}/source/luatex/lilyglyphs/glyphimages/generated_src/lily-crotchetDown.ly
%doc %{_texmfdistdir}/source/luatex/lilyglyphs/glyphimages/generated_src/lily-decrescHairpin.ly
%doc %{_texmfdistdir}/source/luatex/lilyglyphs/glyphimages/generated_src/lily-fancyExample.ly
%doc %{_texmfdistdir}/source/luatex/lilyglyphs/glyphimages/generated_src/lily-halfNote.ly
%doc %{_texmfdistdir}/source/luatex/lilyglyphs/glyphimages/generated_src/lily-halfNoteDotted.ly
%doc %{_texmfdistdir}/source/luatex/lilyglyphs/glyphimages/generated_src/lily-halfNoteDottedDouble.ly
%doc %{_texmfdistdir}/source/luatex/lilyglyphs/glyphimages/generated_src/lily-halfNoteDottedDoubleDown.ly
%doc %{_texmfdistdir}/source/luatex/lilyglyphs/glyphimages/generated_src/lily-halfNoteDottedDown.ly
%doc %{_texmfdistdir}/source/luatex/lilyglyphs/glyphimages/generated_src/lily-halfNoteDown.ly
%doc %{_texmfdistdir}/source/luatex/lilyglyphs/glyphimages/generated_src/lily-quaver.ly
%doc %{_texmfdistdir}/source/luatex/lilyglyphs/glyphimages/generated_src/lily-quaverDotted.ly
%doc %{_texmfdistdir}/source/luatex/lilyglyphs/glyphimages/generated_src/lily-quaverDottedDouble.ly
%doc %{_texmfdistdir}/source/luatex/lilyglyphs/glyphimages/generated_src/lily-quaverDottedDoubleDdown.ly
%doc %{_texmfdistdir}/source/luatex/lilyglyphs/glyphimages/generated_src/lily-quaverDottedDoubleDown.ly
%doc %{_texmfdistdir}/source/luatex/lilyglyphs/glyphimages/generated_src/lily-quaverDottedDown.ly
%doc %{_texmfdistdir}/source/luatex/lilyglyphs/glyphimages/generated_src/lily-quaverDown.ly
%doc %{_texmfdistdir}/source/luatex/lilyglyphs/glyphimages/generated_src/lily-semiquaver.ly
%doc %{_texmfdistdir}/source/luatex/lilyglyphs/glyphimages/generated_src/lily-semiquaverDotted.ly
%doc %{_texmfdistdir}/source/luatex/lilyglyphs/glyphimages/generated_src/lily-semiquaverDottedDouble.ly
%doc %{_texmfdistdir}/source/luatex/lilyglyphs/glyphimages/generated_src/lily-semiquaverDottedDoubleDown.ly
%doc %{_texmfdistdir}/source/luatex/lilyglyphs/glyphimages/generated_src/lily-semiquaverDottedDown.ly
%doc %{_texmfdistdir}/source/luatex/lilyglyphs/glyphimages/generated_src/lily-semiquaverDown.ly
%doc %{_texmfdistdir}/source/luatex/lilyglyphs/glyphimages/generated_src/lily-twoBeamedQuavers.ly

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
