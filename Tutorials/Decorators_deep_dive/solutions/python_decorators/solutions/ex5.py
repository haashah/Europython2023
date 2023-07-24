"""Decorator for classes
"""

classes = {}


def register(cls):
    """Register classes.
    """
    classes['.'.join((cls.__module__, cls.__name__))] = cls
    return cls


if __name__ == '__main__':

    #  pylint: disable-msg=too-few-public-methods

    @register
    class Sample1:
        """A sample class.
        """

    @register
    class Sample2:
        """A sample class.
        """

    print(classes)
