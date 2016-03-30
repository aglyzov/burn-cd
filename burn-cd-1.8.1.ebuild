# Copyright 1999-2016 Gentoo Foundation
# Distributed under the terms of the GNU General Public License v2
# $Id$

EAPI=5

PYTHON_COMPAT=( python2_7 )
inherit python-single-r1


DESCRIPTION="Smart console frontend for the cdrkit/cdrtools & dvd+rw-tools"
HOMEPAGE="https://github.com/aglyzov/burn-cd/"
EGIT_REPO_URI="git://github.com/aglyzov/burn-cd.git"
inherit git-2
SRC_URI=""

LICENSE="LGPL-2"
IUSE=""
SLOT="0"
KEYWORDS="~amd64 ~x86"

RDEPEND="${PYTHON_DEPS}
		 virtual/cdrtools
		 app-cdr/dvd+rw-tools"

src_install() {
	newbin ${P} ${PN}
	insinto /etc
	newins dotburn-cd.conf burn-cd.conf
}
