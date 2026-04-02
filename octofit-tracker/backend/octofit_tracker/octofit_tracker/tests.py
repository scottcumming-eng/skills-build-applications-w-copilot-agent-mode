from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelTests(TestCase):
    def test_create_user(self):
        user = User.objects.create_user(username='test', email='test@example.com', password='pass')
        self.assertEqual(user.email, 'test@example.com')

    def test_create_team(self):
        user = User.objects.create_user(username='test2', email='test2@example.com', password='pass')
        team = Team.objects.create(name='Testers')
        team.members.add(user)
        self.assertIn(user, team.members.all())

    def test_create_activity(self):
        user = User.objects.create_user(username='test3', email='test3@example.com', password='pass')
        activity = Activity.objects.create(user=user, activity_type='Run', duration=30)
        self.assertEqual(activity.activity_type, 'Run')

    def test_create_leaderboard(self):
        team = Team.objects.create(name='Leaders')
        leaderboard = Leaderboard.objects.create(team=team, points=100)
        self.assertEqual(leaderboard.points, 100)

    def test_create_workout(self):
        workout = Workout.objects.create(name='Pushups', difficulty='Easy')
        self.assertEqual(workout.name, 'Pushups')
