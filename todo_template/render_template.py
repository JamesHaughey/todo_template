#!/usr/bin/env python 
# Standard library imports.
from datetime import datetime, timedelta
from pathlib import Path

# Related third party imports.
from jinja2 import Environment, FileSystemLoader, select_autoescape, Template, PackageLoader

# Local application/library specific imports.


class TodoTemplate():
    def __init__(self, template_name: str = 'todo_template.md'):
        self._env = Environment(
            loader=PackageLoader(package_name="todo_template"),
            autoescape=select_autoescape(['html', 'xml'])
        )
        self._template = self._env.get_template(template_name)

    def return_date_dict(self, now: datetime = datetime.now()):
        daily_fmt = "%d/%m/%Y"
        monday = now - timedelta(days=now.weekday())
        return {
            'title_date': monday.strftime('%Y.%m.%d'),
            'tag_date': monday.strftime('%m_%B'),
            'monday_date': monday.strftime(daily_fmt),
            'tuesday_date': (monday+timedelta(days=1)).strftime(daily_fmt),
            'wednesday_date': (monday+timedelta(days=2)).strftime(daily_fmt),
            'thursday_date': (monday+timedelta(days=3)).strftime(daily_fmt),
            'friday_date': (monday+timedelta(days=4)).strftime(daily_fmt),
            'year': monday.strftime('%Y'),
            'month': monday.strftime('%m'),
        }

    def render_today_template(self):
        todo_dates = self.return_date_dict() 
        render = self._template.render(config=todo_dates)
        folder = f'{todo_dates["year"]}/{todo_dates["month"]}'
        todo_folder_path = Path(f'{folder}')
        todo_folder_path.mkdir(parents=True, exist_ok=True)
        todo_path = todo_folder_path / f'{todo_dates["title_date"]}_weekly_todo.md'
        
        with todo_path.open('w') as fh:
            fh.write(render)

    # def render_template(self, config, )

if __name__ == "__main__":
    todo = TodoTemplate()
    todo.render_today_template()
