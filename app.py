from operator import truediv
import sys

from flask import Flask
from flask_s3_viewer import FlaskS3Viewer
from flask_s3_viewer.aws.ref import Region

import os

app = Flask(__name__)


def getEnvVar(name, defaultValue = None):
    val = os.environ.get(name)
    if val:
        return val
    else:
        if defaultValue:
            return defaultValue
        else:
            raise Exception(f'must set enviroment variable: {name}!')


# For test, disable template caching
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1
app.config['TEMPLATES_AUTO_RELOAD'] = True

# FlaskS3Viewer Init
s3viewer = FlaskS3Viewer(
    app,  # Flask app
    namespace='occ-s3-viewer',  # namespace be unique

    object_hostname=getEnvVar("S3_HOST"),  # file's hostname
    allowed_extensions={},  # allowed extension
    template_namespace='customized',
    config={  # Bucket configs and else
        'profile_name': None,
        'access_key': getEnvVar('S3_ACCESS_KEY'),
        'secret_key': getEnvVar('S3_SECRET_KEY'),
        'endpoint_url': getEnvVar("S3_HOST"),
        'bucket_name': getEnvVar('S3_BUCKET'),
        'cache_dir': '/tmp/flask_s3_viewer',
        'use_cache': True,
        'ttl': getEnvVar('S3_FILE_LIST_CACHE_SECS',86400)
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
    app.run(debug=debug,host='0.0.0.0', port=getEnvVar('PORT'))
