# Copyright 1999-2007 Gentoo Foundation
# Distributed under the terms of the GNU General Public License v2
# $Header: $

DESCRIPTION="Smart console frontend for the cdrkit/cdrtools & dvd+rw-tools"
HOMEPAGE="http://burn-cd.sourceforge.net/"
SRC_URI="mirror://sourceforge/${PN}/${P}.gz"

LICENSE="LGPL-2"
IUSE=""
SLOT="0"
KEYWORDS="~amd64 ~ppc ~sparc ~x86"

RDEPEND=">=dev-lang/python-2.1
		 virtual/cdrtools
		 app-cdr/dvd+rw-tools"

src_install() {
	newbin ${P} ${PN}
}
