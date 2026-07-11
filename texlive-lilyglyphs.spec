%global tl_name lilyglyphs
%global tl_revision 56473

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2.4
Release:	%{tl_revision}.1
Summary:	Access lilypond fragments and glyphs, in LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/unicodetex/latex/lilyglyphs
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lilyglyphs.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lilyglyphs.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lilyglyphs.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(lilyglyphs.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides the means to include arbitrary elements of Lilypond
notation, including symbols from Lilypond's Emmentaler font, in a LaTeX
document. The package uses OpenType fonts, and as a result must be
compiled with LuaLaTeX or XeLaTeX.

