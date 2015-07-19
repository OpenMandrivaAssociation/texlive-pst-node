# revision 33303
# category Package
# catalog-ctan /graphics/pstricks/contrib/pst-node
# catalog-date 2014-03-26 09:37:24 +0100
# catalog-license lppl
# catalog-version 1.33
Name:		texlive-pst-node
Version:	1.33
Release:	4
Summary:	Nodes and node connections in pstricks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-node
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-node.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-node.doc.tar.xz
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
the pstricks base distribution; the package serves as an
extension to PSTricks.

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
%{_texmfdistdir}/tex/generic/pst-node/pst-node97.tex
%{_texmfdistdir}/tex/latex/pst-node/pst-node.sty
%doc %{_texmfdistdir}/doc/generic/pst-node/Changes
%doc %{_texmfdistdir}/doc/generic/pst-node/README
%doc %{_texmfdistdir}/doc/generic/pst-node/psmatrix-docDE.bib
%doc %{_texmfdistdir}/doc/generic/pst-node/psmatrix-docDE.pdf
%doc %{_texmfdistdir}/doc/generic/pst-node/psmatrix-docDE.tex
%doc %{_texmfdistdir}/doc/generic/pst-node/pst-node-doc.bib
%doc %{_texmfdistdir}/doc/generic/pst-node/pst-node-doc.pdf
%doc %{_texmfdistdir}/doc/generic/pst-node/pst-node-doc.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips tex doc %{buildroot}%{_texmfdistdir}
