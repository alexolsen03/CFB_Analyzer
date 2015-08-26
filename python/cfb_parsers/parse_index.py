from bs4 import BeautifulSoup
from prettytable import PrettyTable
import re
import locale
import sys

def execute(path):
	locale.setlocale( locale.LC_ALL, 'en_US.UTF-8' )

	team_id = path.split("/")[1] #assumes  the caller of this is in cfb_parsers

	soup	= BeautifulSoup(open(path))
	tbl	= soup.find("table", {"class": "team-schedule"})

	trs	= tbl.find_all("tr")

	opponents = []

	for j in range(len(trs)):
		if j == 0: #table header data
			continue #stop processing anything

		tr	= trs[j]
		tds	= tr.find_all("td")

		if len(tds) > 1 and "Totals" not in tds[1]:
			isAwayGame		= False
			homeTeamRank	= 0
			awayTeamRank	= 0
			awayTeamId		= 0
			homeTeamId		= 0
			isNotFBS		= False

			opp_name 	= tds[1]
			opp_id 		= 0

			if len(opp_name.find_all("a")) > 0:
				ahref_path 	= opp_name.find("a")['href']
				opp_id 		= locale.atoi(ahref_path.split('/')[3])
			else: #is not fbs team
				opp_id		= -1
				isNotFBS	= True

			if "@" in opp_name:
				isAwayGame 	= True
				homeTeamId 	= opp_id
				awayTeamId 	= team_id
			else:
				#isAwayGame already False
				homeTeamId	= team_id
				awayTeamId	= opp_id

			opp = {}

			opp['date']		= tds[0].text
			opp['homeTeamId']	= homeTeamId
			opp['awayTeamId']	= awayTeamId
			opp['pointsHome']	= tds[2].text
			opp['pointsAway']	= tds[4].text
			opp['isNotFBS']		= isNotFBS
			opp['homeTeamRank']	= homeTeamRank
			opp['awayTeamRank'] 	= awayTeamRank
			opp['gameTime'] 	= tds[3].text
			opp['attendance'] 	= tds[4].text

			opponents.append(opp)

	return opponents

