from markdown2 import markdown
from jinja2 import Environment, FileSystemLoader
from json import load


template_env=Environment(loader=FileSystemLoader(searchpath='./'))
# ^ load from current directory "./", you can adjust to preference

template = template_env.get_template('layout.html')


# open json config file
#   with open ('config.json') as config_file:
#        config=load(config_file)


# open markdown article
with open('article.md') as markdown_file:
    article=markdown(markdown_file.read())

    
# write new html file
with open('new.html','w') as output_file:
    output_file.write(
        template.render(
            article=article
        )
    )
