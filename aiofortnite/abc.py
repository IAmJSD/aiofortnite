'''
========================================
abc.py - Copyright (C) Jake Gealer 2018.
Licensed under the MPL-2.0 license.
https://www.mozilla.org/en-US/MPL/2.0/
========================================
This file contains classes which are used across the project.
'''


class Modes:
    solo = "_p2"
    duo = "_p10"
    squad = "_p9"
    all = "_p"
# A ABC list of all of the request modes.


class ModeStatBase:
    score = 0
    matches = 0
    time = 0
    kills = 0
    wins = 0
    top3 = 0
    top5 = 0
    top6 = 0
    top10 = 0
    top12 = 0
    top25 = 0
# A ABC for the base of the modes.


class PlatformStatBase:
    class solo(ModeStatBase):
        pass

    class duo(ModeStatBase):
        pass

    class squad(ModeStatBase):
        pass

    class all(ModeStatBase):
        pass

    class other(ModeStatBase):
        pass
# A ABC for the platforms to inherit from.


class UserStats:
    class pc(PlatformStatBase):
        pass

    class ps4(PlatformStatBase):
        pass

    class xbox_one(PlatformStatBase):
        pass

    class other(PlatformStatBase):
        pass

    def __init__(self, stats_json):
        for stat in stats_json:
            if "pc" in stat.get("name"):
                if Modes.all in stat.get("name"):
                    if 'score_' in stat.get('name'):
                        self.pc.all.score += stat.get('value')
                    elif 'matchesplayed_' in stat.get('name'):
                        self.pc.all.matches += stat.get('value')
                    elif 'minutesplayed_' in stat.get('name'):
                        self.pc.all.time += stat.get('value')
                    elif 'kills_' in stat.get('name'):
                        self.pc.all.kills += stat.get('value')
                    elif 'placetop1_' in stat.get('name'):
                        self.pc.all.wins += stat.get('value')
                    elif 'placetop3_' in stat.get('name'):
                        self.pc.all.top3 += stat.get('value')
                    elif 'placetop5_' in stat.get('name'):
                        self.pc.all.top5 += stat.get('value')
                    elif 'placetop6_' in stat.get('name'):
                        self.pc.all.top6 += stat.get('value')
                    elif 'placetop10_' in stat.get('name'):
                        self.pc.all.top10 += stat.get('value')
                    elif 'placetop12_' in stat.get('name'):
                        self.pc.all.top12 += stat.get('value')
                    elif 'placetop25_' in stat.get('name'):
                        self.pc.all.top25 += stat.get('value')
                elif Modes.duo in stat.get("name"):
                    if 'score_' in stat.get('name'):
                        self.pc.duo.score += stat.get('value')
                    elif 'matchesplayed_' in stat.get('name'):
                        self.pc.duo.matches += stat.get('value')
                    elif 'minutesplayed_' in stat.get('name'):
                        self.pc.duo.time += stat.get('value')
                    elif 'kills_' in stat.get('name'):
                        self.pc.duo.kills += stat.get('value')
                    elif 'placetop1_' in stat.get('name'):
                        self.pc.duo.wins += stat.get('value')
                    elif 'placetop3_' in stat.get('name'):
                        self.pc.duo.top3 += stat.get('value')
                    elif 'placetop5_' in stat.get('name'):
                        self.pc.duo.top5 += stat.get('value')
                    elif 'placetop6_' in stat.get('name'):
                        self.pc.duo.top6 += stat.get('value')
                    elif 'placetop10_' in stat.get('name'):
                        self.pc.duo.top10 += stat.get('value')
                    elif 'placetop12_' in stat.get('name'):
                        self.pc.duo.top12 += stat.get('value')
                    elif 'placetop25_' in stat.get('name'):
                        self.pc.duo.top25 += stat.get('value')
                elif Modes.solo in stat.get("name"):
                    if 'score_' in stat.get('name'):
                        self.pc.solo.score += stat.get('value')
                    elif 'matchesplayed_' in stat.get('name'):
                        self.pc.solo.matches += stat.get('value')
                    elif 'minutesplayed_' in stat.get('name'):
                        self.pc.solo.time += stat.get('value')
                    elif 'kills_' in stat.get('name'):
                        self.pc.solo.kills += stat.get('value')
                    elif 'placetop1_' in stat.get('name'):
                        self.pc.solo.wins += stat.get('value')
                    elif 'placetop3_' in stat.get('name'):
                        self.pc.solo.top3 += stat.get('value')
                    elif 'placetop5_' in stat.get('name'):
                        self.pc.solo.top5 += stat.get('value')
                    elif 'placetop6_' in stat.get('name'):
                        self.pc.solo.top6 += stat.get('value')
                    elif 'placetop10_' in stat.get('name'):
                        self.pc.solo.top10 += stat.get('value')
                    elif 'placetop12_' in stat.get('name'):
                        self.pc.solo.top12 += stat.get('value')
                    elif 'placetop25_' in stat.get('name'):
                        self.pc.solo.top25 += stat.get('value')
                elif Modes.squad in stat.get("name"):
                    if 'score_' in stat.get('name'):
                        self.pc.squad.score += stat.get('value')
                    elif 'matchesplayed_' in stat.get('name'):
                        self.pc.squad.matches += stat.get('value')
                    elif 'minutesplayed_' in stat.get('name'):
                        self.pc.squad.time += stat.get('value')
                    elif 'kills_' in stat.get('name'):
                        self.pc.squad.kills += stat.get('value')
                    elif 'placetop1_' in stat.get('name'):
                        self.pc.squad.wins += stat.get('value')
                    elif 'placetop3_' in stat.get('name'):
                        self.pc.squad.top3 += stat.get('value')
                    elif 'placetop5_' in stat.get('name'):
                        self.pc.squad.top5 += stat.get('value')
                    elif 'placetop6_' in stat.get('name'):
                        self.pc.squad.top6 += stat.get('value')
                    elif 'placetop10_' in stat.get('name'):
                        self.pc.squad.top10 += stat.get('value')
                    elif 'placetop12_' in stat.get('name'):
                        self.pc.squad.top12 += stat.get('value')
                    elif 'placetop25_' in stat.get('name'):
                        self.pc.squad.top25 += stat.get('value')
                else:
                    if 'score_' in stat.get('name'):
                        self.pc.other.score += stat.get('value')
                    elif 'matchesplayed_' in stat.get('name'):
                        self.pc.other.matches += stat.get('value')
                    elif 'minutesplayed_' in stat.get('name'):
                        self.pc.other.time += stat.get('value')
                    elif 'kills_' in stat.get('name'):
                        self.pc.other.kills += stat.get('value')
                    elif 'placetop1_' in stat.get('name'):
                        self.pc.other.wins += stat.get('value')
                    elif 'placetop3_' in stat.get('name'):
                        self.pc.other.top3 += stat.get('value')
                    elif 'placetop5_' in stat.get('name'):
                        self.pc.other.top5 += stat.get('value')
                    elif 'placetop6_' in stat.get('name'):
                        self.pc.other.top6 += stat.get('value')
                    elif 'placetop10_' in stat.get('name'):
                        self.pc.other.top10 += stat.get('value')
                    elif 'placetop12_' in stat.get('name'):
                        self.pc.other.top12 += stat.get('value')
                    elif 'placetop25_' in stat.get('name'):
                        self.pc.other.top25 += stat.get('value')
            elif "xb1" in stat.get("name"):
                if Modes.all in stat.get("name"):
                    if 'score_' in stat.get('name'):
                        self.xbox_one.all.score += stat.get('value')
                    elif 'matchesplayed_' in stat.get('name'):
                        self.xbox_one.all.matches += stat.get('value')
                    elif 'minutesplayed_' in stat.get('name'):
                        self.xbox_one.all.time += stat.get('value')
                    elif 'kills_' in stat.get('name'):
                        self.xbox_one.all.kills += stat.get('value')
                    elif 'placetop1_' in stat.get('name'):
                        self.xbox_one.all.wins += stat.get('value')
                    elif 'placetop3_' in stat.get('name'):
                        self.xbox_one.all.top3 += stat.get('value')
                    elif 'placetop5_' in stat.get('name'):
                        self.xbox_one.all.top5 += stat.get('value')
                    elif 'placetop6_' in stat.get('name'):
                        self.xbox_one.all.top6 += stat.get('value')
                    elif 'placetop10_' in stat.get('name'):
                        self.xbox_one.all.top10 += stat.get('value')
                    elif 'placetop12_' in stat.get('name'):
                        self.xbox_one.all.top12 += stat.get('value')
                    elif 'placetop25_' in stat.get('name'):
                        self.xbox_one.all.top25 += stat.get('value')
                elif Modes.duo in stat.get("name"):
                    if 'score_' in stat.get('name'):
                        self.xbox_one.duo.score += stat.get('value')
                    elif 'matchesplayed_' in stat.get('name'):
                        self.xbox_one.duo.matches += stat.get('value')
                    elif 'minutesplayed_' in stat.get('name'):
                        self.xbox_one.duo.time += stat.get('value')
                    elif 'kills_' in stat.get('name'):
                        self.xbox_one.duo.kills += stat.get('value')
                    elif 'placetop1_' in stat.get('name'):
                        self.xbox_one.duo.wins += stat.get('value')
                    elif 'placetop3_' in stat.get('name'):
                        self.xbox_one.duo.top3 += stat.get('value')
                    elif 'placetop5_' in stat.get('name'):
                        self.xbox_one.duo.top5 += stat.get('value')
                    elif 'placetop6_' in stat.get('name'):
                        self.xbox_one.duo.top6 += stat.get('value')
                    elif 'placetop10_' in stat.get('name'):
                        self.xbox_one.duo.top10 += stat.get('value')
                    elif 'placetop12_' in stat.get('name'):
                        self.xbox_one.duo.top12 += stat.get('value')
                    elif 'placetop25_' in stat.get('name'):
                        self.xbox_one.duo.top25 += stat.get('value')
                elif Modes.solo in stat.get("name"):
                    if 'score_' in stat.get('name'):
                        self.xbox_one.solo.score += stat.get('value')
                    elif 'matchesplayed_' in stat.get('name'):
                        self.xbox_one.solo.matches += stat.get('value')
                    elif 'minutesplayed_' in stat.get('name'):
                        self.xbox_one.solo.time += stat.get('value')
                    elif 'kills_' in stat.get('name'):
                        self.xbox_one.solo.kills += stat.get('value')
                    elif 'placetop1_' in stat.get('name'):
                        self.xbox_one.solo.wins += stat.get('value')
                    elif 'placetop3_' in stat.get('name'):
                        self.xbox_one.solo.top3 += stat.get('value')
                    elif 'placetop5_' in stat.get('name'):
                        self.xbox_one.solo.top5 += stat.get('value')
                    elif 'placetop6_' in stat.get('name'):
                        self.xbox_one.solo.top6 += stat.get('value')
                    elif 'placetop10_' in stat.get('name'):
                        self.xbox_one.solo.top10 += stat.get('value')
                    elif 'placetop12_' in stat.get('name'):
                        self.xbox_one.solo.top12 += stat.get('value')
                    elif 'placetop25_' in stat.get('name'):
                        self.xbox_one.solo.top25 += stat.get('value')
                elif Modes.squad in stat.get("name"):
                    if 'score_' in stat.get('name'):
                        self.xbox_one.squad.score += stat.get('value')
                    elif 'matchesplayed_' in stat.get('name'):
                        self.xbox_one.squad.matches += stat.get('value')
                    elif 'minutesplayed_' in stat.get('name'):
                        self.xbox_one.squad.time += stat.get('value')
                    elif 'kills_' in stat.get('name'):
                        self.xbox_one.squad.kills += stat.get('value')
                    elif 'placetop1_' in stat.get('name'):
                        self.xbox_one.squad.wins += stat.get('value')
                    elif 'placetop3_' in stat.get('name'):
                        self.xbox_one.squad.top3 += stat.get('value')
                    elif 'placetop5_' in stat.get('name'):
                        self.xbox_one.squad.top5 += stat.get('value')
                    elif 'placetop6_' in stat.get('name'):
                        self.xbox_one.squad.top6 += stat.get('value')
                    elif 'placetop10_' in stat.get('name'):
                        self.xbox_one.squad.top10 += stat.get('value')
                    elif 'placetop12_' in stat.get('name'):
                        self.xbox_one.squad.top12 += stat.get('value')
                    elif 'placetop25_' in stat.get('name'):
                        self.xbox_one.squad.top25 += stat.get('value')
                else:
                    if 'score_' in stat.get('name'):
                        self.xbox_one.other.score += stat.get('value')
                    elif 'matchesplayed_' in stat.get('name'):
                        self.xbox_one.other.matches += stat.get('value')
                    elif 'minutesplayed_' in stat.get('name'):
                        self.xbox_one.other.time += stat.get('value')
                    elif 'kills_' in stat.get('name'):
                        self.xbox_one.other.kills += stat.get('value')
                    elif 'placetop1_' in stat.get('name'):
                        self.xbox_one.other.wins += stat.get('value')
                    elif 'placetop3_' in stat.get('name'):
                        self.xbox_one.other.top3 += stat.get('value')
                    elif 'placetop5_' in stat.get('name'):
                        self.xbox_one.other.top5 += stat.get('value')
                    elif 'placetop6_' in stat.get('name'):
                        self.xbox_one.other.top6 += stat.get('value')
                    elif 'placetop10_' in stat.get('name'):
                        self.xbox_one.other.top10 += stat.get('value')
                    elif 'placetop12_' in stat.get('name'):
                        self.xbox_one.other.top12 += stat.get('value')
                    elif 'placetop25_' in stat.get('name'):
                        self.xbox_one.other.top25 += stat.get('value')
            elif "ps4" in stat.get("name"):
                if Modes.all in stat.get("name"):
                    if 'score_' in stat.get('name'):
                        self.ps4.all.score += stat.get('value')
                    elif 'matchesplayed_' in stat.get('name'):
                        self.ps4.all.matches += stat.get('value')
                    elif 'minutesplayed_' in stat.get('name'):
                        self.ps4.all.time += stat.get('value')
                    elif 'kills_' in stat.get('name'):
                        self.ps4.all.kills += stat.get('value')
                    elif 'placetop1_' in stat.get('name'):
                        self.ps4.all.wins += stat.get('value')
                    elif 'placetop3_' in stat.get('name'):
                        self.ps4.all.top3 += stat.get('value')
                    elif 'placetop5_' in stat.get('name'):
                        self.ps4.all.top5 += stat.get('value')
                    elif 'placetop6_' in stat.get('name'):
                        self.ps4.all.top6 += stat.get('value')
                    elif 'placetop10_' in stat.get('name'):
                        self.ps4.all.top10 += stat.get('value')
                    elif 'placetop12_' in stat.get('name'):
                        self.ps4.all.top12 += stat.get('value')
                    elif 'placetop25_' in stat.get('name'):
                        self.ps4.all.top25 += stat.get('value')
                elif Modes.duo in stat.get("name"):
                    if 'score_' in stat.get('name'):
                        self.ps4.duo.score += stat.get('value')
                    elif 'matchesplayed_' in stat.get('name'):
                        self.ps4.duo.matches += stat.get('value')
                    elif 'minutesplayed_' in stat.get('name'):
                        self.ps4.duo.time += stat.get('value')
                    elif 'kills_' in stat.get('name'):
                        self.ps4.duo.kills += stat.get('value')
                    elif 'placetop1_' in stat.get('name'):
                        self.ps4.duo.wins += stat.get('value')
                    elif 'placetop3_' in stat.get('name'):
                        self.ps4.duo.top3 += stat.get('value')
                    elif 'placetop5_' in stat.get('name'):
                        self.ps4.duo.top5 += stat.get('value')
                    elif 'placetop6_' in stat.get('name'):
                        self.ps4.duo.top6 += stat.get('value')
                    elif 'placetop10_' in stat.get('name'):
                        self.ps4.duo.top10 += stat.get('value')
                    elif 'placetop12_' in stat.get('name'):
                        self.ps4.duo.top12 += stat.get('value')
                    elif 'placetop25_' in stat.get('name'):
                        self.ps4.duo.top25 += stat.get('value')
                elif Modes.solo in stat.get("name"):
                    if 'score_' in stat.get('name'):
                        self.ps4.solo.score += stat.get('value')
                    elif 'matchesplayed_' in stat.get('name'):
                        self.ps4.solo.matches += stat.get('value')
                    elif 'minutesplayed_' in stat.get('name'):
                        self.ps4.solo.time += stat.get('value')
                    elif 'kills_' in stat.get('name'):
                        self.ps4.solo.kills += stat.get('value')
                    elif 'placetop1_' in stat.get('name'):
                        self.ps4.solo.wins += stat.get('value')
                    elif 'placetop3_' in stat.get('name'):
                        self.ps4.solo.top3 += stat.get('value')
                    elif 'placetop5_' in stat.get('name'):
                        self.ps4.solo.top5 += stat.get('value')
                    elif 'placetop6_' in stat.get('name'):
                        self.ps4.solo.top6 += stat.get('value')
                    elif 'placetop10_' in stat.get('name'):
                        self.ps4.solo.top10 += stat.get('value')
                    elif 'placetop12_' in stat.get('name'):
                        self.ps4.solo.top12 += stat.get('value')
                    elif 'placetop25_' in stat.get('name'):
                        self.ps4.solo.top25 += stat.get('value')
                elif Modes.squad in stat.get("name"):
                    if 'score_' in stat.get('name'):
                        self.ps4.squad.score += stat.get('value')
                    elif 'matchesplayed_' in stat.get('name'):
                        self.ps4.squad.matches += stat.get('value')
                    elif 'minutesplayed_' in stat.get('name'):
                        self.ps4.squad.time += stat.get('value')
                    elif 'kills_' in stat.get('name'):
                        self.ps4.squad.kills += stat.get('value')
                    elif 'placetop1_' in stat.get('name'):
                        self.ps4.squad.wins += stat.get('value')
                    elif 'placetop3_' in stat.get('name'):
                        self.ps4.squad.top3 += stat.get('value')
                    elif 'placetop5_' in stat.get('name'):
                        self.ps4.squad.top5 += stat.get('value')
                    elif 'placetop6_' in stat.get('name'):
                        self.ps4.squad.top6 += stat.get('value')
                    elif 'placetop10_' in stat.get('name'):
                        self.ps4.squad.top10 += stat.get('value')
                    elif 'placetop12_' in stat.get('name'):
                        self.ps4.squad.top12 += stat.get('value')
                    elif 'placetop25_' in stat.get('name'):
                        self.ps4.squad.top25 += stat.get('value')
                else:
                    if 'score_' in stat.get('name'):
                        self.ps4.other.score += stat.get('value')
                    elif 'matchesplayed_' in stat.get('name'):
                        self.ps4.other.matches += stat.get('value')
                    elif 'minutesplayed_' in stat.get('name'):
                        self.ps4.other.time += stat.get('value')
                    elif 'kills_' in stat.get('name'):
                        self.ps4.other.kills += stat.get('value')
                    elif 'placetop1_' in stat.get('name'):
                        self.ps4.other.wins += stat.get('value')
                    elif 'placetop3_' in stat.get('name'):
                        self.ps4.other.top3 += stat.get('value')
                    elif 'placetop5_' in stat.get('name'):
                        self.ps4.other.top5 += stat.get('value')
                    elif 'placetop6_' in stat.get('name'):
                        self.ps4.other.top6 += stat.get('value')
                    elif 'placetop10_' in stat.get('name'):
                        self.ps4.other.top10 += stat.get('value')
                    elif 'placetop12_' in stat.get('name'):
                        self.ps4.other.top12 += stat.get('value')
                    elif 'placetop25_' in stat.get('name'):
                        self.ps4.other.top25 += stat.get('value')
            else:
                if Modes.all in stat.get("name"):
                    if 'score_' in stat.get('name'):
                        self.other.all.score += stat.get('value')
                    elif 'matchesplayed_' in stat.get('name'):
                        self.other.all.matches += stat.get('value')
                    elif 'minutesplayed_' in stat.get('name'):
                        self.other.all.time += stat.get('value')
                    elif 'kills_' in stat.get('name'):
                        self.other.all.kills += stat.get('value')
                    elif 'placetop1_' in stat.get('name'):
                        self.other.all.wins += stat.get('value')
                    elif 'placetop3_' in stat.get('name'):
                        self.other.all.top3 += stat.get('value')
                    elif 'placetop5_' in stat.get('name'):
                        self.other.all.top5 += stat.get('value')
                    elif 'placetop6_' in stat.get('name'):
                        self.other.all.top6 += stat.get('value')
                    elif 'placetop10_' in stat.get('name'):
                        self.other.all.top10 += stat.get('value')
                    elif 'placetop12_' in stat.get('name'):
                        self.other.all.top12 += stat.get('value')
                    elif 'placetop25_' in stat.get('name'):
                        self.other.all.top25 += stat.get('value')
                elif Modes.duo in stat.get("name"):
                    if 'score_' in stat.get('name'):
                        self.other.duo.score += stat.get('value')
                    elif 'matchesplayed_' in stat.get('name'):
                        self.other.duo.matches += stat.get('value')
                    elif 'minutesplayed_' in stat.get('name'):
                        self.other.duo.time += stat.get('value')
                    elif 'kills_' in stat.get('name'):
                        self.other.duo.kills += stat.get('value')
                    elif 'placetop1_' in stat.get('name'):
                        self.other.duo.wins += stat.get('value')
                    elif 'placetop3_' in stat.get('name'):
                        self.other.duo.top3 += stat.get('value')
                    elif 'placetop5_' in stat.get('name'):
                        self.other.duo.top5 += stat.get('value')
                    elif 'placetop6_' in stat.get('name'):
                        self.other.duo.top6 += stat.get('value')
                    elif 'placetop10_' in stat.get('name'):
                        self.other.duo.top10 += stat.get('value')
                    elif 'placetop12_' in stat.get('name'):
                        self.other.duo.top12 += stat.get('value')
                    elif 'placetop25_' in stat.get('name'):
                        self.other.duo.top25 += stat.get('value')
                elif Modes.solo in stat.get("name"):
                    if 'score_' in stat.get('name'):
                        self.other.solo.score += stat.get('value')
                    elif 'matchesplayed_' in stat.get('name'):
                        self.other.solo.matches += stat.get('value')
                    elif 'minutesplayed_' in stat.get('name'):
                        self.other.solo.time += stat.get('value')
                    elif 'kills_' in stat.get('name'):
                        self.other.solo.kills += stat.get('value')
                    elif 'placetop1_' in stat.get('name'):
                        self.other.solo.wins += stat.get('value')
                    elif 'placetop3_' in stat.get('name'):
                        self.other.solo.top3 += stat.get('value')
                    elif 'placetop5_' in stat.get('name'):
                        self.other.solo.top5 += stat.get('value')
                    elif 'placetop6_' in stat.get('name'):
                        self.other.solo.top6 += stat.get('value')
                    elif 'placetop10_' in stat.get('name'):
                        self.other.solo.top10 += stat.get('value')
                    elif 'placetop12_' in stat.get('name'):
                        self.other.solo.top12 += stat.get('value')
                    elif 'placetop25_' in stat.get('name'):
                        self.other.solo.top25 += stat.get('value')
                elif Modes.squad in stat.get("name"):
                    if 'score_' in stat.get('name'):
                        self.other.squad.score += stat.get('value')
                    elif 'matchesplayed_' in stat.get('name'):
                        self.other.squad.matches += stat.get('value')
                    elif 'minutesplayed_' in stat.get('name'):
                        self.other.squad.time += stat.get('value')
                    elif 'kills_' in stat.get('name'):
                        self.other.squad.kills += stat.get('value')
                    elif 'placetop1_' in stat.get('name'):
                        self.other.squad.wins += stat.get('value')
                    elif 'placetop3_' in stat.get('name'):
                        self.other.squad.top3 += stat.get('value')
                    elif 'placetop5_' in stat.get('name'):
                        self.other.squad.top5 += stat.get('value')
                    elif 'placetop6_' in stat.get('name'):
                        self.other.squad.top6 += stat.get('value')
                    elif 'placetop10_' in stat.get('name'):
                        self.other.squad.top10 += stat.get('value')
                    elif 'placetop12_' in stat.get('name'):
                        self.other.squad.top12 += stat.get('value')
                    elif 'placetop25_' in stat.get('name'):
                        self.other.squad.top25 += stat.get('value')
                else:
                    if 'score_' in stat.get('name'):
                        self.other.other.score += stat.get('value')
                    elif 'matchesplayed_' in stat.get('name'):
                        self.other.other.matches += stat.get('value')
                    elif 'minutesplayed_' in stat.get('name'):
                        self.other.other.time += stat.get('value')
                    elif 'kills_' in stat.get('name'):
                        self.other.other.kills += stat.get('value')
                    elif 'placetop1_' in stat.get('name'):
                        self.other.other.wins += stat.get('value')
                    elif 'placetop3_' in stat.get('name'):
                        self.other.other.top3 += stat.get('value')
                    elif 'placetop5_' in stat.get('name'):
                        self.other.other.top5 += stat.get('value')
                    elif 'placetop6_' in stat.get('name'):
                        self.other.other.top6 += stat.get('value')
                    elif 'placetop10_' in stat.get('name'):
                        self.other.other.top10 += stat.get('value')
                    elif 'placetop12_' in stat.get('name'):
                        self.other.other.top12 += stat.get('value')
                    elif 'placetop25_' in stat.get('name'):
                        self.other.other.top25 += stat.get('value')
# The ABC class for user stats.


class User:
    value = None
    rank = None

    def __init__(self, username, user_id, stats_json):
        self.username = username.lower()
        self.id = user_id
        if stats_json:
            self.stats = UserStats(stats_json)
        else:
            self.stats = None
# The user ABC class.


class LoginError(Exception):
    pass
# The ABC class for a error logging in.


class Platforms:
    pc = "pc"
    ps4 = "ps4"
    xbox_one = "xb1"
# A class of all of the platforms.


class News:
    def __init__(self, news_json):
        self.image = news_json["image"]
        self.title = news_json["title"]
        self.body = news_json["body"]
# A ABC class for the news.
