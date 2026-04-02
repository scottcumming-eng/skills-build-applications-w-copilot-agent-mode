
from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear collections
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Users
        ironman = User.objects.create_user(username='ironman', email='ironman@marvel.com', password='password')
        cap = User.objects.create_user(username='captainamerica', email='cap@marvel.com', password='password')
        batman = User.objects.create_user(username='batman', email='batman@dc.com', password='password')
        wonderwoman = User.objects.create_user(username='wonderwoman', email='wonderwoman@dc.com', password='password')

        # Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')
        marvel.members.set([ironman, cap])
        dc.members.set([batman, wonderwoman])

        # Activities
        Activity.objects.create(user=ironman, activity_type='Running', duration=30)
        Activity.objects.create(user=cap, activity_type='Cycling', duration=45)
        Activity.objects.create(user=batman, activity_type='Swimming', duration=60)
        Activity.objects.create(user=wonderwoman, activity_type='Yoga', duration=50)

        # Leaderboard
        Leaderboard.objects.create(team=marvel, points=75)
        Leaderboard.objects.create(team=dc, points=110)

        # Workouts
        Workout.objects.create(name='Super Strength', difficulty='Hard')
        Workout.objects.create(name='Flight Training', difficulty='Medium')
        Workout.objects.create(name='Stealth Ops', difficulty='Hard')
        Workout.objects.create(name='Shield Practice', difficulty='Easy')

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data.'))