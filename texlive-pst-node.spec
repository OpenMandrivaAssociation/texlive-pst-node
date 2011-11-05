# revision 23658
# category Package
# catalog-ctan /graphics/pstricks/contrib/pst-node
# catalog-date 2011-08-22 14:32:24 +0200
# catalog-license lppl
# catalog-version 1.20
Name:		texlive-pst-node
Version:	1.20
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package enables the user to connect information, and to
place labels, without knowing (in advance) the actual positions
of the items to be connected, or where the connecting line
should go. The macros are useful for making graphs and trees,
mathematical diagrams, linguistic syntax diagrams, and so on.
The package contents were previously distributed as a part of
the pstricks base distribution.

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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
