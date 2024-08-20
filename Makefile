serve:
	python render_schedule.py > schedule.md && bundle exec jekyll serve

install:
	bundle install

activate:
	mm activate cs230-web

env:
	pip freeze > requirements.txt
