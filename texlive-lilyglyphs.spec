Name:		texlive-lilyglyphs
Version:	56473
Release:	1
Summary:	Access lilypond fragments and glyphs, in LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/luatex/latex/lilyglyphs
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lilyglyphs.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lilyglyphs.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lilyglyphs.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Provides:	texlive-lilyglyphs.bin = %{EVRD}

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
%{_bindir}/lily-*
%{_texmfdistdir}/fonts/opentype/public/lilyglyphs
%{_texmfdistdir}/scripts/lilyglyphs
%{_texmfdistdir}/tex/latex/lilyglyphs
%doc %{_texmfdistdir}/doc/latex/lilyglyphs
#- source
%doc %{_texmfdistdir}/source/latex/lilyglyphs

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
ln -sf %{_texmfdistdir}/scripts/lilyglyphs/lily-glyph-commands.py lily-glyph-commands
ln -sf %{_texmfdistdir}/scripts/lilyglyphs/lily-image-commands.py lily-image-commands
ln -sf %{_texmfdistdir}/scripts/lilyglyphs/lily-rebuild-pdfs.py lily-rebuild-pdfs
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
