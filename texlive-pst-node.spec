# revision 24693
# category Package
# catalog-ctan /graphics/pstricks/contrib/pst-node
# catalog-date 2011-11-29 01:11:11 +0100
# catalog-license lppl
# catalog-version 1.21
Name:		texlive-pst-node
Version:	1.21
Release:	1
Summary:	Draw connections using pstricks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-node
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-node.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-node.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-node.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package enables the user to connect information, and to
place labels, without knowing (in advance) the actual positions
of the items to be connected, or where the connecting line
should go. The macros are useful for making graphs and trees,
mathematical diagrams, linguistic syntax diagrams, and so on.
The package contents were previously distributed as a part of
the pstricks base distribution.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/dvips/pst-node/pst-node.pro
%{_texmfdistdir}/dvips/pst-node/pst-node97.pro
%{_texmfdistdir}/tex/generic/pst-node/pst-node.tex
%{_texmfdistdir}/tex/latex/pst-node/pst-node.sty
%doc %{_texmfdistdir}/doc/generic/pst-node/Changes
%doc %{_texmfdistdir}/doc/generic/pst-node/README
%doc %{_texmfdistdir}/doc/generic/pst-node/more_docs/Makefile
%doc %{_texmfdistdir}/doc/generic/pst-node/more_docs/psmatrix-docDE.bib
%doc %{_texmfdistdir}/doc/generic/pst-node/more_docs/psmatrix-docDE.pdf
%doc %{_texmfdistdir}/doc/generic/pst-node/more_docs/psmatrix-docDE.tex
%doc %{_texmfdistdir}/doc/generic/pst-node/pst-node-doc.bib
%doc %{_texmfdistdir}/doc/generic/pst-node/pst-node-doc.pdf
%doc %{_texmfdistdir}/doc/generic/pst-node/pst-node-doc.tex
%doc %{_texmfdistdir}/doc/generic/pst-node/pst-node97.tex
#- source
%doc %{_texmfdistdir}/source/generic/pst-node/Makefile

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips tex doc source %{buildroot}%{_texmfdistdir}
