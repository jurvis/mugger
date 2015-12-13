# Mugger
This project just generates a very simple site with no CSS whatsoever with a list of modules you're taking and the corresponding notes that you've taken.

My use-case is very specific:
1. Export my notes from Markdown to HTML with Ulysses (which helps me inject the CSS I want)
2. Copy HTML file to corresponding folder in `modules/`
3. Run generate.py and update my site accordingly

You can see an example at: [http://lab.jurvis.co/repo](http://lab.jurvis.co/repo)

It's really nothing fancy so you can probably stop reading now.

## Future Plans
1. A build system
2. Better naming
3. Supports uploading

## Dependencies
- jinja2

## Installation
1. Clone
2. `pip install jinja2`
3. Add files to `modules`
4. `python generate.py`
