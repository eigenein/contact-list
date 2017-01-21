### Notes

* Main app and API are implemented as two apps within **one Django project** for the sake of simplicity.
* Everywhere I use **local-memory caching** for the sake of simplicity.
* I don't care about Python 2.x compatibility.
* Line width (right margin) is not strictly limited.
* Images are proxified through API just to enable caching and/or ability to replace the source.

### Questions to clarify

* `setup.py` is **missing**.
* CSV file size **is not checked**.
* Image file size **is not checked**.
* Tests are **missing**.

![Screenshot](docs/screenshot.png)
