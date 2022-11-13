Name:		texlive-powerdot-FUBerlin
Version:	52922
Release:	1
Summary:	Powerdot, using the style of FU Berlin
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/powerdot-FUBerlin
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/powerdot-fuberlin.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/powerdot-fuberlin.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The bundle provides a powerdot-derived class and a package for
use with powerdot to provide the corporate design of the Free
University in Berlin. Users may use the class itself
(FUpowerdot) or use the package in the usual way with
\style=BerlinFU as a class option. Examples of using both the
class and the package are provided; the PDF is visually
identical, so the catalogue only lists one; the sources of the
examples do of course differ.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/powerdot-fuberlin
%doc %{_texmfdistdir}/doc/latex/powerdot-fuberlin

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
