import urllib2
import os

team_ids = [721,5,8,27,29,28,31,30,725,37,77,47,51,66,67,71,86,107,129,140,147,157,156,164,193,196,204,235,229,231,234,96,257,253,254,255,277,288,295,301,306,312,311,328,327,331,334,365,366,671,498,367,388,392,400,404,415,414,418,416,419,428,433,430,434,726,463,466,473,472,457,490,497,503,509,513,519,518,522,521,523,529,528,539,545,559,574,587,663,626,630,646,648,651,664,674,688,698,690,694,703,697,670,700,709,716,718,719,9,128,110,465,657,704,706,732,731,736,746,742,749,756,754,768,772,774,796,811]

pages = ["rushing", "passing", "redzone", "turnovermargin", "index"]

# #get rushing game log offense
# for i in range(len(team_ids)):
# 	print "getting rushing for " + str(team_ids[i])

# 	filename = "html_files/" + str(team_ids[i]) + "/2014/"
# 	if not os.path.exists(os.path.dirname(filename)):
#  		os.makedirs(os.path.dirname(filename))

# 	response = urllib2.urlopen("http://www.cfbstats.com/2014/team/" + str(team_ids[i]) + "/" + pages[0] +"/offense/gamelog.html")
# 	obj = open("html_files/" + str(team_ids[i]) + "/2014/rushing.html", "w+")
# 	obj.write(response.read())
# 	obj.close()

# #get passing game log offense
# for i in range(len(team_ids)):
# 	print "getting passing for " + str(i)
# 	response = urllib2.urlopen("http://www.cfbstats.com/2014/team/" + str(team_ids[i]) + "/" + pages[1] +"/offense/gamelog.html")
# 	obj = open("html_files/" + str(team_ids[i]) + "/2014/passing.html", "w+")
# 	obj.write(response.read())
# 	obj.close()

# #get redzone game log
# for i in range(len(team_ids)):
# 	print "getting redzone for " + str(i)
# 	response = urllib2.urlopen("http://www.cfbstats.com/2014/team/" + str(team_ids[i]) + "/" + pages[2] +"/offense/gamelog.html")
# 	obj = open("html_files/" + str(team_ids[i]) + "/2014/redzone.html", "w+")
# 	obj.write(response.read())
# 	obj.close()

# #get turnovers game log
# for i in range(len(team_ids)):
# 	print "getting turnovers for " + str(i)
# 	response = urllib2.urlopen("http://www.cfbstats.com/2014/team/" + str(team_ids[i]) + "/" + pages[3] +"/gamelog.html")
# 	obj = open("html_files/" + str(team_ids[i]) + "/2014/turnovers.html", "w+")
# 	obj.write(response.read())
# 	obj.close()

#get game data
for i in range(len(team_ids)):
	print "getting indexes for " + str(i)
	response = urllib2.urlopen("http://www.cfbstats.com/2014/team/" + str(team_ids[i]) + "/" + pages[4] +".html")
	obj = open("html_files/" + str(team_ids[i]) + "/2014/index.html", "w+")
	obj.write(response.read())
	obj.close()
