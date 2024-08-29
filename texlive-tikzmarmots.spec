Name:		texlive-tikzmarmots
Version:	71076
Release:	1
Summary:	Drawing little marmots in TikZ
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tikzmarmots
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikzmarmots.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikzmarmots.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a LaTeX package for marmots to be used in TikZ
pictures. These little figures are constructed in such a way
that they may even "borrow" some garments and other attributes
from the TikZducks.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/tikzmarmots
%doc %{_texmfdistdir}/doc/latex/tikzmarmots

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
