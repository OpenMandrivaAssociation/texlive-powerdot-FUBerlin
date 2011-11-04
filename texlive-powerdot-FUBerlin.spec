# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/powerdot-FUBerlin
# catalog-date 2009-07-30 21:57:53 +0200
# catalog-license lppl
# catalog-version 0.01
Name:		texlive-powerdot-FUBerlin
Version:	0.01
Release:	1
Summary:	Powerdot, using the style of FU Berlin
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/powerdot-FUBerlin
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/powerdot-FUBerlin.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/powerdot-FUBerlin.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The bundle provides a powerdot-derived class and a package for
use with powerdot to provide the corporate design of the Free
University in Berlin. Users may use the class itself
(FUpowerdot) or use the package in the usual way with
\style=BerlinFU as a class option. Examples of using both the
class and the package are provided; the PDF is visually
identical, so the catalogue only lists one; the sources of the
examples do of course differ.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/powerdot-FUBerlin/FUpowerdot.cls
%{_texmfdistdir}/tex/latex/powerdot-FUBerlin/powerdot-BerlinFU.sty
%doc %{_texmfdistdir}/doc/latex/powerdot-FUBerlin/FULogo.eps
%doc %{_texmfdistdir}/doc/latex/powerdot-FUBerlin/FULogo_RGB.eps
%doc %{_texmfdistdir}/doc/latex/powerdot-FUBerlin/FUbib.eps
%doc %{_texmfdistdir}/doc/latex/powerdot-FUBerlin/FUseal.eps
%doc %{_texmfdistdir}/doc/latex/powerdot-FUBerlin/README
%doc %{_texmfdistdir}/doc/latex/powerdot-FUBerlin/exampleClass.pdf
%doc %{_texmfdistdir}/doc/latex/powerdot-FUBerlin/exampleClass.tex
%doc %{_texmfdistdir}/doc/latex/powerdot-FUBerlin/exampleStyle.pdf
%doc %{_texmfdistdir}/doc/latex/powerdot-FUBerlin/exampleStyle.tex
%doc %{_texmfdistdir}/doc/latex/powerdot-FUBerlin/silberlaube2.eps
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
