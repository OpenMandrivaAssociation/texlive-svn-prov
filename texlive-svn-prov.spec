%global tl_name svn-prov
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.1862
Release:	%{tl_revision}.1
Summary:	Subversion variants of \Provides... macros
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/svn-prov
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/svn-prov.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/svn-prov.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/svn-prov.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package introduces Subversion variants of the standard LaTeX macros
\ProvidesPackage, \ProvidesClass and \ProvidesFile where the file name
and date is extracted from Subversion Id keywords. The file name may
also be given explicitly as an optional argument.

