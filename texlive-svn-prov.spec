# revision 18017
# category Package
# catalog-ctan /macros/latex/contrib/svn-prov
# catalog-date 2010-04-25 23:29:42 +0200
# catalog-license lppl
# catalog-version 3.1862
Name:		texlive-svn-prov
Version:	3.1862
Release:	1
Summary:	Subversion variants of \Provides... macros
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/svn-prov
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/svn-prov.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/svn-prov.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/svn-prov.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package introduces Subversion variants of the standard
LaTeX macros \ProvidesPackage, \ProvidesClass and \ProvidesFile
where the file name and date is extracted from Subversion Id
keywords. The file name may also be given explicitly as an
optional argument.

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
%{_texmfdistdir}/tex/latex/svn-prov/svn-prov.sty
%doc %{_texmfdistdir}/doc/latex/svn-prov/svn-prov.pdf
#- source
%doc %{_texmfdistdir}/source/latex/svn-prov/Makefile
%doc %{_texmfdistdir}/source/latex/svn-prov/svn-prov.dtx
%doc %{_texmfdistdir}/source/latex/svn-prov/svn-prov.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
