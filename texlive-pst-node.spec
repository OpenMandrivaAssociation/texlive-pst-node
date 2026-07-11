%global tl_name pst-node
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.45
Release:	%{tl_revision}.1
Summary:	Nodes and node connections in PSTricks
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-node
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-node.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-node.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package enables the user to connect information, and to place
labels, without knowing (in advance) the actual positions of the items
to be connected, or where the connecting line should go. The macros are
useful for making graphs and trees, mathematical diagrams, linguistic
syntax diagrams, and so on. The package contents were previously
distributed as a part of the pstricks base distribution; the package
serves as an extension to PSTricks.

