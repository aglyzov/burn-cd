# Copyright 1999-2016 Gentoo Foundation
# Distributed under the terms of the GNU General Public License v2
# $Id$

EAPI=5

DESCRIPTION="Smart console frontend for the cdrkit/cdrtools & dvd+rw-tools"
HOMEPAGE="https://github.com/aglyzov/burn-cd/"
SRC_URI="https://github.com/aglyzov/${PN}/archive/${PV}.tar.gz -> ${P}.tar.gz"

LICENSE="LGPL-2"
IUSE=""
SLOT="0"
KEYWORDS="~amd64 ~x86"

RDEPEND="dev-lang/python:2.7
	virtual/cdrtools
	app-cdr/dvd+rw-tools"

src_install() {
	newbin ${P} ${PN}
	insinto /etc
	newins dotburn-cd.conf burn-cd.conf
}
