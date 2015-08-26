from bs4 import BeautifulSoup
from prettytable import PrettyTable
import re
import locale
import sys

def execute(path):
	locale.setlocale( locale.LC_ALL, 'en_US.UTF-8' )

	soup	= BeautifulSoup(open(path))
	tbl	= soup.find("table", {"class": "game-log"})

	trs	= tbl.find_all("tr")

	opponents = []

	for j in range(len(trs)):
		if j == 0: #table header data
			continue #stop processing anything

		tr	= trs[j]
		tds	= tr.find_all("td")

		if len(tds) > 1 and "Totals" not in tds[1]:
			opp_name 	= tds[1]
			opp_id 		= 0

			if len(opp_name.find_all("a")) > 0:
				ahref_path 	= opp_name.find("a")['href']
				opp_id 		= locale.atoi(ahref_path.split('/')[3])
			else: #is not fbs team
				opp_id		= -1

			opp = {}

			opp['opponentId']	= opp_id
			opp['date']		= tds[0].text
			opp['surface']		= tds[2].text
			opp['attempts']		= tds[4].text
			opp['yards']		= tds[5].text
			opp['touchdowns']	= tds[7].text

			opponents.append(opp)

	return opponents

