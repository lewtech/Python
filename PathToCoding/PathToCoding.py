class JobSeeker(object):
    name = "Lew Flauta"
    goal = "get C# Developer @ Sysmex"
    level0 = "2 hour overview"
    level1 = "intermediate class"
    level2 = "expert class"
    level3 = "interview @ sysmex"

    state_mental = "good"
    state_physical = "good"
    mental_mindset = "growth mindset"
    status_portfolio_projects = 0
    status_resume = 1


jobseeker = JobSeeker()


def main():
    get_job()


def get_job():
    print("bucket goal: " + jobseeker.goal)
    print("level 0: " + jobseeker.level0)
    print("level 1: " + jobseeker.level1)
    print("level 2: " + jobseeker.level2)
    print("boss battle: " + jobseeker.level3)
    get_job_good_portfolio()
    get_job_research_companies()
    get_job_get_noticed()


def get_job_good_portfolio():
    pass


def get_job_get_noticed():
    pass


def get_job_research_companies():
    pass


def daily_actions():
    daily_standup()
    daily_algorithm_practice()
    daily_morning_routine()


def interview_prep():
    pass


def daily_standup():
    pass


def daily_algorithm_practice():
    pass


def daily_morning_routine():
    pass


def states_mental_state():
    pass


main()
