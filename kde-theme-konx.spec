
%define		_name	konx

Summary:	KDE theme - %{_name}
Summary(pl):	Motyw KDE - %{_name}
Name:		kde-theme-%{_name}
Version:	0.2
Release:	1
License:	GPL
Group:		Themes
Source0:	http://stud4.tuwien.ac.at/~e0125672/%{_name}-%{version}.tar.gz
# Source0-md5:	e4d3d31ba85fb18a7961e3f6915b43a3
URL:		http://www.kde-look.org/content/show.php?content=12463
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	freetype-devel
BuildRequires:	kdelibs-devel
BuildRequires:	unsermake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Konx is a completely flat and clean theme based on dotNet from KDE.
This package contains a standard grey/light blue colorscheme.

%description -l pl
Konx to zupe³nie p³aski ale i wyra¼ny motyw oparty na dotNet z KDE.
Ten pakiet zawiera standardowy czarno-jasnoniebieski schemat kolorów.

%package -n kde-style-%{_name}
Summary:	KDE style - %{_name}
Summary(pl):	Styl do KDE - %{_name}
Group:		Themes
Requires:	kdelibs

%description -n kde-style-%{_name}
Konx is a completely flat and clean theme based on dotNet from KDE.

%description -n kde-style-%{_name} -l pl
Konx to zupe³nie p³aski ale i wyra¼ny motyw oparty na dotNet z KDE.

%package -n kde-colorscheme-%{_name}
Summary:	Color scheme for KDE style - %{_name}
Summary(pl):	Schemat kolorów do stylu KDE - %{_name}
Group:		Themes
Requires:	kdebase-core

%description -n kde-colorscheme-%{_name}
This package contains a typical grey/light blue colorscheme.

%description -n kde-colorscheme-%{_name} -l pl
Ten pakiet zawiera typowy czarno/jasnoniebieski schemat kolorów.

%prep
%setup -q -n %{_name}-%{version}

%build
cp -f %{_datadir}/automake/config.sub admin
export UNSERMAKE=%{_datadir}/unsermake/unsermake
%{__make} -f Makefile.cvs

%configure \
	--with-qt-libraries=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir="%{_kdedocdir}"

%clean
rm -rf $RPM_BUILD_ROOT

%files -n kde-style-%{_name}
%defattr(644,root,root,755)
##%{_libdir}/kde3/kstyle_*.la
##%attr(755,root,root) %{_libdir}/kde3/kstyle_*.so
%{_libdir}/kde3/plugins/styles/*.la
%attr(755,root,root) %{_libdir}/kde3/plugins/styles/*.so
%{_datadir}/apps/kstyle/themes/*.themerc

%files -n kde-colorscheme-%{_name}
%defattr(644,root,root,755)
%{_datadir}/apps/kdisplay/color-schemes/*.kcsrc
