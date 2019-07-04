import os
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

if __name__ == '__main__':
    import sys
    from core import app

    sys.exit(app.run_app())
