# revision 18017
# category Package
# catalog-ctan /macros/latex/contrib/svn-prov
# catalog-date 2010-04-25 23:29:42 +0200
# catalog-license lppl
# catalog-version 3.1862
Name:		texlive-svn-prov
Version:	3.1862
Release:	7
Summary:	Subversion variants of \Provides... macros
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/svn-prov
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/svn-prov.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/svn-prov.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/svn-prov.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 3.1862-2
+ Revision: 756362
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 3.1862-1
+ Revision: 719620
- texlive-svn-prov
- texlive-svn-prov
- texlive-svn-prov
- texlive-svn-prov

