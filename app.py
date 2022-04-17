import sys

from flask import Flask
from flask_s3_viewer import FlaskS3Viewer
from flask_s3_viewer.aws.ref import Region

app = Flask(__name__)

# For test, disable template caching
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1
app.config['TEMPLATES_AUTO_RELOAD'] = True

# FlaskS3Viewer Init
s3viewer = FlaskS3Viewer(
    app, # Flask app
    namespace='occ-s3-viewer', # namespace be unique
    
    object_hostname='http://localhost:9000', # file's hostname
    allowed_extensions={}, # allowed extension
    template_namespace='customized',
    config={ # Bucket configs and else
        'profile_name': None,
        
        'access_key': 'FENUEPE4UL6LEEDA8DFY',
        'secret_key': 'vjSh6c+sbHrt2d2NoiDLjmgqqZqZCXWbyjkfzCzY',
        'endpoint_url': 'http://localhost:9000',
        'bucket_name': 'scan-results',
        'cache_dir': '/tmp/flask_s3_viewer',
        'use_cache': True,
        'ttl': 86400
    }
)


# Apply FlaskS3Viewer blueprint
s3viewer.register()

# Usage: python example.py test (run debug mode)
if __name__ == '__main__':
    debug = False
    if len(sys.argv) > 1:
        if sys.argv[1] == 'test':
            debug = True
    app.run(debug=debug, port=3000)
