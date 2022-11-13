Name:		texlive-svn-prov
Version:	64967
Release:	1
Summary:	Subversion variants of \Provides... macros
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/svn-prov
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/svn-prov.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/svn-prov.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/svn-prov.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package introduces Subversion variants of the standard
LaTeX macros \ProvidesPackage, \ProvidesClass and \ProvidesFile
where the file name and date is extracted from Subversion Id
keywords. The file name may also be given explicitly as an
optional argument.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/svn-prov/svn-prov.sty
%doc %{_texmfdistdir}/doc/latex/svn-prov/svn-prov.pdf
#- source
%doc %{_texmfdistdir}/source/latex/svn-prov/Makefile
%doc %{_texmfdistdir}/source/latex/svn-prov/svn-prov.dtx
%doc %{_texmfdistdir}/source/latex/svn-prov/svn-prov.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
