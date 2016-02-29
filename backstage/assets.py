from django_assets import Bundle, register

js_files = [
    'static/js/vendor/fancybox/jquery.fancybox.js',
]

js = Bundle(*js_files, filters='jsmin', output='static/js/bundle.js')

register('js_all', js)
