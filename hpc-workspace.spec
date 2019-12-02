Name:   hpc-workspace
Version:1.0
Release:        5%{?dist}
Summary:A workspace is a directory created on behalf of a user, associated with an expiration date, to prevent disks from uncontrolled filling. The project provides user and admin tools to manage those directories.

Group:  System
License:Proprietary
URL:    https://github.com/holgerBerger/hpc-workspace
Source0: https://github.com/mstud/hpc-workspace/archive/master.zip

BuildRequires:  yaml-cpp-devel python2-pyyaml libcap-devel ncurses-devel cmake boost-devel lua-devel lua
Requires:python2-pyyaml lua

%description
A workspace is a directory created on behalf of a user, associated with an expiration date, to prevent disks from uncontrolled filling. The project provides user and admin tools to manage those directories.

%prep
%setup -q -n hpc-workspace-master


%build
mkdir build
cd build
cmake .. -DLUACALLOUTS=yes
make %{?_smp_mflags}
cp bin/* ../bin/


%install
install -m 755 -d $RPM_BUILD_ROOT/%{_bindir}
install -m 755 -d $RPM_BUILD_ROOT/%{_sysconfdir}
install -m 755 -d $RPM_BUILD_ROOT/%{_sbindir}
install -m 755 bin/ws_list $RPM_BUILD_ROOT/usr/bin
install -m 755 bin/ws_extend $RPM_BUILD_ROOT/usr/bin
install -m 755 bin/ws_find $RPM_BUILD_ROOT/usr/bin
install -m 755 bin/ws_register $RPM_BUILD_ROOT/usr/bin
install -m 755 bin/ws_send_ical $RPM_BUILD_ROOT/usr/bin
install -m 4755 bin/ws_allocate $RPM_BUILD_ROOT/usr/bin
install -m 4755 bin/ws_release $RPM_BUILD_ROOT/usr/bin
install -m 4755 bin/ws_restore $RPM_BUILD_ROOT/usr/bin
install -m 755 sbin/ws_expirer $RPM_BUILD_ROOT/usr/sbin
install -m 755 sbin/ws_restore $RPM_BUILD_ROOT/usr/sbin
install -m 755 sbin/ws_validate_config $RPM_BUILD_ROOT/usr/sbin
install -m 644 ws.conf_full_sample $RPM_BUILD_ROOT/etc/ws.conf.sample

%files
%attr(4755, root, root) /usr/bin/ws_allocate
/usr/bin/ws_extend
/usr/bin/ws_find
/usr/bin/ws_list
/usr/bin/ws_register
%attr(4755, root, root)/usr/bin/ws_release
%attr(4755, root, root)/usr/bin/ws_restore
/usr/bin/ws_send_ical
/usr/sbin/ws_expirer
/usr/sbin/ws_restore
/usr/sbin/ws_validate_config
/etc/ws.conf.sample


%changelog
* Mon Jun 24 2019 Maik Schmidt <maik.schmidt@tu-dresden.de> 1.0.0
- Initial RPM

