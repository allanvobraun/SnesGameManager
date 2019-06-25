# decorator usado para arrumar a thread
# https://stackoverflow.com/questions/19760001/how-to-ensure-qprogressdialog-is-shown-in-pyqt/30093084#30093084


def nongui(fun):
    """Decorator running the function in non-gui thread while
    processing the gui events."""
    from multiprocessing.pool import ThreadPool
    from PyQt5.QtWidgets import QApplication

    def wrap(*args, **kwargs):
        pool = ThreadPool(processes=1)
        async = pool.apply_async(fun, args, kwargs)
        while not async.ready():
            async.wait(0.01)
            QApplication.processEvents()
        return async.get()
    return wrap
