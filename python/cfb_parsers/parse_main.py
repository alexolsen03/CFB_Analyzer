import glob, os
import csv
import parse_rushing
import parse_passing
import parse_redzone
import parse_turnover

with open('team_stats.csv', 'w') as f:
	writer = csv.writer(f)
	writer.writerow(['id','team_id', 'opponent_id', 'date', 'away_game', 'points_for', 'points_agst', 'result', 'game_time', 'attendance', 'surface', 'rushing_attempts_for', 'rushing_yards_for', 'rushing_tds_for', 'rushing_attempts_agst', 'rushing_yards_agst', 'rushing_tds_agst', 'passing_attempts_for', 'passing_completions_for', 'passing_yards_for', 'passing_tds_for', 'passing_ints_for', 'passing_attempts_agst', 'passing_completions_agst', 'passing_yards_agst', 'passing_tds_agst', 'passing_ints_agst', 'red_zone_attempts_offense', 'red_zone_scores_offense', 'red_zone_touchdowns_offense', 'red_zone_field_goals_offense','red_zone_attempts_defense', 'red_zone_scores_defense', 'red_zone_touchdowns_defense', 'red_zone_field_goals_defense'])

	ctr = 1
	for file in glob.glob("html/*.html"):
		team_id = file.split('/')[1].split('.')[0].split('_')[1]

		idx = 0
		schedule 		= parse.parseSchedule(file, False)
		rush_stats_for	= parse_by_game.parseRushingFor(team_id, False)
		rush_stats_agst	= parse_by_game.parseRushingAgst(team_id, False)
		pass_stats_for 	= parse_by_game.parsePassingFor(team_id, False)
		pass_stats_agst	= parse_by_game.parsePassingAgst(team_id, False)
		red_zone_o	= parse_red_zone_split.parseRedZoneOffense(team_id, False)
		red_zone_d	= parse_red_zone_split.parseRedZoneDefense(team_id, False)


		for opponent in schedule:
			writer.writerow([
			ctr,
			opponent['teamId'],
			opponent['opponentId'],
			opponent['date'],
			opponent['isAway'],
			opponent['ptsFor'],
			opponent['ptsAgst'],
			opponent['result'],
			opponent['gameTime'],
			opponent['attendance'],
			rush_stats_for[idx]['surface'],
			rush_stats_for[idx]['attempts'],
			rush_stats_for[idx]['yards'],
			rush_stats_for[idx]['touchdowns'],
			rush_stats_agst[idx]['attempts'],
			rush_stats_agst[idx]['yards'],
			rush_stats_agst[idx]['touchdowns'],
			pass_stats_for[idx]['attempts'],
			pass_stats_for[idx]['completions'],
			pass_stats_for[idx]['yards'],
			pass_stats_for[idx]['touchdowns'],
			pass_stats_for[idx]['ints'],
			pass_stats_agst[idx]['attempts'],
			pass_stats_agst[idx]['completions'],
			pass_stats_agst[idx]['yards'],
			pass_stats_agst[idx]['touchdowns'],
			pass_stats_agst[idx]['ints'],
			red_zone_o[idx]['attempts'],
			red_zone_o[idx]['scores'],
			red_zone_o[idx]['touchdowns'],
			red_zone_o[idx]['fieldGoals'],
			red_zone_d[idx]['attempts'],
			red_zone_d[idx]['scores'],
			red_zone_d[idx]['touchdowns'],
			red_zone_d[idx]['fieldGoals']
			])
			ctr = ctr + 1
			idx = idx + 1