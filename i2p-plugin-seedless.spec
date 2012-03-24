Name:		i2p-plugin-seedless
# Version from plugin.config (shortened)
Version:	0.0.62
Release:	1%{?dist}
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
# Extract thw xpi package with 7zip to 02_seedless
7za x -o02_seedless 02_seedless.xpi2p


%build
# This is a binary


%install
rm -rf $RPM_BUILD_ROOT
# Install to i2p plugins (-p, --preserve-timestamps for extra security)
install -d -p $RPM_BUILD_ROOT/usr/local/i2p/.i2p/plugins
# FIXTHIS: Use install, not cp
cp -R 02_seedless $RPM_BUILD_ROOT/usr/local/i2p/.i2p/plugins/


%post
# Condrestart i2p and return 0
/sbin/service i2p condrestart >/dev/null 2>&1 || :
# Set owner and group to i2p
chown i2p:i2p -R /usr/local/i2p/.i2p


%postun
# Condrestart i2p and return 0
/sbin/service i2p condrestart >/dev/null 2>&1 || :


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc
/usr/local/i2p/.i2p/plugins/02_seedless


%changelog
* Sat Mar 24 2012 Mattias Ohlsson <mattias.ohlsson@inprose.com> - 0.0.62-1
- Initial package
