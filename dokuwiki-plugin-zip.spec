%define		plugin		zip
Summary:	DokuWiki zip plugin
Summary(pl.UTF-8):	Wtyczka zip dla DokuWiki
Name:		dokuwiki-plugin-%{plugin}
Version:	0.4
Release:	0.1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://wiki.pilsch.com/doku-zip-%{version}.zip
# Source0-md5:	7525314836db3ab7fd2f97d5a9e3bf89
Source1:	dokuwiki-find-lang.sh
URL:		http://wiki.pilsch.com/zip.html
BuildRequires:	unzip
Requires:	dokuwiki >= 20061106
Requires:	php-pear-File_Archive
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		dokuconf	/etc/webapps/dokuwiki
%define		dokudir		/usr/share/dokuwiki
%define		plugindir	%{dokudir}/lib/plugins/%{plugin}

%description
This plugin saves a doku wiki as a zip file that contains changes.log,
pages/, and, attic/ from the directory pointed to by $conf["savedir"].
In addition to the ability to save zip backups, this plugin also
allows for the restoration of lost data from such an archive.

%description -l pl.UTF-8
Wtyczka zip dla DokuWiki

%prep
%setup -q -n %{plugin}-standalone

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a . $RPM_BUILD_ROOT%{plugindir}

# find locales
sh %{SOURCE1} %{name}.lang

%clean
rm -rf $RPM_BUILD_ROOT

%post
# force css cache refresh
if [ -f %{dokuconf}/local.php ]; then
	touch %{dokuconf}/local.php
fi

%files -f %{name}.lang
%defattr(644,root,root,755)
%dir %{plugindir}
%{plugindir}/*.php
%{plugindir}/*.css
