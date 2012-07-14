Name:		i2p-plugin-seedless
# Version from plugin.config (0.1.2-0.1.8)
Version:	0.1.2
Release:	0.1.8.1%{?dist}
Summary:	Seedless plugin for I2P	

Group:		Applications/Internet
# License from plugin.config
License:	WTFPL
URL:		http://sponge.i2p/files/seedless/02_seedless.xpi2p
# FIXTHIS: This is a the binary in a archive folder
Source0:	i2p-plugin-seedless-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:	p7zip
Requires:	i2p i2p-plugin-neodatis
BuildArch: 	noarch

# Description from plugin.config and from 
# http://sponge.i2p/files/seedless/doc/Seedless.pdf
%description
Seedless core and console plugin is a self-seeding seed information spreader for I2P.


%prep
%setup -q
# Extract the xpi package with 7zip to 02_seedless
7za x -o02_seedless 02_seedless.xpi2p


%build
# This is a binary

# Disable automatic update
sed -i \
  -e 's|updateURL=|#DISABLED (rpm package): updateURL=|g' \
  02_seedless/plugin.config


%install
rm -rf $RPM_BUILD_ROOT
# Install to i2p plugins (-p, --preserve-timestamps for extra security)
install -d -p $RPM_BUILD_ROOT/usr/local/i2p/.i2p/plugins
# FIXTHIS: Use install, not cp
cp -R 02_seedless $RPM_BUILD_ROOT/usr/local/i2p/.i2p/plugins/


%post
# Condrestart i2p and return 0
/sbin/service i2p condrestart >/dev/null 2>&1 || :


%postun
# Condrestart i2p and return 0
/sbin/service i2p condrestart >/dev/null 2>&1 || :


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(700,i2p,i2p,700)
%doc
# list all folders to apply defattr
/usr/local/i2p/.i2p
/usr/local/i2p/.i2p/plugins
/usr/local/i2p/.i2p/plugins/02_seedless


%changelog
* Mon Jul 9 2012 Mattias Ohlsson <mattias.ohlsson@inprose.com> - 0.1.2-0.1.8.1
- New version

* Mon Apr 9 2012 Mattias Ohlsson <mattias.ohlsson@inprose.com> - 0.0.62-2
- Disable automatic update

* Sat Mar 24 2012 Mattias Ohlsson <mattias.ohlsson@inprose.com> - 0.0.62-1
- Initial package
