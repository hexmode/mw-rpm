# Hello packaging friend!
#
# If you find yourself using this 'fpm --edit' feature frequently, it is
# a sign that fpm is missing a feature! I welcome your feature requests!
# Please visit the following URL and ask for a feature that helps you never
# need to edit this file again! :)
#   https://github.com/jordansissel/fpm/issues
# ------------------------------------------------------------------------

# Disable the stupid stuff rpm distros include in the build process by default:
#   Disable any prep shell actions. replace them with simply 'true'
%define __spec_prep_post true
%define __spec_prep_pre true
#   Disable any build shell actions. replace them with simply 'true'
%define __spec_build_post true
%define __spec_build_pre true
#   Disable any install shell actions. replace them with simply 'true'
%define __spec_install_post true
%define __spec_install_pre true
#   Disable any clean shell actions. replace them with simply 'true'
%define __spec_clean_post true
%define __spec_clean_pre true
# Disable checking for unpackaged files ?
#%undefine __check_files

# Use md5 file digest method
%define _binary_filedigest_algorithm 1

# Use gzip payload compression
%define _binary_payload w9.gzdio 


Name: python-passwords
Version: 0.2.0
Release: 1
Summary: Passwords for everyone.
AutoReqProv: no
# Seems specifying BuildRoot is required on older rpmbuild (like on CentOS 5)
# fpm passes '--define buildroot ...' on the commandline, so just reuse that.
BuildRoot: %buildroot
# Add prefix, must not end with /

Prefix: /

Group: default
License: Copyright (c) 2012 Jonathan Cremin.
Vendor: none
URL: http://github.com/kudos/passwords
Packager: <mah@vm0>

%description
Passwords for everyone.

%prep
# noop

%build
# noop

%install
# noop

%clean
# noop



%files
%defattr(-,root,root,-)

# Reject config files already listed or parent directories, then prefix files
# with "/", then make sure paths with spaces are quoted. I hate rpm so much.
/usr/lib/python2.6/site-packages/passwords-0.2.0-py2.6.egg-info/SOURCES.txt
/usr/lib/python2.6/site-packages/passwords-0.2.0-py2.6.egg-info/dependency_links.txt
/usr/lib/python2.6/site-packages/passwords-0.2.0-py2.6.egg-info/top_level.txt
/usr/lib/python2.6/site-packages/passwords-0.2.0-py2.6.egg-info/PKG-INFO
/usr/lib/python2.6/site-packages/passwords/pbkdf2.py
/usr/lib/python2.6/site-packages/passwords/pbkdf2.pyc
/usr/lib/python2.6/site-packages/passwords/__init__.pyc
/usr/lib/python2.6/site-packages/passwords/__init__.py

%changelog

