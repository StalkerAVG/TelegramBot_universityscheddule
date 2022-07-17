import os

token = "5242691084:AAFF0TyQbbGNyq7yTYuWmAbsNQ8PNSoQ80o"
days = ['Понеділок', 'Вівторок', 'Середа', 'Четвер', 'П\'ятниця']
lstgrps = [f.name for f in os.scandir('groups') if f.is_dir() ]
groups = {}