import os

token = ""
days = ['Понеділок', 'Вівторок', 'Середа', 'Четвер', 'П\'ятниця']
lstgrps = [f.name for f in os.scandir('groups') if f.is_dir() ]#getting list of groups
groups = {}
