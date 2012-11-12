from fanstatic import Library, Resource

library = Library('raphael', 'resources')

raphael = Resource(library, 'raphael.js', minified='raphael-min.js')
