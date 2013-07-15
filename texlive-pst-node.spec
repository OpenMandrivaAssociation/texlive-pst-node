# revision 27799
# category Package
# catalog-ctan /graphics/pstricks/contrib/pst-node
# catalog-date 2012-09-21 20:41:56 +0200
# catalog-license lppl
# catalog-version 1.25
Name:		texlive-pst-node
Version:	1.25
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


%changelog
* Tue Oct 30 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.25-1
+ Revision: 820781
- Update to latest release.

* Thu Feb 23 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.22-1
+ Revision: 779621
- Update to latest release.

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.21-2
+ Revision: 755374
- Rebuild to reduce used resources

* Fri Dec 09 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.21-1
+ Revision: 739871
- texlive-pst-node

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.20-1
+ Revision: 719370
- texlive-pst-node
- texlive-pst-node
- texlive-pst-node
- texlive-pst-node

