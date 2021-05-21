#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Lexical-SealRequireHints
Version  : 0.011
Release  : 16
URL      : https://cpan.metacpan.org/authors/id/Z/ZE/ZEFRAM/Lexical-SealRequireHints-0.011.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/Z/ZE/ZEFRAM/Lexical-SealRequireHints-0.011.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libl/liblexical-sealrequirehints-perl/liblexical-sealrequirehints-perl_0.011-2.debian.tar.xz
Summary  : 'prevent leakage of lexical hints'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Lexical-SealRequireHints-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
NAME
Lexical::SealRequireHints - prevent leakage of lexical hints
DESCRIPTION
This module works around two historical bugs in Perl's handling of the
"%^H" (lexical hints) variable.  One bug causes lexical state in one file
to leak into another that is "require"d/"use"d from it.  This bug, [perl
#68590], was present from Perl 5.6 up to Perl 5.10, fixed in Perl 5.11.0.
The second bug causes lexical state (normally a blank "%^H" once the first
bug is fixed) to leak outwards from "utf8.pm", if it is automatically
loaded during Unicode regular expression matching, into whatever source
is compiling at the time of the regexp match.  This bug, [perl #73174],
was present from Perl 5.8.7 up to Perl 5.11.5, fixed in Perl 5.12.0.

%package dev
Summary: dev components for the perl-Lexical-SealRequireHints package.
Group: Development
Provides: perl-Lexical-SealRequireHints-devel = %{version}-%{release}
Requires: perl-Lexical-SealRequireHints = %{version}-%{release}

%description dev
dev components for the perl-Lexical-SealRequireHints package.


%package perl
Summary: perl components for the perl-Lexical-SealRequireHints package.
Group: Default
Requires: perl-Lexical-SealRequireHints = %{version}-%{release}

%description perl
perl components for the perl-Lexical-SealRequireHints package.


%prep
%setup -q -n Lexical-SealRequireHints-0.011
cd %{_builddir}
tar xf %{_sourcedir}/liblexical-sealrequirehints-perl_0.011-2.debian.tar.xz
cd %{_builddir}/Lexical-SealRequireHints-0.011
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Lexical-SealRequireHints-0.011/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Lexical::SealRequireHints.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/Lexical/SealRequireHints.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Lexical/SealRequireHints/SealRequireHints.so
