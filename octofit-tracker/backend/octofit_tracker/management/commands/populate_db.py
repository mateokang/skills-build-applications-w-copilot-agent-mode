from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.conf import settings
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Connect to MongoDB directly for index creation
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']
        db.users.create_index('email', unique=True)

        # Clear all collections
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Users
        users = [
            User(email='tony@stark.com', name='Tony Stark', team='Marvel', is_superhero=True),
            User(email='steve@rogers.com', name='Steve Rogers', team='Marvel', is_superhero=True),
            User(email='bruce@wayne.com', name='Bruce Wayne', team='DC', is_superhero=True),
            User(email='clark@kent.com', name='Clark Kent', team='DC', is_superhero=True),
        ]
        User.objects.bulk_create(users)

        # Activities
        Activity.objects.create(user='tony@stark.com', activity_type='run', duration=30, date='2025-12-01')
        Activity.objects.create(user='steve@rogers.com', activity_type='swim', duration=45, date='2025-12-02')
        Activity.objects.create(user='bruce@wayne.com', activity_type='cycle', duration=60, date='2025-12-03')
        Activity.objects.create(user='clark@kent.com', activity_type='fly', duration=120, date='2025-12-04')

        # Leaderboard
        Leaderboard.objects.create(team='Marvel', points=150)
        Leaderboard.objects.create(team='DC', points=180)

        # Workouts
        Workout.objects.create(name='Pushups', description='Do 20 pushups', difficulty='Easy')
        Workout.objects.create(name='Sprints', description='Sprint 100m x 5', difficulty='Medium')
        Workout.objects.create(name='Deadlift', description='Deadlift 100kg', difficulty='Hard')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
