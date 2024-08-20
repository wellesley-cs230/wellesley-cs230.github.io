serve:
	python render_schedule.py > schedule.md && bundle exec jekyll serve

install:
	bundle install
